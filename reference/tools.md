# Tool reference

This reference describes the hosted ShareOfAsk MCP interface reviewed on **November 2, 2026**: **14 read tools, 2 optional write tools, and 5 read-only view launchers**. A separate context tool is available only to embedded apps. The server advertises tools according to the connection's granted scopes; calls that access workspace data also check current workspace, role, and product access.

Endpoint: `https://api.shareofask.com/mcp`. Connect using OAuth with dynamic client registration (DCR). See [Getting started](../docs/getting-started.md), [Permissions](../docs/permissions.md), and [Client compatibility](../docs/clients/compatibility.md).

## Shared conventions

| Argument | Type and meaning |
| --- | --- |
| `workspaceId` | Required for every tool below except `list_workspaces` and `get_methodology`; string of 1–36 characters obtained from `list_workspaces`. |
| `limit`, `cursor` | Optional cursor pagination for tools that list them. `limit` is an integer from 1–100, except Sources tools, which allow 1–500. `cursor` is an opaque string returned by the same tool with the same filters. |
| `provider`, `targetModel` | Optional provider and model strings where listed. Use identifiers from the workspace or returned measurement data. |
| `snapshotId` | Optional identifier of an existing organic measurement where listed. It never starts a new measurement. |
| `questionId`, `rootQuestionId` | Question identifiers from returned data; strings of 1–36 characters. |
| `responseId` | Positive integer identifying a stored organic measurement response. |

General filter strings are trimmed and limited to 1–512 characters unless specified otherwise. Cursor strings allow 1–2,048 characters. Unrecognized input fields are rejected.

Results are available as structured content and a text JSON fallback with an outer `{ data, meta }` envelope. Outer metadata identifies ShareOfAsk, retrieval time, and the workspace where applicable. Domain data, pagination, and domain-specific metadata are inside `data`; do not assume every tool has the same inner shape.

For cursor-paginated lists, continue using `nextCursor` while `hasMore` is true. Mentions use `page`/`pageSize` instead. Do not report a page length as a population total. Reads respect the current history window and preserve incomplete or unavailable data. [Data and metrics](../docs/data-and-metrics.md) explains the interpretation rules.

## Read tools

### `list_workspaces`

**Scope:** `workspaces:read`\
**Optional:** `limit`, `cursor`

Lists currently accessible workspaces covered by the connection. Metadata distinguishes selected workspaces from all current and future workspaces in one organization. Follow all pages; start again without a cursor to discover newly added workspaces. The list is current access, not a transactional snapshot of the organization.

### `get_workspace`

**Scope:** `workspaces:read`\
**Required:** `workspaceId`

Reads workspace and brand context, existing themes, and configured models. Use this context to interpret results and select a valid existing theme before editing a question.

### `get_methodology`

**Scope:** `workspaces:read`\
**Arguments:** none; pass `{}`

Reads metric definitions and units, measurement methodology, neutral-question guidance, history limits, citation limitations, and pagination guidance. It does not run AI or measurements.

### `list_competitors`

**Scope:** `competitors:read`\
**Required:** `workspaceId`\
**Optional:** `limit`, `cursor`, `snapshotId`

Returns current configured competitors separately from brands observed in an existing snapshot. The observed population has one row per `brandKey`; `totalObservedCount` counts unique observed keys, not configured competitors.

Observed brands include `website` as a URL or `null`, using the Competitor Brand Discovery view's default 90-day window. This is not a citation-domain field. Main-brand and tracked-competitor aliases can resolve to their canonical website; discovered-brand aliases are not merged. `configured[].website` remains the configured competitor website.

### `list_questions`

**Scope:** `questions:read`\
**Required:** `workspaceId`\
**Optional:** `limit`, `cursor`, `includeHistory` (boolean), `rootQuestionId`

Reads current questions and revisions. Set `includeHistory: true` to include retained immutable content versions; use `rootQuestionId` to follow a question's lineage. Read the current `revision` before an edit. A content version and an edit revision serve different purposes: metadata changes can change the revision without creating a new content version.

