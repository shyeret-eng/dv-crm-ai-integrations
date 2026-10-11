# Sources
Checked against production main (MCP server 1.14.0) on October 10, 2026 through non-mutating source reads. Live deployment is reported by the owner; this hub did not query business records. All 42 registered tools, 16 scopes and five role rows were derived from authoritative scope/role/tool declarations. This public repository contains descriptions, not backend source or its private history.

Official packaging and host references reviewed during foundation work; recheck before installation because host behavior changes:

- [Agent Skills](https://agentskills.io/specification)
- [OpenAI skills and snapshots](https://developers.openai.com/plugins/build/skills)
- [OpenAI packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI connection refresh](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [Workspace marketplace sync](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Claude manifest and validation](https://code.claude.com/docs/en/plugins-reference)
- [Claude marketplace updates](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Gemini extensions](https://geminicli.com/docs/extensions/reference/)
- [Gemini MCP](https://geminicli.com/docs/tools/mcp-server/)
- [Gemini custom apps](https://support.google.com/gemini/answer/17209137)
- [Portable plugin schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)

Hosted refresh evidence, October 1, 2026: the user verified Manage → Manage app → Refresh tools below App description; a connected session subsequently discovered refreshed tools and completed read-only get_whats_new/quote/client/schedule calls. This operational finding supplements generic developer-mode documentation. Screenshots, private identifiers and payloads are excluded.

Onboarding review, October 2, 2026: [Plugins directory and installation](https://learn.chatgpt.com/docs/plugins), [developer-mode HTTPS endpoint connection UI](https://developers.openai.com/plugins/deploy/connect-chatgpt), and [workspace availability / desktop-only raw MCP import](https://learn.chatgpt.com/docs/enterprise/plugin-management). The repair guide is not proof of recipient account eligibility or mobile success. A redacted callback error confirms HTTP loopback navigation was blocked by HTTPS-only browsing; OAuth query values and screenshots are excluded. No production OAuth change is justified by that browser error alone.

0.3.3 path correction: original browser-operation history was reread. The successful cloud creation explicitly used Plugins → Add → Create MCP App; subsequent settings inspection found no developer-mode toggle while the app itself was marked DEVELOPMENT. These are observed account-specific UI facts, not a promise that every recipient has the same controls. No private app IDs, source message IDs, account names, auth query values or screenshots are included. Later 0.3.4 instructions supersede those alternatives: only the observed recipient route is prescribed, with stop-on-failure.

0.3.4 recipient-label review: supplied redacted UI evidence confirms Add → Create custom MCP server and a form with OAuth, Advanced OAuth settings, trusted-server consent, and Create as a plugin. This confirms creation controls exist in that recipient UI without a Developer mode toggle; the user reports apparent setup success, while separate consent/read/web/mobile verification remains unrecorded. No screenshots, account identities or OAuth values are included.
