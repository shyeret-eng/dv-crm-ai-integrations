# Changelog

## 0.5.0 — 2026-10-10
- Refresh to production main, CRM AI server 1.14.0: 42 tools, 16 scopes.
- Add create_event and search_venues (events.create; admins only for now). The client and venue must already exist; the AI never creates either and asks the person to add a missing one in the CRM.
- create_event is always two steps: preview with possible duplicates, the person's explicit yes, then confirmationCode and requestKey. The event starts as Created, is never confirmed, nothing is sent to clients or crew, bookkeeping gets the CRM's usual new-job alert, and one event can be created per person per hour.
- Document 1.12-1.13: invalid shift hours are refused; labor budget and quote actual labor use paid hours; Needs Attention card transactions follow each card's start date; dismissed Old Westbury requests leave attention; task requests notify reviewers in the Team app.
- Update the role/tool matrix, permissions, synthetic example and release checks.

## 0.4.0 — 2026-10-07
- Refresh to production main, CRM AI server 1.11.0: 40 tools, 15 scopes.
- Add request_task_edit and review_task_request (approvers only; preview, explicit yes, then confirmation code).
- Add get_event_equipment (equipment.read) and set_equipment_sources (equipment.write; vendor choice and over-allocation confirmation).
- Add get_labor_budget and list_labor_budgets (labor.finance); get_quote profitAndLoss (admins only); inventory broken/usable counts and unit weight.
- Add list_staffing_gaps, find_available_crew, and assign_shift, create_shifts, update_shift_times (schedule.write; invites are never sent).
- Document write limits per hour and enabling new permissions in Edit permissions without reconnecting.
- Update the role/tool matrix, workflows, synthetic examples and release checks.

## 0.3.4 — 2026-10-02
- Use the exact observed Create custom MCP server → Create as a plugin route; stop on absence/failure without alternate installation attempts.
- Preserve OAuth/default advanced settings and personal trusted-server consent.
- Record user-reported apparent setup success separately from unverified read/web/mobile checks.
- Identify the canonical standalone skill archive without claiming attachment to the hosted app.

## 0.3.3 — 2026-10-02
- Correct the first-time hosted path to the observed web Plugins → Add → Create MCP App flow.
- Keep official developer-mode setup as an account-dependent alternative, without requiring a missing toggle.
- Retain one-step guidance, own sign-in/consent, and recipient web/mobile verification gates.

## 0.3.2 — 2026-10-02
- Add hosted-first ChatGPT onboarding, actual tool-availability gates, direct web fallback, and a short repository reread prompt.
- Separate desktop-only client setup from the existing remote CRM server and HTTP loopback callback failure.
- Document supported UI fallback, independent installation/consent, and pending web/mobile acceptance checks.
- Add one-step plain-language teammate guidance and clearly labeled copy-paste inputs.
- Regenerate packages; no server, OAuth, plugin, or grant changes.

## 0.3.1 — 2026-10-01
- Document verified hosted ChatGPT plugin → Manage → Manage app → Refresh tools below App description.
- Distinguish metadata refresh from CRM permissions, OAuth reconnect and new chats.
- Record dated discovery/live read evidence without private screenshots, IDs or payloads.
- Regenerate consistent packages; keep Cursor steps unchanged.

## 0.3.0 — 2026-10-01
- Document shipped schedule/client/quote tools and live get_whats_new.
- Add inactive draft quote building/editing, signed 10-minute two-step line removal, and seven-day conditional restore.
- Refresh all 29 tools, 11 scopes and five role eligibility rows from production main.
- Prepare a public-safe initial source history and current release packages with synthetic examples only.
- Preserve host consent/refresh boundaries; no live grants, plugin edits or CRM writes performed.

Earlier local review candidates are superseded and excluded from the public repository.
