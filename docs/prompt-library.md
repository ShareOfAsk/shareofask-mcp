# Prompt library

Copy a prompt, replace bracketed text and choose the workspace before requesting analysis. These prompts use existing stored data. Your assistant's written analysis is separate from the original measurements.

## First connection

```text
Use ShareOfAsk to list my accessible workspaces. Ask me to choose one if there
is more than one match. Show the available saved measurement dates and tell me
what you can read with this connection. Do not change anything.
```

## Visibility and competition

```text
Show AI Presence for [workspace] using the latest available saved data. Explain
the metric, dates, denominator and partial-data limitations. Then show the
available competitor comparison without mixing metrics with different scopes.
```

## Compare two saved measurements

```text
List saved measurements for [workspace] so I can choose a baseline and target.
Compare the two complete measurements. Flag changed questions or models and
keep this separate from provider/model-filtered trends. Do not run a new check.
```

## Inspect an original answer

```text
Open the full original answer behind this result, with the original question,
model, measurement date and available citations. Keep the original text intact
and put any interpretation outside it.
```

## Explore a source gap

```text
In [workspace], show three answers mentioning a configured competitor while
omitting our tracked brand. State dates and filters. Let me inspect the cited
sources; do not treat those citations as proof of why the model chose a brand.
```

## Open one recommendation

```text
Show the existing shared action plan for [workspace] so I can choose an action.
Then open only that recommendation, with its saved status, priority, steps and
available evidence. Do not change its status.
```

## Review tracked questions

```text
Show current tracked questions for [workspace], including their themes and
tags. Help me choose one and inspect its saved history. Suggest improvements
here without saving edits. Keep historical answers tied to their original questions.
```

## Prepare a change for review

```text
For the selected existing question, propose revised wording and tags in this
conversation. Show the current and proposed versions side by side. Do not save
the change. Explain how a later edit could affect measurement comparability.
```

To actually change a question or action status, first review [permissions and write behavior](permissions.md). The public prompts above do not grant write access. If a write result is uncertain, follow [troubleshooting](troubleshooting.md) rather than submitting a new operation blindly.

For complete workflows, see [agencies](playbooks/agencies.md), [marketing teams](playbooks/marketing-teams.md) and [content/SEO](playbooks/content-seo.md).
