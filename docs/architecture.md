# Thin hub and update boundaries
Canonical skill + per-client setup/packages → existing authenticated MCP → caller-permitted tools. There is no new backend here.

The shipped get_whats_new read tool returns serverVersion, changes, yourTools, permissionsYouCanAdd, howToEnable and tips. Changes accept since date or sinceVersion; without either they cover the last 30 days. A tool can be unavailable because permission is unticked or the role is ineligible. Discover it at session start; fall back to the dated bundled snapshot if absent.

Server-returned guidance can stay current without rewriting every bundled reference. Imported skills/packages still need versioned redistribution, and new tool metadata can require host refresh. Grant approval, role eligibility, client discovery and package updates are distinct. No instant/silent rollout is promised.

The portable package is skills-only: enable it alongside the existing working hosted ChatGPT connection. Do not replace the cloud/mobile connection with a desktop-only raw MCP declaration. Claude/Gemini native packages point to the same endpoint; no persistent credentials are bundled.

This public repository contains documentation/tool metadata and synthetic examples only. It does not contain CRM backend source, databases, live payloads, account grants or internal history.