### `list_snapshots`

**Scope:** `metrics:read`\
**Required:** `workspaceId`\
**Optional:** `limit`, `cursor`, `status`

`status` accepts `pending`, `running`, `succeeded`, or `failed`. Lists existing organic measurements within the available history window. Recommendation research is excluded. No measurement is started.

### `get_metrics`

**Scope:** `metrics:read`\
**Required:** `workspaceId`

Choose one input mode:

| Mode | Optional or required arguments |
| --- | --- |
| Time series | Optional `timeRange`: `1m`, `3m`, `6m`, or `12m` (default `3m`); optional `provider`, `targetModel`. |
| Whole-snapshot comparison | Both `baseSnapshotId` and `targetSnapshotId` are required together. Do not include `timeRange`, `provider`, or `targetModel`. |

Returns stored visibility metrics or a comparison of two entire snapshots. Comparison metadata flags changed question/model cohorts; an unavailable cohort flag is not confirmation of comparability. Preserve returned units and missing values.

`mainBrandMetrics.mentionsWithOwnDomainCitation` and `mentionsWithoutOwnDomainCitation` split main-brand mention responses by whether their stored citations include the workspace website or a subdomain. They do not change existing totals or establish why the brand was mentioned.

### `list_mentions`

**Scope:** `mentions:read`\
**Required:** `workspaceId`

| Optional argument | Accepted values |
| --- | --- |
| `provider`, `targetModel`, `questionId`, `snapshotId`, `brandKey` | Identifiers/filter strings |
| `page` | Integer 1–100,000 |
| `pageSize` | Integer 1–100 |
| `mentionType` | `primary_recommendation`, `recommendation`, `alternative`, `comparison`, `passing`, `dismissal` |
| `sentiment` | `positive`, `negative`, `neutral` |
| `search` | Text filter |
| `dateRange` | `7d`, `30d`, `90d`, `all` |
| `sortBy` | `date`, `sentiment`, `mentionType` |
| `sortOrder` | `asc`, `desc` |

Returns paginated mentions, supporting context, a summary, and pagination metadata. With `snapshotId` and no `dateRange`, it reads that snapshot without an extra recent-period filter; the history entitlement still applies.

Each mention includes `brandKey`, `brandName`, and `website` (URL or `null`, from the same discovery view described for `list_competitors`). `hasOwnDomainCitation` describes the mention's response. The summary's with/without-own-domain counts split the filtered mention count and do not alter `totalMentions`.

### `list_responses`

**Scope:** `responses:read`\
**Required:** `workspaceId`\
**Optional:** `limit`, `cursor`, `provider`, `targetModel`, `snapshotId`, `questionId`, `from`, `to`, `countryCode`, `languageCode`, `ok`

`from` and `to` are ISO date-time strings with a UTC offset or `Z`; `ok` is a boolean. Reads stored organic model responses and their original-question provenance. It returns full saved answer text, not shortened excerpts. Follow pagination for all matches. Recommendation research responses are excluded.

### `get_response`

**Scope:** `responses:read`\
**Required:** `workspaceId`, `responseId`

Reads one complete stored organic response and original-question provenance. `queryTextSource`, `queryTextCompleteness`, and any `queryTextLimitation` describe the question's history. `textTruncated: false` describes the model answer, not a guarantee that the historical question could be fully recovered.

### Sources filters

`list_sources` and `list_source_domains` share these optional inputs in addition to required `workspaceId`:

