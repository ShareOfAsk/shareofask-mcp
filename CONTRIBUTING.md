# Contributing

Help make connecting and using ShareOfAsk easier. We welcome clearer setup instructions, corrections, accessible illustration descriptions and practical workflows grounded in existing capabilities.

## Before opening a change

1. Check the [getting-started guide](docs/getting-started.md) and [tool reference](reference/tools.md).
2. Keep instructions in US English and use fictional workspace names and data.
3. For client setup changes, link the vendor's current official documentation and state when you checked it. Distinguish a documented setup path from a connection you personally tested.
4. For a new recipe, include the audience, task, copyable prompt, expected result and interpretation limits. Clearly distinguish conversation drafts from changes saved to ShareOfAsk.

Do not include access tokens, authorization codes, private workspace identifiers, client reports or screenshots containing account data. Report sensitive issues through the [private contact](SECURITY.md).

## Submit an improvement

Open an issue to describe the problem or send a pull request with the proposed change. For documentation updates, explain which user task becomes clearer. For a client-specific issue, include the client/version, date, setup path and a redacted error message.

This repository documents a hosted service. Product runtime changes, new tools and backend fixes are handled separately; opening a documentation PR does not change the live service.

## Licensing your contribution

By submitting a contribution, you agree to license it under the license that applies to that material: [CC BY 4.0](LICENSE) for documentation, playbooks, natural-language prompts and published illustrations; [MIT](LICENSE-CODE) for scripts, configuration and code examples. See [LICENSING.md](LICENSING.md) for the scope and attribution guidance.

Only submit material you have the right to contribute under those terms. Identify any third-party material and its license, preserve required credits and notices, and explain any exceptions in your pull request. Do not assume a trademark or a private source file is covered by the repository licenses.

## Validate your changes

From the repository root, run:

```sh
python3 scripts/check-docs.py
```

This checks local links, heading anchors and illustration files. Review external links and copyable prompts manually. If you change an illustration, keep the matching alt text and the [asset inventory](assets/README.md) up to date.

[Back to README](README.md)
