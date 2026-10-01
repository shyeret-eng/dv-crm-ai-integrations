# Integration hub instructions
Keep this repository thin: client setup, a canonical skill, synthetic examples, and reproducible packages. Use Dynamic Vision CRM in user-facing text.
Never add credentials, tokens, real customer/personnel/event/financial records, local user paths, private app/session identifiers, backend source, or unrelated internal information. Examples must be synthetic.
Edit canonical files, bump VERSION, regenerate with python3 scripts/release.py, and run scripts/check.py, tests, and scripts/audit_public.py. Generated packages must carry the same skill references. Do not hand-edit them.
Discovered MCP schemas and caller permissions govern use. Preserve optimistic concurrency and the explicit two-step quote-line removal confirmation. Never send messages, activate/confirm quotes, approve/delete tasks, or change live grants/plugins through this hub.
Inspect authoritative production source without switching or modifying its checkout when refreshing documentation. Publishing the integration hub does not authorize publishing CRM source or secrets.
