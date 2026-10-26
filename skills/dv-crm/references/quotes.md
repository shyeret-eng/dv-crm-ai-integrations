# Draft quotes: build, edit, remove, restore
Only admin, manager and manager_sensitive with approved quotes.write may use these tools. Start with quote/event lookup and inspect the current discovered schemas. The quote must be draft and not active for inventory, including drafts originally made by a person. Finalization stays with a person in CRM.

Before building a client's quote, use list_quotes with exact clientId and get_quote to read 1–3 of that client's recent confirmed quotes. Follow their layout, say which quote was followed, and ask the person about conflicts. search_quote_lines also supports exact clientId filtering.

- Services and pass-through costs (trucking, delivery, freight, catering, hotels, flights, per diem, mileage, sub-rentals) are add-on lines with their group; custom lines are physical items only. If add_quote_lines or update_quote_line returns advisory lineTypeHints, tell the person.
- Resolve equipment through search_inventory and labor roles through list_labor_roles. Equipment/labor prices come from the server defaults, never AI-entered overrides. Custom/add-on amounts require pricing rights. An add-on needs exactly one of the six Event P&L groups (Labor, Equipment rental & subs, Trucking, Food, Travel & lodging, Misc); existing add-ons keep their old type until update_quote_line addonType sets a group. A Labor add-on replaces calculated labor in totals and P&L: confirm with the person first. When a quote ignores rental cost, its cost also excludes custom lines.
- create_draft_quote takes event (returned ID or event number), optional name and requestKey. It creates an inactive draft. Use a unique requestKey and reuse it only for a retry of the same request after an uncertain outcome.
- add_quote_lines requires quoteId, requestKey and 1–25 lines (equipment/labor/custom/addon). Placement supports position start/end or afterLineId, never both; target line must be in the same section. Read and report availability warnings: a draft holds nothing and a warning is not a reservation or a refusal.
- Keep line text short: the quote grid shows about 15 characters of Purpose (it also prints in full on the client PDF; limit 80) and about 20 of Notes (the rest only on hover). Use a few client-safe words for Purpose, lead Notes with the key words, and put longer context in the chat. When textWarnings comes back, tell the person the text is partly hidden.
- update_quote_line requires lineId and that line's expectedUpdatedAt. Supply only fields allowed for its type. Equipment/labor prices cannot be changed; labor uses days or hours. Conflicts require a fresh read and intent reassessment.
- reorder_quote_lines receives exactly the section's current line IDs once each; rename_quote_section changes a section name and cannot merge existing sections. Use current quote/line versions where the schema accepts them. Quote-level updatedAt does not represent every line change; always use the line's updatedAt for line edits/removal.

In-House reservation dates follow the item's own dates, then the quote's In-House dates, then the event's equipment dates. Items newly moved from a vendor to In-House follow this fallback too. get_event_equipment reservationDates.layer identifies item, quote or event. Stock numbers in get_event_equipment, get_quote and get_inventory_availability, and shortage checks in set_equipment_sources, add_quote_lines and update_quote_line, use these dates, including other quotes' In-House dates. Edit reservation dates only in the CRM; a draft holds no stock.

## Explicit two-step removal
1. Read the line from get_quote. Call remove_quote_line with lineId and expectedUpdatedAt and **no confirmationCode**. This deletes nothing and returns the exact preview, signed confirmationCode, expiry, and confirmation message. Protected linked lines or non-drafts can be refused before confirmation.
2. Show the preview and ask the person to confirm removal. Only an explicit yes after the preview authorizes the second call. Send the same lineId and expectedUpdatedAt plus that returned code. Never silently approve, fabricate a code, or use a code for a different connection/line/version.

The signed code lasts ten minutes. An expired/tampered code or changed line requires a new preview and new confirmation. A client may also display its own destructive-action prompt; that is separate. The server verifies the code but cannot prove that a human said yes, so the skill must enforce the conversation step.

Removing the last line for an item on a quote also clears that item's own In-House reservation dates; adding it back follows the quote's dates. restore_quote_line does not bring the old dates back.

## Restore within seven days
list_deleted_quote_lines takes quoteId and returns eligible recent deletions with deletedLineId and restorable status. For a user-requested restore, restore_quote_line takes the returned deletedLineId. Restore requires the quote still be an inactive draft, an available line ID, valid referenced items and a recoverable deletion record. It restores the previous line identity/fields/order and issues a new updatedAt. The seven-day window is conditional recovery, not a guarantee; read the returned result.

For profit or margin, read get_quote profitAndLoss (admins only; never estimate it for others).

Never activate, confirm, send, or change quote status through this workflow. Never send messages or calendar invites.
