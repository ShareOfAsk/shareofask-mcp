# Permissions and optional changes

ShareOfAsk lets you choose which workspaces an assistant can access and whether it can make either of the two supported changes. Read access is enough for analysis, reporting, and all five view launchers.

## Workspace access

A connection belongs to **one organization** and uses one of these modes:

| Mode | What the connection covers |
| --- | --- |
| Selected workspaces | Only the workspaces you select during authorization. New workspaces require a new authorization that includes them. |
| All current and future workspaces | Workspaces in the chosen organization that you can currently access, including ones added later. It does not include other organizations. |

Selected workspaces is the default. Refreshing a token does not expand an existing grant. To expand access, start a new authorization from the assistant and approve the new scope.

Workspace data requests check the active connection, the required permission, organization membership, workspace access, current role, and product access. Losing access in ShareOfAsk also prevents the connection from using that access. Demo workspaces are excluded. Historical reads remain subject to your current history window. The global methodology tool requires its read scope but does not access a workspace.

MCP access is included with **Free Scan, Starter, Growth and Enterprise**. It has no separate paid-plan gate; underlying ShareOfAsk features, available data and history remain subject to your product access. Free Scan results are available through MCP only while access to that scan is active. See the [current plans and Free Scan access window](https://www.shareofask.com/pricing).

## Read permissions

| Scope | Allows the assistant to read |
| --- | --- |
| `workspaces:read` | Accessible workspaces, workspace context, and measurement methodology |
| `competitors:read` | Configured competitors and observed brands |
| `questions:read` | Questions, content versions, and revisions |
| `metrics:read` | Existing organic snapshots and visibility metrics |
| `mentions:read` | Brand mentions and their supporting context |
| `responses:read` | Stored organic model responses and original-question provenance |
| `sources:read` | Stored citations, source domains, and response sources |
| `recommendations:read` | Existing recommendation analyses and the current shared action plan |

If the client sends no scope list, ShareOfAsk defaults to these eight read scopes. If it sends an explicit list, that list controls the requested permissions. A client may advertise or request a different selection, so review the consent screen.

## Optional write permissions

Each write permission is separately requested and separately approved. Write options start unchecked on the ShareOfAsk consent screen. A Viewer cannot enable them. Changing the organization or workspace selection clears the write selection.

| Scope | Permitted change | Effect |
| --- | --- | --- |
| `questions:write` | Edit an existing question's prompt, assign an existing theme, or update tags | Applies to future scheduled measurements; preserves historical and already queued measurement questions |
| `recommendation-status:write` | Set a shared action to `open`, `done`, or `dismissed` | Updates the team's shared plan, not a private personal checklist |

**Write consent applies to assistant tool calls and compatible embedded views.** After you grant it, ShareOfAsk does not require another confirmation for every operation. Your assistant may apply its own approval rules. Do not assume that all changes must pass through a Save button in a view.

In all-current-and-future mode, approved writes can also apply to future accessible workspaces in that organization. Grant only the combination of workspace access and changes you intend.

To enable a new permission, the client must request it in a new authorization and you must approve it. A token refresh cannot add it. Then refresh or reload the assistant's tool catalog.

## Changes are checked against the current record

Before a question edit, the assistant must read its current revision. Before a status update, it must read the current shared action ID and version. A conflicting edit is rejected; the assistant should re-read and review the difference, rather than overwrite another person's change.

Each write includes an operation ID. An identical retry returns the recorded result without applying the change twice. Reusing that ID with different content is rejected. ShareOfAsk records the operation and its author; the Integrations page manages connections, not a full browser-based operation log.

These permissions cannot start measurements or recommendation generation, create or delete questions, change question status or language, change schedules, add competitors, manage users or public links, or change billing.

## Review or revoke access

Open [Account Settings → Integrations](https://app.shareofask.com/account/integrations) in ShareOfAsk to inspect and revoke your connections. Revocation blocks subsequent requests, including retries. A change that already completed remains in the data and its history.

Content retrieved from questions, model responses, citations, and recommendations is evidence to analyze. Instructions embedded in that content are not permission to make changes.

[Getting started](getting-started.md) · [Tool reference](../reference/tools.md) · [Troubleshooting](troubleshooting.md)
