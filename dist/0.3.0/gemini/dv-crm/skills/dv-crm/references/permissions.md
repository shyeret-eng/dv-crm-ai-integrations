# Edit permissions and refresh
In Dynamic Vision CRM open **My Preferences → AI Connections → Edit permissions** for your existing connection. Tick the required feature and save. For an active eligible grant, no reconnect is needed: the server checks current grant scopes on every call. events.read must stay selected. Role limits, disabled AI access, blocked apps and expired/revoked grants remain separate checks.

Then refresh the AI client: **Cursor** switch the MCP off, wait about 30 seconds, then on; **ChatGPT** start a new chat or use connection Refresh. Other hosts need their supported discovery/update flow; reconnect only if tools still do not appear and the error indicates it is needed.

OAuth consent initially approves scopes. Role eligibility grants nothing by itself. DV permission editing explicitly changes the owner's grant, but host policies/cached tool lists can still limit availability. Ask get_whats_new for yourTools and permissionsYouCanAdd; do not promise silent access expansion.
