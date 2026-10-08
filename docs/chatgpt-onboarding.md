# ChatGPT web/mobile onboarding and repair

Updated October 2, 2026. Use the exact observed web route below. A recipient reported that this route appeared to work; a separate harmless read, new web chat, and mobile check have not yet been verified for that connection.

## Help teammates one step at a time

Give only the next action in plain language, then wait for the result. Keep progress short. Put inputs they need to copy in clearly labeled code boxes. Explain manual sign-in, permission consent and trusted-server risk honestly. Give technical diagnostics only when needed, briefly and without secrets; an optional copyable advisor report must exclude credentials, callback query values and business records.

## Exact web setup

Keep an already working hosted connection. For a new connection, use **Plugins → Add → Create custom MCP server → Create as a plugin** in ChatGPT's web browser UI. Do not assume this menu is available to every account.

**First action:** Open ChatGPT on the web and select **Plugins → Add**. Tell your helper whether **Create custom MCP server** appears. The helper waits for that answer before the next action.

Then guide the user through these actions individually:

1. Select **Create custom MCP server**.
2. Enter the name below and a description such as “Access Dynamic Vision CRM within my approved permissions.”
3. Enter the existing remote HTTPS Streamable HTTP endpoint below.
4. Keep **OAuth** selected and leave **Advanced OAuth settings** at their defaults. Do not invent client IDs, secrets or authentication URLs.
5. Read the trusted-server warning. The user decides whether to accept its checkbox personally.
6. Select **Create as a plugin**. Follow installation/enabling and connection prompts; complete the user's own DV sign-in and OAuth permission consent personally.
7. Inspect discovered tools and verify one harmless permitted read. Use get_whats_new only if available. Then verify a new web chat and the same-account phone separately.

**Copy-paste name**

```text
Dynamic Vision CRM
```

**Copy-paste endpoint**

```text
https://dynamic-vision-erp-rev101.vercel.app/api/mcp
```

**Stop rule:** If the menu is missing, creation fails, sign-in fails, or tools cannot be used, stop. Give one short blocker and the next needed evidence, such as the missing menu label or a redacted error. Do not attempt another installation route, a Developer-mode detour, a Plugin Creator prompt loop, an archive upload, a desktop package, CLI, localhost listener, tunnel or new server. Do not bypass browser security, replay OAuth codes or change production authentication.

Only after the hosted read succeeds, show the exact earlier duplicate desktop-only DV entry and its proposed removal. Ask for confirmation before removing that one entry; preserve other plugins, files, grants and server code.

## Short repository reread prompt

**Copy-paste prompt**

```text
Read https://github.com/shyeret-eng/dv-crm-ai-integrations/blob/main/docs/chatgpt-onboarding.md. Guide me one simple action at a time through Plugins → Add → Create custom MCP server → Create as a plugin. Use the documented DV HTTPS endpoint and OAuth; label inputs I must copy. I will complete sign-in and consent. If this route is missing or fails, stop with one short blocker and the next evidence needed—no alternate installation attempts. Verify a harmless read, then web and phone separately. Ask before removing the exact duplicate desktop-only entry.
```

If the guide cannot be read, say so; do not pretend its instructions were verified.

## Acceptance record

Record pass, fail or pending, without live payloads or tokens:

- Exact menu/form available and cloud connection created or existing connection reused.
- Plugin installed/enabled and user's own OAuth consent completed.
- Discovered tools and one harmless read verified.
- New web chat verified.
- Same-account mobile chat verified.
- Exact duplicate identified and any removal separately confirmed.

A user report that setup “appeared to work” does not prove all these checks. [Official plugin documentation](https://learn.chatgpt.com/docs/plugins) describes general web/mobile support for plugins available to your account; Desktop only plugins are excluded from mobile. Verify this particular connection independently.

## Skills are separate from the connection

Creating a custom MCP connection discovers tools; it does not automatically import this repository's canonical skill. The source is [skills/dv-crm/SKILL.md](../skills/dv-crm/SKILL.md), with its adjacent references. The self-contained skill archive is [skill-0.4.0.zip](../dist/0.4.0/skill-0.4.0.zip). Preserve those references when importing; do not copy only the main file.

A supported skill-attachment control on this private hosted app has not been verified. Do not claim the archive was attached or upload a full MCP plugin to replace the cloud connection. [Official skills documentation](https://developers.openai.com/plugins/build/skills) supports packaged skill upload during submission or MCP skill import through Scan Tools in the submission portal; imports are versioned snapshots. That public submission workflow is not proof of an Add skill control on a private custom app. Inspect the actual supported owner UI before choosing an attachment step. No app modification or new MCP resource deployment is performed by this repository.

## Evidence and boundaries

The CRM server was already remote. The earlier desktop-only client flow used an HTTP loopback /callback navigation that HTTPS-only browsing blocked (WebKit 305). This explains that browser navigation failure, not a production OAuth fault. Never record callback query strings or fragments.

The current recipient screenshots establish Create custom MCP server and Create as a plugin labels, OAuth/default advanced settings, and trusted-server consent. Earlier account-specific Create MCP App observations are historical, not an alternate installation instruction. Neither repository access nor another person's private workspace plugin grants CRM access. Raw MCP package import is desktop-only even with HTTPS: see [workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management). [Official developer-testing documentation](https://developers.openai.com/plugins/deploy/connect-chatgpt) provides platform context; its alternate route is not prescribed by this guide.

Existing hosted connection with stale tools: **Dynamic Vision CRM → Manage → Manage app → Refresh tools**, then a new chat. DV **My Preferences → AI Connections → Edit permissions** changes eligible feature permissions separately. Refresh does not bypass consent or account eligibility.
