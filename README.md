# Dynamic Vision CRM · AI integrations
Connect your AI to Dynamic Vision CRM and use the same short workflow across clients. This public repository contains setup guides, a canonical skill, synthetic examples, and local review packages. **Version 0.3.2 · updated October 2, 2026.**

Your connection uses your own CRM permissions. This repository grants no access. Current capabilities include event/task lookup and permitted writes, inventory availability, Needs Attention, schedules, clients, quote reading and draft quote building/editing/removal/restore. Activity history is admin-only. Finalize quotes yourself in the CRM; AI never activates, confirms, or sends them.

## Get started

1. For ordinary **ChatGPT web/mobile**, start with [hosted onboarding and the repair prompt](docs/chatgpt-onboarding.md). Check actual cloud-tool availability first. If absent, use supported direct web setup; stop if its required controls are unavailable. Install/enable the connection and complete your own OAuth consent. Repository access alone does not install a plugin. Raw MCP packages are desktop-only even when the CRM server is remote. Other clients: [setup guide](docs/platforms.md).
2. In CRM **My Preferences → AI Connections → Edit permissions**, enable the features you need, then refresh your AI client. For stale hosted ChatGPT tools use **plugin → Manage → Manage app → Refresh tools** ([exact steps](docs/platforms.md#refresh-the-hosted-chatgpt-tool-list)).
3. Ask: **“What’s new, and what can my connection do?”** The live `get_whats_new` tool reports available tools and permissions you can add.

When guiding teammates, give one plain-language action at a time and label inputs they need to copy. Sign-in and consent remain manual. [Copy-paste connection prompt](docs/chatgpt-onboarding.md#short-repository-reread-prompt).

See the [role/tool matrix](skills/dv-crm/references/capabilities.md), [draft quote workflow](skills/dv-crm/references/quotes.md), [synthetic examples](skills/dv-crm/references/examples.md), and [canonical skill](skills/dv-crm/SKILL.md).

## Packages and checks

Review/download files under [dist/0.3.2](dist/0.3.2/release-index.json). Portable is skills-only; Claude Code and Gemini CLI packages use the existing MCP endpoint. Host setup, OAuth approval, and tool discovery are still required. Package installation/OAuth tests were not performed by this repo; hosted ChatGPT refresh and subsequent live reads were verified in a connected session.

```sh
python3 scripts/release.py
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/audit_public.py
```

For official portable manifest schema validation, install requirements-dev.txt in a local virtual environment and run `scripts/check.py --schema`. If Claude Code is installed, run `claude plugin validate --strict dist/0.3.2/claude/dv-crm`.

[Release/update behavior](docs/releases.md) · [Changelog](CHANGELOG.md) · [Sources](docs/sources.md) · [Public audit](docs/verification.md).
