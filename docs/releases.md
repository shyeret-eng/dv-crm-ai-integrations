# Reproducible releases
Edit canonical sources, update VERSION and CHANGELOG, then run release.py, check.py --schema, tests and audit_public.py. Review generated UPDATE-ACTIONS.md and SHA-256 index before handing off.

Packages use one root directory and include hidden native manifests. Generation does not install, contact CRM, notify staff or publish. Treat generated manifests as review candidates until host login/discovery has been tested. Imported skills are versioned snapshots; host refresh and OAuth permission approval remain explicit.

Never hand-edit generated files or re-use a request key for a new CRM operation. To roll back a package, deliberately select a reviewed older version in the host; this does not reverse data changes or grants. Quote-line recovery is a separate server operation with a seven-day window.

Publish only the audited current release and sanitized source history. Local backups/older candidates stay outside publication. A public GitHub link grants access to these guides, not CRM. Workspace/team installations still require their normal administrator/user consent.
