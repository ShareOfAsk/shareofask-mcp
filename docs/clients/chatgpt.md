# Use ShareOfAsk in ChatGPT

Connect the hosted service as a custom connection named **ShareOfAsk**. These instructions do not depend on a public directory listing.

## Add ShareOfAsk

1. On ChatGPT web, open **Plugins**, choose **+**, then **Add custom MCP server**.
2. Name it **ShareOfAsk** and enter `https://api.shareofask.com/mcp` as the server URL.
3. Choose **OAuth**. Use **DCR** if a client-registration choice is shown; ShareOfAsk registers a public client dynamically, so you do not supply a client secret.
4. Complete ChatGPT's creation flow and install the resulting custom plugin.
5. Sign in to ShareOfAsk when prompted, select an organization and workspace access, and review the permissions. Start with read access unless you want the optional edits described in [Permissions](../permissions.md).
6. In a conversation, type **@** and select your ShareOfAsk connection.

The current ChatGPT interface and availability depend on workspace permissions and security settings. OpenAI documents the setup and the app details page used to refresh tools in [Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server). Instructions checked November 2, 2026.

## First conversation

> Use ShareOfAsk to list my accessible workspaces. After I choose one, open its Visibility view and explain the results using the stored data and ShareOfAsk's metric definitions.

You can also ask for **Answers**, **Sources**, **Action Plan**, or **Questions**. For a focused review:

> Open the existing shared Action Plan. Show each action I select in its own panel, including its explanation and supporting evidence. Do not change any statuses.

## If a view or tool is missing

Some first openings have required ChatGPT's **Try again**. If a view stays unavailable, ask for the same information through the data tools. After granting additional scopes, refresh the connection's tools in its details page; signing in alone may leave an older tool list cached.

All five views were checked in a ChatGPT custom-connection QA session on November 2, 2026. That session had CSP enforcement disabled, so it does not establish rendering under standard strict CSP. See [Compatibility](compatibility.md) for the precise verification scope.

[Getting started](../getting-started.md) · [Troubleshooting](../troubleshooting.md)
