# Synthetic prompts and call patterns
Every name, ID, date and amount here is fictional. Use live lookup IDs, never these fixture IDs, against real CRM.

| Ask your AI | Workflow |
|---|---|
| What's new, and what can my connection do? | get_whats_new; explain available tools and optional permissions |
| Show events from October 5 through October 9, 2026 | list_events with explicit from/to; disclose pagination |
| What needs my attention? | get_needs_attention; distinguish total counts from visible samples |
| Who is working the Demo Summit load-in? | list_events → get_event_schedule using returned event ID |
| What shifts do I have this week? | Resolve person/date range; list_shifts; clarify if identity is unknown |
| Find the contact for Demo Organization | search_clients → get_client; treat returned contacts as private |
| Change Demo Summit to Confirm | Read event then set_event_status using fresh expectedStatus |
| Create a task to check Demo Speaker | create_task; resolve assignees or explain everyone assignment; report approvalState |
| Build an inactive draft with two Demo Speakers | Resolve event/item → create_draft_quote → add_quote_lines → get_quote; report warnings |
| Remove the Demo Speaker line | Read line → removal preview → explicit human yes → second removal call |
| Undo that line removal | list_deleted_quote_lines → user-requested restore_quote_line if restorable |
| Send 5 Demo Lights to Demo Vendor A and 5 to Demo Vendor B | get_event_equipment → set_equipment_sources with the item's version; if needsVendorChoice, ask the user; if needsConfirmation, show the preview and wait for an explicit yes |
| How is labor tracking on Demo Summit? | get_labor_budget; explain the gap by role, day and person (positive is over budget); list_labor_budgets for a date range |
| What is the profit on the Demo Summit quote? | get_quote and read profitAndLoss; admins only, otherwise say it is not available |
| Which shifts are not staffed next week? Who is free Friday 9 to 5 for A1? | list_staffing_gaps; find_available_crew (names only) |
| Put Demo Crew Member on the Demo Summit load-in | find_available_crew → assign_shift with the shift's updatedAt; show any needsConfirmation reasons, wait for an explicit yes; tell the user no invite was sent |
| Approve the pending Demo task request | get_task → review_task_request without a code → show the preview → explicit yes → same call with the returned code |

Synthetic get_whats_new inputs: `{}` or `{"since":"2026-09-30"}` or `{"sinceVersion":"1.0.0"}`; never combine date and version.

Synthetic draft equipment batch shape:
```json
{"quoteId":"demo-quote-001","requestKey":"demo-request-001","lines":[{"type":"equipment","inventoryItemId":"demo-item-001","quantity":2,"section":"Demo Equipment","position":"end"}]}
```

For retries use the same key only for the same operation. Two-step tools (remove_quote_line, review_task_request, set_equipment_sources, shift changes) change nothing on the first call: show the preview and wait for the person's explicit yes before the second call; never confirm on your own. Never insert a fabricated confirmationCode in an example or live call. “Confirm the quote and email it” is unsupported: do neither. “Set the event Completed” is unsupported: that status is automatic. Stale versions mean re-read, explain the conflict, and reassess intent.
