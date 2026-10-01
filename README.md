# Dynamic Vision CRM · AI integrations
Connect your AI to Dynamic Vision CRM and use the same short workflow across clients. This public repository contains setup guides, a canonical skill, synthetic examples, and local review packages. **Version 0.3.0 · checked October 1, 2026.**

Your connection uses your own CRM permissions. This repository grants no access. Current capabilities include event/task lookup and permitted writes, inventory availability, Needs Attention, schedules, clients, quote reading and draft quote building/editing/removal/restore. Activity history is admin-only. Finalize quotes yourself in the CRM; AI never activates, confirms, or sends them.

## Get started

1. Follow the [client setup guide](docs/platforms.md). Keep the existing hosted ChatGPT connection when it already works on web/mobile; a raw MCP package is not a replacement for that cloud connection.
2. In CRM **My Preferences → AI Connections → Edit permissions**, enable the features you need, then refresh your AI client.
3. Ask: **“What’s new, and what can my connection do?”** The live `get_whats_new` tool reports available tools and permissions you can add.

See the [role/tool matrix](skills/dv-crm/references/capabilities.md), [draft quote workflow](skills/dv-crm/references/quotes.md), [synthetic examples](skills/dv-crm/references/examples.md), and [canonical skill](skills/dv-crm/SKILL.md).

## Packages and checks

Review/download files under [dist/0.3.0](dist/0.3.0/release-index.json). Portable is skills-only; Claude Code and Gemini CLI packages use the existing MCP endpoint. Host setup, OAuth approval, and tool discovery are still required. Runtime/OAuth tests were not performed by this repo.

```sh
python3 scripts/release.py
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/audit_public.py
```

For official portable manifest schema validation, install requirements-dev.txt in a local virtual environment and run `scripts/check.py --schema`. If Claude Code is installed, run `claude plugin validate --strict dist/0.3.0/claude/dv-crm`.

[Release/update behavior](docs/releases.md) · [Changelog](CHANGELOG.md) · [Sources](docs/sources.md) · [Public audit](docs/verification.md).
