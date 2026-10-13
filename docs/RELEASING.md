# Release checklist

- [ ] Define the supported behavior, platforms, and acceptance criteria.
- [ ] Run formatting, static checks, unit tests, and the installed CLI.
- [ ] Review dependency and code-security alerts.
- [ ] Document known limitations and breaking changes.
- [ ] Confirm that no secrets, personal data, or restricted assets are shipped.
- [ ] Update the version and write release notes.
- [ ] Test installation from the built distribution in a clean environment.
- [ ] Create a version tag only after review.
- [ ] For deployed services, verify environment configuration, monitoring, access controls, backup / restore, and rollback procedures.

Releases and deployments are manual decisions. This template does not publish packages or deploy infrastructure automatically.
