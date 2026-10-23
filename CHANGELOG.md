# Changelog

## 0.8.0 — 2026-10-23
- Refresh from the supplied CRM changelog for server 1.20.0–1.21.0: 49 tools, 17 scopes and role eligibility unchanged; no new tools.
- 1.20.0: equipment reservations support HH:MM times, a time zone and partial windows. Timed ranges are [start, end), missing times mean whole days, and same-day flips count once in inventory availability. Equipment reads show times and partials; source, quote-add and production-row checks use timed counting. Times and partial windows are edited only in the CRM.
- 1.20.1: partial windows match stock counting (clipped to the item window and capped at held In-House units); equipment shortages and source/quote-add/quote-update warnings count other reservations during partial windows.
- 1.21.0: get_event_equipment pages by whole item; follow nextCursor with unchanged filters until null before drawing conflict, shortage or whole-quote conclusions. Adds sections/itemIds filters, unmatchedSections, itemsOnly, itemsTotal/itemsReturned and reservationDates timeZoneVenue, reservedLines and partialsTotal; changed event, quote, filters or quote items require restarting without a cursor.

## 0.7.1 — 2026-10-22
- Refresh to production main, CRM AI server 1.19.1: 49 tools, 17 scopes (unchanged).
- Quote lines: the quote grid shows only about 15 characters of Purpose (Purpose also prints in full on the client PDF) and about 20 of Notes; the rest shows on hover. Purpose write limit is now 80 characters (Notes stays 1000). add_quote_lines and update_quote_line return textWarnings when written text runs past what the grid shows.

## 0.7.0 — 2026-10-21
- Refresh to production main, CRM AI server 1.19.0: 49 tools, 17 scopes (no new scope).
- Add shift groups (the named staffing blocks in Schedule Management, not Production Schedule rows), scope schedule.write (also needs schedule.read; admin, manager, manager_sensitive): create_shift_groups (1 to 20 groups per call, optional open role slots up to 100, a requestKey for safe retries, overnight when end is at or before start), update_shift_group (pass the group's updatedAt as expectedUpdatedAt; slots without their own times follow the new hours, slots with their own times keep them; crew overlaps are refused) and delete_shift_group (always two steps: preview, explicit yes, confirmation code; only groups with no assigned crew). Nothing is sent; invitesOutOfDate means resend the invite from the CRM.
- get_event_schedule shift groups now include updatedAt.
- add_production_rows: reusing a requestKey with only part of the earlier rows is now refused instead of treated as a retry.
- Tool counts per role: admin 49, manager 45, manager_sensitive 46, warehouse_manager 21, user 11.

## 0.6.0 — 2026-10-15
- Refresh to production main, CRM AI server 1.18.1: 46 tools, 17 scopes.
- Add the production schedule: get_production_schedule (events.read, every role) and add_production_rows, update_production_row, remove_production_row (new scope production.write; admin, manager, manager_sensitive; also needs events.read). Changes pass the row's updatedAt as expectedUpdatedAt, use HH:MM venue-time times and a requestKey for retries; equipment conflicts are refused; removal is always two steps (preview, explicit yes, confirmation code) and cannot be undone with the AI tools. Nothing is sent to crew; invitesOutOfDate means resend the invite from the CRM.
- 1.16.0: quote add-ons require one of six Event P&L groups; ignoring rental cost also excludes custom lines from quote cost.
- 1.17.0 and 1.17.1: equipment uses per-item reservation dates (last day inclusive, edited only in the CRM); a saved equipment plan holds no stock.
- 1.18.1: Needs Attention card counts skip duplicate charges from an old standalone card.
- Edit permissions is now grouped, with "Turn on everything my role allows", "New" badges and an "N more permissions available" note; ticking a Change permission also ticks the See it needs. Guidance updated.
- Update the role/tool matrix (production.write column), checks and synthetic examples.

## 0.5.3 — 2026-10-13
- Refresh to CRM AI server 1.15.2: Needs Attention card transaction counts now include charges the bank feed mislabels as a card payment. No new tools or scopes.

## 0.5.2 — 2026-10-13
- Stop publishing install packages: remove the old 0.3.x packages and point links to the canonical skill folder. Packages can still be built locally with scripts/release.py.

## 0.5.1 — 2026-10-13
- Refresh to production main, CRM AI server 1.15.1: 42 tools, 16 scopes (no new tools or scopes).
- Schedule writes check double booking across events: a different location at the same time is refused; the same location asks for a confirmation on assign_shift.
- get_event_equipment adds vendor logistics per section preset (sectionPresets): separate pickup and return details for a named group of sections.

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
