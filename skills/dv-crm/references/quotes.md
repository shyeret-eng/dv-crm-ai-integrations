# Draft quotes: build, edit, remove, restore
Only admin, manager and manager_sensitive with approved quotes.write may use these tools. Start with quote/event lookup and inspect the current discovered schemas. The quote must be draft and not active for inventory, including drafts originally made by a person. Finalization stays with a person in CRM.

- Resolve equipment through search_inventory and labor roles through list_labor_roles. Equipment/labor prices come from the server defaults, never AI-entered overrides. Custom/add-on amounts require pricing rights.
- create_draft_quote takes event (returned ID or event number), optional name and requestKey. It creates an inactive draft. Use a unique requestKey and reuse it only for a retry of the same request after an uncertain outcome.
- add_quote_lines requires quoteId, requestKey and 1–25 lines (equipment/labor/custom/addon). Placement supports position start/end or afterLineId, never both; target line must be in the same section. Read and report availability warnings: a draft holds nothing and a warning is not a reservation or a refusal.
- update_quote_line requires lineId and that line's expectedUpdatedAt. Supply only fields allowed for its type. Equipment/labor prices cannot be changed; labor uses days or hours. Conflicts require a fresh read and intent reassessment.
- reorder_quote_lines receives exactly the section's current line IDs once each; rename_quote_section changes a section name and cannot merge existing sections. Use current quote/line versions where the schema accepts them. Quote-level updatedAt does not represent every line change; always use the line's updatedAt for line edits/removal.

## Explicit two-step removal
1. Read the line from get_quote. Call remove_quote_line with lineId and expectedUpdatedAt and **no confirmationCode**. This deletes nothing and returns the exact preview, signed confirmationCode, expiry, and confirmation message. Protected linked lines or non-drafts can be refused before confirmation.
2. Show the preview and ask the person to confirm removal. Only an explicit yes after the preview authorizes the second call. Send the same lineId and expectedUpdatedAt plus that returned code. Never silently approve, fabricate a code, or use a code for a different connection/line/version.

The signed code lasts ten minutes. An expired/tampered code or changed line requires a new preview and new confirmation. A client may also display its own destructive-action prompt; that is separate. The server verifies the code but cannot prove that a human said yes, so the skill must enforce the conversation step.

## Restore within seven days
list_deleted_quote_lines takes quoteId and returns eligible recent deletions with deletedLineId and restorable status. For a user-requested restore, restore_quote_line takes the returned deletedLineId. Restore requires the quote still be an inactive draft, an available line ID, valid referenced items and a recoverable deletion record. It restores the previous line identity/fields/order and issues a new updatedAt. The seven-day window is conditional recovery, not a guarantee; read the returned result.

For profit or margin, read get_quote profitAndLoss (admins only; never estimate it for others).

Never activate, confirm, send, or change quote status through this workflow. Never send messages or calendar invites.
