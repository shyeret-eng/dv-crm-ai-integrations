# Client setup
Review your host's current [official documentation](sources.md). Endpoint:
`https://dynamic-vision-erp-rev101.vercel.app/api/mcp`

## ChatGPT and Codex
For ordinary ChatGPT web/mobile, follow [hosted onboarding](chatgpt-onboarding.md) first. Keep a working hosted connection. New teammates can register their own eligible cloud connection; workspace sharing alone does not cover teammates outside that workspace. Creation, installation and OAuth consent are separate steps. Check actual cloud-tool availability first. When it is missing, use the guide's direct web setup instead of repeated creation prompts. Stop if the account lacks that UI or required access. Do not substitute the CLI packages below.

The CRM server is already remote. A desktop-only client connection to it does not mean the CRM server is local. Any imported package declaring mcp.json or .mcp.json is desktop-only even with HTTPS; this repository's portable package is a skills-only companion and creates no hosted connection. See [official workspace rules](https://learn.chatgpt.com/docs/enterprise/plugin-management).

### Refresh the hosted ChatGPT tool list

When CRM permissions are enabled but the hosted Dynamic Vision CRM plugin still shows an older tool list:

1. Open the existing **Dynamic Vision CRM plugin → Manage**.
2. Scroll down to **Manage app**.
3. Select **Refresh tools**, below **App description**.
4. Check the refreshed tool list and ask “What’s new, and what can my connection do?” get_whats_new reports yourTools and permissionsYouCanAdd when available. A new chat can then use refreshed metadata.

**CRM Edit permissions changes your grant; Refresh tools updates ChatGPT’s registered tool metadata.** Starting a new chat alone did not fix the verified stale registration. Refresh does not approve scopes, change your role, reconnect OAuth, or require a duplicate/rebuilt app. If permissions are missing, approve the desired eligible scopes in CRM first, then refresh the existing app.

Verified October 1, 2026: the stale registration exposed 12 tools despite 11 CRM permissions. After Refresh tools, the connection exposed 29 tools (19 read, 10 write); get_whats_new reported serverVersion 1.3.1 and no missing permissions, and quote/client/schedule reads succeeded. These counts are a dated snapshot, not a permanent expectation. Check the current discovered list and live result. Private screenshots, app identifiers and business payloads are excluded.

For developer-mode connections, Refresh metadata after server tool changes and start a new chat. Published plugin tool updates have their own review behavior; imported skills are snapshots requiring a new version. Workspace GitHub marketplace import requires an administrator's opt-in and authorization; new imports default to daily sync. Publishing this repository alone does not import or install it anywhere.

## Claude Code
Review generated files, then from this repository:
```sh
claude --plugin-dir ./dist/0.3.2/claude/dv-crm
```
Use `/mcp` to authenticate. Approve only needed role-eligible scopes; avoid a duplicate connection if the same endpoint is already configured. Native manifest validation passed; runtime/OAuth has not been tested by this hub.

A future marketplace install requires registration and installation. Third-party auto-update is off by default; users/admins opt in, versions must change, and host reload/new-session behavior applies. There is no marketplace manifest in this repository.

## Gemini CLI
Review generated files, then:
```sh
gemini extensions install ./dist/0.3.2/gemini/dv-crm
```
The extension uses httpUrl for Streamable HTTP and has no fixed includeTools list. The server governs caller exposure. Complete host OAuth consent and inspect discovery; compatibility is untested by this hub. Extensions are copied on install; use `gemini extensions update dv-crm` and restart. Auto-update is opt-in; installation does not bypass consent.

## Gemini web/mobile
Custom apps currently require a personal Google Account, age 18+, US availability, English, and Keep Activity on; work/school accounts are excluded. Connect in web Settings → Connected Apps → Custom apps with the endpoint and follow consent, then use on web/mobile. Stop on unsupported auth instead of improvising credentials. Consumer skill uploads and CLI extensions are separate; no automatic snapshot refresh is promised.

## Cursor
Use your host's remote MCP setup with the endpoint and OAuth. Existing connections: enable newly needed permissions in DV, switch MCP off, wait about 30 seconds, then on. No Cursor configuration package is generated here. Runtime compatibility must be checked in the target client.

## Enable newly shipped features
Follow [Edit permissions and refresh](../skills/dv-crm/references/permissions.md), then ask what's new. [Role eligibility](../skills/dv-crm/references/capabilities.md) is not proof of an enabled account/grant.

Try synthetic prompt patterns with an approved test record. Write/removal tests need explicit authorization for that record. Record only pass/fail and redacted errors; never commit live payloads, contacts, prices or tokens.
