# Troubleshooting

Start by confirming the connection uses `https://api.shareofask.com/mcp`, OAuth, and dynamic client registration (DCR). The setup pages cover [ChatGPT](clients/chatgpt.md), [Codex](clients/codex.md), and [Claude](clients/claude.md).

## The connection cannot sign in

Use the assistant's reconnect or sign-in flow. ShareOfAsk requires its MCP OAuth authorization; a ShareOfAsk website session, application JWT, or API key is not a substitute.

If your client offers OAuth registration methods, use **DCR** or **Register automatically**. ShareOfAsk does not currently accept a client metadata URL (CIMD) as its registration method. Do not add your own client secret or a manually copied bearer token.

For Codex, start with the URL-only configuration and explicit login command in the [Codex guide](clients/codex.md). In the historically tested version, an added `oauth_resource` setting duplicated the resource parameter and caused sign-in to fail.

## A workspace is missing

Ask the assistant to start a fresh `list_workspaces` request and follow all pages. Then check:

1. Is it in the organization selected for this connection?
2. Does your current ShareOfAsk account have access to it?
3. Did you authorize that workspace, or choose all current and future workspaces?

In selected-workspace mode, a new workspace is not added automatically. Start a new authorization to include it. A token refresh does not broaden access. Demo workspaces are not exposed.

## A view does not open

All five views have displayed data in ChatGPT QA, but some initial loads have required **Try again**. Retry once. If the view still fails, ask the assistant for the corresponding data:

| View | Data-tool fallback |
| --- | --- |
| Visibility | `get_metrics` |
| Answers | `list_responses`, then `get_response` |
| Sources | `list_sources` or `list_source_domains` |
| Action Plan | `get_recommendations` with `view: "actions"` |
| Questions | `list_questions` |

The latest ChatGPT QA used a custom connection with CSP enforcement disabled. It does not verify standard strict-CSP rendering. Keep your normal security settings and use the data fallback; see [Compatibility](clients/compatibility.md).

## I approved writes, but the assistant cannot edit

Both steps are required: the client requests the write scope and you enable it on ShareOfAsk's consent screen. Then refresh the connection's tools in the assistant; ChatGPT QA encountered a cached read-only tool catalog after authorization changed.

Your current role and product access must also permit the action. A Viewer cannot write. Updating recommendation status additionally requires access to read recommendations. See [Permissions](permissions.md).

## An edit reports a conflict or times out

A revision or version conflict means the record changed since it was read. Read it again, inspect the difference, and decide whether the intended change still applies. Do not overwrite unseen changes automatically.

If the result of a write is uncertain, retry the **identical** operation with the same `operationId`. Do not generate a new ID for that retry. A different payload with a reused ID is rejected; a genuinely new operation needs a new ID and current revision or version.

## Results are empty, partial, or different from the website

Check the workspace, filters, measurement dates, history window, and pagination. Current configuration and the current action plan are different from historical measurements. Compare the same scope before comparing numbers.

- An explicit snapshot and a recent date filter can exclude each other. For mentions, omitting `dateRange` when supplying `snapshotId` avoids adding the default recent-period filter.
- Source totals, returned rows, and distinct responses are different counts.
- A source gap requires a chosen `gapForBrandKey`, a competitor mention, and no mention of the chosen brand in the response.
- Stored citations may be unavailable even when an answer exists.
- Recommendation research answers are excluded from the response and Sources tools.

Use [Data and metrics](data-and-metrics.md) to preserve these distinctions in a report.

## Common error responses

| Response | Next step |
| --- | --- |
| `401` authentication required | Reconnect or sign in; the connection may be expired or revoked. |
| `402` product access required | Check the organization's current ShareOfAsk product access. |
| `403` insufficient permission | Check the granted scope, current role, and feature access. |
| `404` record not found | Confirm the workspace and record are within the connection and available history. Inaccessible records can appear as not found. |
| `409` conflict | Re-read the current revision/version; check whether an operation ID was reused with different content. |
| `429` rate limited | Wait for the returned retry interval before trying again. |

For a reproducible issue, record the assistant and version, date, tool or view, error text, and whether it happens again after reconnecting. Redact tokens, authorization codes, customer data, and private URLs before posting a public issue.

[Getting started](getting-started.md) · [Tool reference](../reference/tools.md)
