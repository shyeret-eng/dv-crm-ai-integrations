# Edit permissions and refresh
In Dynamic Vision CRM open **My Preferences → AI Connections → Edit permissions** for your existing connection. Tick the required feature and save. For an active eligible grant, no reconnect is needed: the server checks current grant scopes on every call. events.read must stay selected. Role limits, disabled AI access, blocked apps and expired/revoked grants remain separate checks.

Then refresh the AI client: **Cursor** switch the MCP off, wait about 30 seconds, then on; **Hosted ChatGPT Dynamic Vision CRM plugin** open the existing plugin → Manage, scroll down to Manage app, then select Refresh tools below App description. Starting a new chat alone may leave a stale registered tool list unchanged; refresh tools first. Other hosts need their supported discovery/update flow; reconnect only if tools still do not appear and the error indicates it is needed.

OAuth consent initially approves scopes. Role eligibility grants nothing by itself. DV permission editing explicitly changes the owner's grant, but host policies/cached tool lists can still limit availability. Ask get_whats_new for yourTools and permissionsYouCanAdd; do not promise silent access expansion.

CRM Edit permissions changes approved scopes; hosted ChatGPT Refresh tools updates registered metadata. Refresh does not grant scopes, change role, reconnect OAuth, or require a duplicate/rebuilt app. Check discovery and get_whats_new; tool counts can change. Developer-mode connections use their connection Refresh flow.

New permissions (equipment.read, equipment.write, labor.finance, schedule.write) are not added to existing connections automatically. Open Edit permissions, tick them, save, then refresh the AI app; no reconnect is needed. get_whats_new lists permissions you can add and how to enable them. Some need a companion permission: equipment.write needs equipment.read, and schedule.write needs schedule.read.
