# Capability snapshot · October 7, 2026
MCP server 1.11.0, 40 tools, 15 scopes. Verified against production main source; live deployment is reported by the owner. No live records were queried for this guide. Discovered caller schemas are authoritative.

| Tools | Scope |
|---|---|
| get_whats_new, list_events, get_event | events.read |
| set_event_status | events.status |
| list_activity | activity.read |
| list_tasks, get_task, list_task_assignees | tasks.read |
| create_task, update_task, request_task_edit, review_task_request | tasks.write |
| search_inventory, get_inventory_availability | inventory.read |
| get_needs_attention | attention.read |
| get_event_schedule, list_shifts, list_staffing_gaps, find_available_crew | schedule.read |
| list_quotes, get_quote, search_quote_lines | quotes.read |
| search_clients, get_client | clients.read |
| list_labor_roles, create_draft_quote, add_quote_lines, reorder_quote_lines, rename_quote_section, update_quote_line, remove_quote_line, list_deleted_quote_lines, restore_quote_line | quotes.write |
| get_event_equipment | equipment.read |
| set_equipment_sources | equipment.write |
| get_labor_budget, list_labor_budgets | labor.finance |
| assign_shift, create_shifts, update_shift_times | schedule.write |

## Role eligibility

All five roles can hold events.read, tasks.read, tasks.write, attention.read; this includes get_whats_new. Additional scopes:

| Role | events.status | activity.read | inventory.read | schedule.read | quotes.read | quotes.write | clients.read | equipment.read | equipment.write | labor.finance | schedule.write |
|---|---|---|---|---|---|---|---|---|---|---|---|
| admin | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| manager | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| manager_sensitive | Yes | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| warehouse_manager | No | No | Yes | Yes | Yes | No | No | Yes | No | No | No |
| user | No | No | No | No | No | No | No | No | No | No | No |

Eligibility is not authorization: AI access must be enabled, the connection active, and scope approved. Server discovery and every call enforce the current role/grant. The hub neither enables users nor changes access.

Admin and manager_sensitive create approved tasks and can edit task content. Manager, warehouse_manager and user create pending Open requests. The first four roles can change approved task status; basic users can change only approved tasks directly assigned to them. Pending requests cannot change status before approval. request_task_edit proposes a change to an approved task; the task stays unchanged until an approver accepts it in the CRM (basic users: only tasks they created). review_task_request approves or declines a pending task or edit request, only for roles that can approve tasks (admin, manager_sensitive), and always in two steps (see [safeguards](quotes.md)). No task delete or meeting/invite tools are included. Task updates require the latest updatedAt.

Quote structure is visible to warehouse_manager; money/prices/costs are hidden, and money-containing text can be redacted. Managers and manager_sensitive see quote prices/costs but not profit/margin; admin sees financials: get_quote returns profitAndLoss for admins only, following the quote's saved labor basis (quoted or actual). Basic users have no quote access. Quote writes are inactive drafts only. See [safeguards](quotes.md).

Schedules expose shifts, venue-local times, role assignments and booking status; no crew contact/pay details. list_staffing_gaps shows open, awaiting-reply and declined shifts; find_available_crew returns names only, applying the Scheduler's overlap and approved time off rules. schedule.write (assign_shift, create_shifts, update_shift_times) changes crew and shift times with the CRM's checks; overlaps are refused, approved time off needs a confirmation, and invites, WhatsApp requests and calendar events are never sent: send them from the CRM. It needs schedule.read as well. Client tools expose permitted organization/contact/billing details, never quote prices. Real outputs can be sensitive: do not paste them into public issues, examples, or this repository.

equipment.read shows each item's In-House, vendor and unassigned units, shortages and saved logistics, never prices or vendor contacts. equipment.write (set_equipment_sources) splits units between In-House, existing vendors and not assigned; the person chooses among unclear vendor names, vendors are never created, and over-allocation needs a confirmation. labor.finance (get_labor_budget, list_labor_budgets) shows labor budget against scheduled cost, including crew pay rates, never contact, tax or payment details.

## Write limits per hour
Tasks, approvals and event status: 30 per connection, 60 per person. Shift changes, quote building and equipment sources: 60 per connection, 120 per person. Previews that change nothing do not count as writes.

Activity dates use New York (up to seven days); inventory ranges support up to ten IDs/31 days. Paginated lists and Needs Attention counts may exceed displayed samples. Reads can record logs and reconcile statuses internally; inventory reads do not reserve stock.
