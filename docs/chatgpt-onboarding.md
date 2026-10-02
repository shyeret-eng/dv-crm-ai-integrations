# ChatGPT web/mobile onboarding and repair

Updated October 2, 2026. Account eligibility and the cloud-registration capability must be checked in the recipient's chat; no universal automatic installer is promised.

## Help teammates one step at a time

Give only the next action in plain language, then wait for the teammate's result. Keep progress short. Put any endpoint or prompt they need to copy in a clearly labeled copy-paste box. Avoid technical explanations unless they are needed to resolve a blocker. Make manual sign-in and permission consent clear; never claim those steps happened automatically. If troubleshooting is needed, give a brief, safe report; offer an optional copyable report for an advisor, without credentials or callback query values.

## Check availability first

First check whether this chat actually exposes a supported cloud-registration capability. Do not assume Plugin Creator is available because a prompt names it. Reuse an already working hosted connection when available. If the cloud tool is missing, do not repeat creation prompts, upload an MCP package, or create a placeholder. Use the direct web route below. If that UI is unavailable too, stop and report the account or workspace-policy blocker.

## Direct web setup: primary fallback

The successful hosted setup used ChatGPT in a web browser: **Plugins → Add → Create MCP App**. The saved result was labeled **Your cloud plugin** and offered **Continue connecting app**. A later inspection found no Developer mode toggle under either Plugins settings or Security and login, even though the saved app was labeled DEVELOPMENT. The app's development status therefore does not establish that a separate toggle must be enabled.

**First action:** Open ChatGPT in your web browser and select **Plugins**. Tell your helper whether you see **Add → Create MCP App**. Helpers should wait for that answer before giving the next step.

If that action is available, use it to connect the existing HTTPS Streamable HTTP endpoint, preserving its OAuth. Enter a clear name such as Dynamic Vision CRM, inspect the saved cloud-app label and discovered tools, and continue the app connection when prompted. Complete your own sign-in and permission consent. Installation/enabling and verification remain separate steps. Do not interpret merely creating the app as successful access.

**Copy-paste endpoint**

```text
https://dynamic-vision-erp-rev101.vercel.app/api/mcp
```

This path was observed in one account; it is not a universal UI or eligibility guarantee. If Add or Create MCP App is absent, report the missing control. Do not repeatedly direct someone to a Developer mode toggle they cannot find, or substitute a local package, tunnel, or server.

The [official developer-testing guide](https://developers.openai.com/plugins/deploy/connect-chatgpt) documents a separate account-dependent route through **Settings → Security and login → Developer mode**, then Plugins → plus → Connection → HTTPS endpoint. Offer that route only when the actual account exposes those controls. If neither web route is available, stop and report the account/policy blocker. Do not infer eligibility from the endpoint or repository alone.

For a hosted plugin already available to the recipient, open its directory details and use the **plus** installation action, authenticate when prompted, then start a new chat. The directory has workspace and Personal sections when available. A working private plugin in another person's workspace is not automatic access for the recipient; public directory distribution requires its own review/publication. See [installation](https://learn.chatgpt.com/docs/plugins) and [workspace availability](https://learn.chatgpt.com/docs/enterprise/plugin-management).

Existing hosted connection with stale tools: **Dynamic Vision CRM → Manage → Manage app → Refresh tools**, then a new chat. DV **My Preferences → AI Connections → Edit permissions** changes eligible feature permissions separately. Neither refresh nor a copied prompt bypasses consent or CRM account eligibility.

[Official plugin documentation](https://learn.chatgpt.com/docs/plugins) describes general web/mobile plugin support for plugins available to your account, and excludes Desktop only plugins from mobile. This is platform support, not evidence that this individual connection has completed consent or works on a recipient's phone. Verify both surfaces separately.

## Short repository reread prompt

**Copy-paste prompt**

```text
Read https://github.com/shyeret-eng/dv-crm-ai-integrations and its ChatGPT onboarding guide using the latest published revision. Help me connect Dynamic Vision CRM for ChatGPT web and phone. Give me only the next action in plain language, one step at a time; keep progress short and put needed copyable inputs in clearly labeled copy-paste boxes. Give technical diagnostics only when needed, briefly and without secrets. First check whether a supported cloud-registration tool is actually available in this chat. If not, first ask whether my web Plugins menu offers Add → Create MCP App, the observed successful route. Do not assume a Developer mode toggle exists or repeat Plugin Creator prompts. Stop if my account lacks the necessary UI or eligibility. Use the existing remote HTTPS MCP endpoint; do not install a desktop-only MCP package, CLI, local listener, tunnel, or new server. I will complete my own sign-in and consent. Verify a harmless read, then separately verify a new web chat and my phone. Leave the earlier desktop-only entry untouched until the hosted read works; show the exact duplicate and ask before removing it. Never expose credentials, write CRM records, send messages, or activate/confirm quotes.
```

Read the latest published revision. If the guide cannot be read, say so; do not pretend the connection instructions were verified.

## Optional cloud registration when the tool is available

Use the supported personal cloud-registration capability to connect the existing HTTPS Streamable HTTP endpoint https://dynamic-vision-erp-rev101.vercel.app/api/mcp, preserving hosting and OAuth. Reuse a working personal cloud connection; do not assume another person's workspace sharing gives you access. Return the actual link supplied by successful registration. Creation, installation/enabling and personal consent are separate steps. Package-upload create_plugin is not a substitute: raw MCP import remains desktop-only. Do not invent plugin IDs or links. Mark creation, installation, OAuth, read, web and mobile checks independently; pending is not success.

## Acceptance record

Record pass, fail, or pending for each item, without business payloads or tokens:

- Account eligibility checked; supported cloud tool or direct web UI route identified.
- Existing hosted connection reused, or exactly one personal cloud connection created with its real returned link.
- Plugin installed/enabled separately from creation.
- Recipient completed their own DV sign-in and OAuth consent.
- Discovered tools and one harmless read verified.
- New ordinary ChatGPT web conversation verified.
- Same-account mobile conversation verified.
- Exact duplicate local entry identified; removal separately confirmed and verified.

The recipient's hosted flow has not been tested here. The redacted browser error shows an HTTP loopback /callback navigation blocked by HTTPS-only browsing (WebKit 305). This identifies the navigation failure in the desktop-only client flow; it does not diagnose a production OAuth fault. The CRM MCP endpoint was already remote. Do not disable browser security, replay callback codes, rewrite URLs, or change production OAuth on this evidence. Never record callback query strings or fragments.

## Evidence and boundaries

The earlier guide assumed an installed hosted connection and omitted its successful creation path. Raw MCP package import is desktop-only even with an HTTPS endpoint. Workspace sharing does not cover teammates outside that workspace. Repository access grants neither ChatGPT plugin access nor DV permissions. See [workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management), [plugin installation](https://learn.chatgpt.com/docs/plugins), and [developer connection testing](https://developers.openai.com/plugins/deploy/connect-chatgpt).

The account package-upload create_plugin flow is not a substitute for the cloud-registration capability requested here. Cloud-registration capabilities differ between chats and must be checked at runtime. The successful setup was performed through the browser UI, not by assuming Plugin Creator tool availability. This document supplies the observed web path when that capability is unavailable; no private app identifiers or inferred links are included.

