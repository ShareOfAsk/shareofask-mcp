# Use ShareOfAsk in Codex

Connect Codex directly to the hosted MCP endpoint. No local ShareOfAsk server or SDK is required.

## Add the server and sign in

Add this entry to your Codex configuration (`~/.codex/config.toml`), keeping any existing configuration:

```toml
[mcp_servers.shareofask]
url = "https://api.shareofask.com/mcp"
```

Then sign in with explicit read permissions:

```sh
codex mcp login shareofask --oauth-client-registration dcr --scopes workspaces:read,competitors:read,questions:read,metrics:read,mentions:read,responses:read,sources:read,recommendations:read
```

Complete the ShareOfAsk consent screen in your browser. Choose one organization, select workspace access, and approve the requested read permissions. Use `codex mcp list` to inspect configured servers and `/mcp` inside the terminal interface to inspect active connections.

OpenAI documents URL configuration, OAuth scopes, and the DCR option in [Model Context Protocol](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). Instructions checked November 2, 2026.

## First task

> Use ShareOfAsk to list my accessible workspaces. For the workspace I choose, read its methodology and existing snapshots, then prepare a visibility review with supporting stored responses and citation URLs. Include coverage limitations and keep missing values distinct from zero.

## Optional write access

To allow changes, start a new OAuth authorization requesting the read scopes above plus either or both of:

- `questions:write`: edit an existing question's text, existing theme, or tags.
- `recommendation-status:write`: change a shared action to open, done, or dismissed.

Enable the corresponding options on ShareOfAsk's consent screen and reload the connection's tool catalog. Read [Permissions](../permissions.md) first: these scopes allow authorized changes through chat tools as well as compatible embedded views. A separate confirmation for every operation is not required by ShareOfAsk; Codex may apply its own tool approval settings.

## Verified scope

OAuth and all 14 read tools were exercised with Codex 0.153.4 on September 12, 2026. This is a historical data-tool check, not current Codex visual-view verification. In that tested version, a URL-only entry worked; adding `oauth_resource` caused duplicate resource parameters. Keep the minimal configuration above.

[Client compatibility](compatibility.md) · [Getting started](../getting-started.md) · [Troubleshooting](../troubleshooting.md)