| Argument | Accepted values |
| --- | --- |
| `limit`, `cursor` | Sources cursor pagination; `limit` 1–500 |
| `provider`, `targetModel`, `snapshotId`, `questionId`, `domain` | Filter strings/identifiers |
| `timeRange` | `30d`, `90d`, `all` |
| `brandKey` | Citations from responses mentioning this brand |
| `brandRole` | `main`, `competitor`, `discovered` |
| `gapForBrandKey` | Citations from responses where a configured competitor is mentioned and this chosen brand is absent |
| `origin` | `provider_sdk`, `inline_text` |
| `includeTotal` | Boolean requesting total metadata |
| `includeMentionedBrands` | Boolean; `list_sources` can include brands mentioned in the response. It is accepted by the domain tool's shared schema but does not add brand lists to domain rows. |

Brand filters operate on mentions in the **response**, not verified content of the cited webpage. The citation and domain lists are independently paginated; their cursors are not interchangeable.

### `list_sources`

**Scope:** `sources:read`\
**Required:** `workspaceId`\
**Optional:** the [Sources filters](#sources-filters)

Reads stored citation URLs and metadata, including domain, recorded title when available, response/snapshot references, and citation origin. It does not retrieve full webpages or establish brand-specific attribution for each source.

### `list_source_domains`

**Scope:** `sources:read`\
**Required:** `workspaceId`\
**Optional:** the [Sources filters](#sources-filters), plus `search` (2–253 characters)

Reads domains with citation counts, distinct-response counts, and saved category/classification status. Categories may be absent and are cached AI classifications. This tool does not fetch or classify domains.

### `get_response_sources`

**Scope:** `sources:read`\
**Required:** `workspaceId`, `responseId`\
**Optional:** `limit` (1–500), `cursor`, `snapshotId`

Reads a page of stored citations for one authorized organic response. Continue through all pages to obtain all available citations. If supplied, `snapshotId` must match the response's measurement. Recommendation research is excluded.

### `get_recommendations`

**Scope:** `recommendations:read`\
**Required:** `workspaceId`\
**Optional:** `limit`, `cursor`, `view`

| `view` | Result |
| --- | --- |
| `runs` (default) | Existing historical recommendation analyses within the available history |
| `actions` | The current shared action plan with stable `actionId` and `version` |

Use `actions` before changing a shared status or opening a selected action panel. Historical private item statuses are not shared team decisions. Preserve research/source coverage and result-completeness metadata. This tool does not generate new recommendations.

## Optional write tools

These tools require separate consent, current edit access, and the current record version. They can be invoked by an authorized assistant directly as well as from a compatible embedded view. ShareOfAsk does not require a fresh confirmation for every call. See [Permissions](../docs/permissions.md).

Both require `operationId`: a string of 8–128 characters using letters, digits, `.`, `_`, `:`, or `-`. Use a new ID for a new operation; reuse it only for an identical retry. A retry returns the stored result without repeating the change. A different payload with the same ID conflicts. Neither tool starts a measurement.

### `update_question`

**Scope:** `questions:write`

| Required argument | Meaning |
| --- | --- |
| `workspaceId` | Authorized workspace |
| `questionId` | Current question ID from `list_questions` |
| `expectedRevision` | Current 64-character lowercase hexadecimal `revision` from that read |
| `operationId` | Unique operation identifier |
| `changes` | Object containing at least one supported change below |

Supported `changes` fields:

- `prompt`: nonempty text, up to 20,000 characters.
- `theme`: name of an existing theme, up to 255 characters.
- `tags`: up to 100 nonempty strings, each up to 255 characters.

A prompt edit preserves question history and may return a new current question ID. Use the returned ID and revision for subsequent work. Identical values do not create a new content version. Changes affect future scheduled measurements, not historical or already queued measurement questions. Questions should remain neutral.

### `update_recommendation_status`

**Scope:** `recommendation-status:write`; current recommendation-read access is also required.

| Required argument | Meaning |
| --- | --- |
| `workspaceId` | Authorized workspace |
| `actionId` | UUID from `get_recommendations` with `view: "actions"` |
| `expectedVersion` | Current positive integer `version` from that read |
| `operationId` | Unique operation identifier |
| `status` | `open`, `done`, or `dismissed` |

Optional fields:

- `reasonCode`: `already_done`, `not_relevant`, `incorrect_assumption`, `not_possible`, `budget`, `later`, `duplicate`, or `other`.
- `comment`: up to 4,000 characters.
- `completionUrl`: HTTP or HTTPS URL without embedded credentials, up to 2,048 characters.
- `revisitAt`: ISO date-time with a UTC offset or `Z`.

Dismissal requires a reason or nonempty comment. When `status` is `dismissed`, reason `other` requires a comment and `later` requires a future `revisitAt`. A dismissal with `already_done` is stored as `done`. Reopening clears the saved reason, comment, completion URL, and revisit date. These changes affect the shared team plan.

## Embedded view launchers

Launchers read existing data and open a view when the host supports it. They do not write or start measurements. The view may offer the two optional writes if separately authorized. Opening a view does not expand the connection's access.

| Tool | Required scope | Inherits arguments from | Additional optional focus |
| --- | --- | --- | --- |
| `show_visibility` | `metrics:read` | `get_metrics` | None |
| `show_responses` | `responses:read` | `list_responses` | `responseId` |
| `show_sources` | `sources:read` | `list_sources` | `responseId` |
| `show_action_plan` | `recommendations:read` | `get_recommendations`, but `view` accepts only `actions` | `actionId` (UUID) |
| `show_questions` | `questions:read` | `list_questions` | `questionId` |

Each also accepts optional `presentation`, an object with a `section` from this table:

| View | Allowed `presentation.section` |
| --- | --- |
| Visibility | `overview`, `trend`, `brands`, `models`, `comparison`, `evidence` |
| Answers | `list`, `answer`, `citations` |
| Sources | `overview`, `domains`, `citations`, `gaps` |
| Action Plan | `overview`, `steps`, `evidence`, `explanation` |
| Questions | `list`, `details`, `history` |

Visibility also accepts `presentation.metric`: `considerationShare` (AI Presence), `shareOfVoice` (Competitive Share of Voice), `questionCoverage` (Question Coverage), or `averagePosition` (Average First Position). Presentation selects a display focus; it is not a data filter. A record focus ID takes precedence. For Sources gaps, supply `gapForBrandKey`; without it the view prompts for a brand rather than labeling unfiltered citations as gaps.

To open separate action panels, first retrieve stable IDs using `get_recommendations` with `view: "actions"`, then call `show_action_plan` once per selected `actionId`. Omitting the ID opens the paginated overview. A focused action or question is resolved independently of an overview cursor and returns only the selected record, or an empty selected result if none is found within the accessible data.

`show_sources` defaults `includeTotal` to `true` for its initial citation/domain lists; an explicit `false` is preserved. Regular Sources read tools keep their own defaults. `show_sources` does not accept the domain tool's `search` argument.

Launcher results preserve the outer `{ data, meta }` envelope. Their `data` contains `contractVersion`, `view`, `workspace`, `filters`, optional `presentation`, `capabilities`, and `initialData`. `initialData` is keyed by underlying tool name. The text JSON fallback remains available when the host does not render the view.

### App-only context: `get_app_context`

**Required:** `workspaceId`, `view`\
**Allowed `view`:** `visibility`, `responses`, `sources`, `action_plan`, `questions`

This is an app-only tool, not a normal assistant-facing analysis tool. It refreshes workspace context and current capabilities: `readTools`, `canEditQuestions`, and `canUpdateActionStatus`. It does not return credentials or change data. Every subsequent read or write checks access again.

## Scope boundaries

There is no tool to start a measurement, generate a recommendation run, create/delete questions, change question status or language, change schedules, add competitors, manage billing/users/public links, or call an arbitrary ShareOfAsk API endpoint. The assistant may draft an interpretation or proposal from existing evidence, but it should not claim a new ShareOfAsk measurement or generated run occurred.

[Back to the integration hub](../README.md) · [Data and metrics](../docs/data-and-metrics.md) · [Troubleshooting](../docs/troubleshooting.md)
