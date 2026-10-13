import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automation_starter.cli import CHUNK_SIZE, describe_file, main


class ChecksumTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def make_file(self, name, content):
        path = self.root / name
        path.write_bytes(content)
        return path

    def test_known_checksum_and_size(self):
        path = self.make_file("sample.txt", b"abc")
        self.assertEqual(
            describe_file(path),
            {
                "path": str(path),
                "bytes": 3,
                "sha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            },
        )
        self.assertEqual(path.read_bytes(), b"abc")

    def test_empty_file(self):
        path = self.make_file("empty", b"")
        result = describe_file(path)
        self.assertEqual(result["bytes"], 0)
        self.assertEqual(result["sha256"], hashlib.sha256(b"").hexdigest())

    def test_file_larger_than_one_chunk(self):
        content = b"abcdef" * (CHUNK_SIZE // 6 + 17)
        path = self.make_file("large.bin", content)
        result = describe_file(path)
        self.assertEqual(result["bytes"], len(content))
        self.assertEqual(result["sha256"], hashlib.sha256(content).hexdigest())

    def test_directory_rejected(self):
        with self.assertRaisesRegex(ValueError, "not a regular file"):
            describe_file(self.root)

    def test_multiple_files_and_unicode_paths(self):
        paths = [self.make_file("espacio y ñ.txt", b"one"), self.make_file("two", b"two")]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main([str(path) for path in paths])
        self.assertEqual(status, 0)
        results = json.loads(output.getvalue())
        self.assertEqual([item["path"] for item in results], [str(path) for path in paths])
        self.assertEqual([item["bytes"] for item in results], [3, 3])

    def test_failure_does_not_emit_partial_json(self):
        valid = self.make_file("valid", b"ok")
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            status = main([str(valid), str(self.root / "missing")])
        self.assertEqual(status, 2)
        self.assertEqual(output.getvalue(), "")
        self.assertIn("not a regular file", errors.getvalue())

    def test_permission_error_is_reported(self):
        path = self.make_file("unreadable", b"data")
        errors = io.StringIO()
        with (
            patch.object(Path, "open", side_effect=PermissionError("access denied")),
            contextlib.redirect_stderr(errors),
        ):
            status = main([str(path)])
        self.assertEqual(status, 2)
        self.assertIn("access denied", errors.getvalue())

    def test_missing_arguments_fail(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
            main([])
        self.assertEqual(caught.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
