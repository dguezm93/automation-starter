"""Produce JSON checksums for explicit file paths without modifying inputs."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

CHUNK_SIZE = 1024 * 1024


def describe_file(path: Path) -> dict[str, str | int]:
    """Hash a regular file in bounded chunks; raise on missing or unreadable input."""
    if not path.is_file():
        raise ValueError(f"not a regular file: {path}")
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while chunk := stream.read(CHUNK_SIZE):
            digest.update(chunk)
            size += len(chunk)
    return {"path": str(path), "bytes": size, "sha256": digest.hexdigest()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print SHA-256 checksums as JSON.")
    parser.add_argument("files", type=Path, nargs="+", help="files to inspect (read-only)")
    args = parser.parse_args(argv)
    try:
        results = [describe_file(path) for path in args.files]
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0
