# Client compatibility

ShareOfAsk provides a hosted MCP endpoint at `https://api.shareofask.com/mcp`, using Streamable HTTP and OAuth with dynamic client registration (DCR). Data-tool compatibility and embedded-view compatibility are separate: a client may read the data without rendering the five interactive views.

Last reviewed: **November 2, 2026**.

| Client | What ShareOfAsk has verified | What remains unverified |
| --- | --- | --- |
| [ChatGPT](chatgpt.md) | All five views displayed data in a custom-connection QA session on November 2, 2026. Read and optional write flows were also exercised in earlier QA. | Some initial view loads required retry. The latest QA connection had CSP enforcement disabled; standard strict-CSP rendering and a public directory listing are not verified. |
| [Codex](codex.md) | OAuth and all 14 read tools with Codex 0.153.4 on September 12, 2026. | Current-client regression, embedded-view behavior, and write flows in Codex are not covered by that historical check. |
| [Claude](claude.md) | Setup guidance checked against current vendor documentation. | End-to-end ShareOfAsk connection, views, and writes; verification is deferred. |
| Other MCP clients | Server protocol tests cover MCP client generations using Streamable HTTP. | Each client's sign-in interface, permission behavior, and visual support need a separate check. |

No client row guarantees availability for every plan, organization, or client version. Your assistant's administration policies also control custom connections.

## Choose the right experience

- **For analysis in conversation:** use the 14 read tools. They provide existing ShareOfAsk data with provenance and pagination.
- **For interactive exploration:** ask a compatible host to open Visibility, Answers, Sources, Action Plan, or Questions. The view launchers are read-only; editing inside a view requires separate write permission.
- **For team updates:** grant only the optional write scopes you need. [Permissions](../permissions.md) describes their effects and checks.

If a visual view does not load, ask the assistant to retrieve the same information using the data tools. Do not disable host security settings as a troubleshooting step. [Troubleshooting](../troubleshooting.md) covers retries, stale tool catalogs, and sign-in issues.

[Getting started](../getting-started.md) · [Tool reference](../../reference/tools.md)
