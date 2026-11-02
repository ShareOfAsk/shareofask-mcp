# Read the evidence correctly

ShareOfAsk's MCP connection exposes **existing, stored measurement data**. It does not run a live model test when you ask a question. An assistant's interpretation is a new analysis of that evidence; label it separately from the recorded results and stored ShareOfAsk recommendations.

Ask the assistant to read `get_methodology` before preparing a report. Use the returned definitions, units, filters, and coverage. Do not introduce a new formula under an existing ShareOfAsk metric name.

## The main visibility metrics

| Metric | Meaning | Unit |
| --- | --- | --- |
| AI Presence (`considerationShare`, also called Consideration Share) | Responses mentioning the brand as a share of all eligible responses in the selected scope | Percent |
| Competitive Share of Voice (`shareOfVoice`) | Distinct responses mentioning the canonical brand as a share of all distinct canonical-brand/response pairs in the selected eligible observations | Percent |
| Question Coverage (`questionCoverage`) | Questions with a brand mention as a share of questions represented in the selected scope | Percent |
| Average First Position (`averagePosition`) | Mean of the available snapshot average recommendation positions; a lower value means an earlier position | Rank position |

AI Presence and Competitive Share of Voice use different denominators. One answer can mention multiple brands; raw mention counts and distinct response counts are also different. Do not substitute one for another. The technical field names above connect the public interface labels to tool results.

Keep a missing value as missing. A zero can be a valid observation, but a failed or unavailable observation is not zero. Missing positions are not zero. Where `sovFormulaVersion` differs between snapshots, ShareOfAsk returns unavailable changes for the affected Competitive Share of Voice and AI Presence trends instead of treating the formulas as comparable.

`keySignals` is a stored portrayal briefing with an availability status, not a visibility percentage. A missing briefing does not mean that the brand has no strengths or weaknesses.

## Make comparisons explicit

For a time series, `get_metrics` accepts `timeRange` and optional provider/model filters. For a comparison, it requires both `baseSnapshotId` and `targetSnapshotId` and compares the **whole snapshots**. You cannot combine comparison IDs with provider, model, or time-range filters.

Before describing a change, inspect dates, question versions, model identifiers, coverage, and comparison metadata. A different question set or model mix can change the result. If comparability cannot be assessed, say so. A metric change alone does not establish the effect of a campaign or content update.

## Stored answers and original questions

The response tools return stored organic measurement answers without silently shortening their text. They exclude recommendation research responses. Historical access is bounded by the workspace's current history entitlement.

The question attached to a historical response is not replaced with today's edited question. Check its provenance:

| Field | How to use it |
| --- | --- |
| `queryTextSource` | `snapshot_job` identifies a verified original snapshot job; `stored_response` uses the text saved with the answer; `unavailable` means no question text is available. |
| `queryTextCompleteness` | `complete`, `unknown`, or `unavailable`; preserve the distinction in evidence excerpts. |
| `queryTextLimitation` | Explains a limitation when completeness is unknown or text is unavailable. |

`unknown` does not prove that a question was truncated. It means the historical record does not establish completeness. Complete answer text does not guarantee complete original-question text.

## Sources, domains, and gaps

Sources are stored citation URLs and metadata. Their origin can be `provider_sdk` or `inline_text`. A citation record is not the full text of its webpage; these tools do not fetch pages, crawl websites, or run a fresh domain classification.

- A citation does **not** prove that the page caused a brand mention.
- A brand mentioned in an answer is not necessarily discussed by every source cited in that answer.
- Domain categories are optional saved AI classifications, not verified ground truth.
- No stored citations means none are available in the requested scope. It does not prove that the model used no sources.

A **source gap for a chosen brand** means the cited response mentions a configured competitor and does not mention the chosen brand. It is a response-level condition. It does not mean that the cited page itself omits the brand, that a publisher rejected it, or that obtaining a citation will guarantee a recommendation. Use `gapForBrandKey` for this analysis; selecting a visual Gaps section alone does not apply that filter.

Own-domain citation counts show whether a response includes at least one stored citation to the workspace website or its subdomain. In visibility metrics these counts split main-brand mention responses; in the mentions list they split filtered mention rows. They remain part of the existing totals and do not establish causation.

The `website` attached to an observed brand or mention is the URL used by ShareOfAsk's Competitor Brand Discovery view over its default 90-day window. It can be `null`; it is not a citation domain or necessarily the website recorded in that individual snapshot.

## Counts, pages, and completeness

Follow every `nextCursor` while `hasMore` is true before calling a result a complete list. A returned page's length is not the population total. Mentions use `page` and `pageSize` instead. Citation lists and domain lists have separate cursors; do not reuse one list's cursor for another.

Use authoritative total metadata when it is available. If you retrieve only part of a list, label it a sample or partial export. `dataState=complete` describes the available stored query result, not complete provider participation or complete citation capture.

Stored recommendations may be partial. Preserve `resultCompleteness`, `researchCompleteness`, `sourceCoverage`, and failure-count information rather than assuming that a completed run has complete evidence. The current shared action plan is current state; historical recommendation runs are a separate view.

## A report-ready request

> Prepare a visibility review from ShareOfAsk's existing data. State the workspace, dates, snapshots, models, and question coverage. Use returned metric definitions and units. Cite stored responses and source URLs for major findings. Separate observed changes, possible explanations, and proposed next steps. Preserve missing data, partial coverage, and comparison limitations.

[Tool reference](../reference/tools.md) · [Permissions](permissions.md) · [Getting started](getting-started.md)
