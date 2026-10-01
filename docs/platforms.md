# Client setup
Review your host's current [official documentation](sources.md). Endpoint:
`https://dynamic-vision-erp-rev101.vercel.app/api/mcp`

## ChatGPT and Codex
If your hosted Dynamic Vision CRM connection already works, keep it enabled; use the portable skills-only companion alongside it if your host supports installing that package. Existing web/mobile access is not replaced by a raw desktop MCP package. New connections require approved account/host access and OAuth consent. This repo does not create a hosted plugin or map private app IDs.

For developer-mode connections, Refresh metadata after server tool changes and start a new chat. Published plugin tool updates have their own review behavior; imported skills are snapshots requiring a new version. Workspace GitHub marketplace import requires an administrator's opt-in and authorization; new imports default to daily sync. Publishing this repository alone does not import or install it anywhere.

## Claude Code
Review generated files, then from this repository:
```sh
claude --plugin-dir ./dist/0.3.0/claude/dv-crm
```
Use `/mcp` to authenticate. Approve only needed role-eligible scopes; avoid a duplicate connection if the same endpoint is already configured. Native manifest validation passed; runtime/OAuth has not been tested by this hub.

A future marketplace install requires registration and installation. Third-party auto-update is off by default; users/admins opt in, versions must change, and host reload/new-session behavior applies. There is no marketplace manifest in this repository.

## Gemini CLI
Review generated files, then:
```sh
gemini extensions install ./dist/0.3.0/gemini/dv-crm
```
The extension uses httpUrl for Streamable HTTP and has no fixed includeTools list. The server governs caller exposure. Complete host OAuth consent and inspect discovery; compatibility is untested by this hub. Extensions are copied on install; use `gemini extensions update dv-crm` and restart. Auto-update is opt-in; installation does not bypass consent.

## Gemini web/mobile
Custom apps currently require a personal Google Account, age 18+, US availability, English, and Keep Activity on; work/school accounts are excluded. Connect in web Settings → Connected Apps → Custom apps with the endpoint and follow consent, then use on web/mobile. Stop on unsupported auth instead of improvising credentials. Consumer skill uploads and CLI extensions are separate; no automatic snapshot refresh is promised.

## Cursor
Use your host's remote MCP setup with the endpoint and OAuth. Existing connections: enable newly needed permissions in DV, switch MCP off, wait about 30 seconds, then on. No Cursor configuration package is generated here. Runtime compatibility must be checked in the target client.

## Enable newly shipped features
Follow [Edit permissions and refresh](../skills/dv-crm/references/permissions.md), then ask what's new. [Role eligibility](../skills/dv-crm/references/capabilities.md) is not proof of an enabled account/grant.

Try synthetic prompt patterns with an approved test record. Write/removal tests need explicit authorization for that record. Record only pass/fail and redacted errors; never commit live payloads, contacts, prices or tokens.
