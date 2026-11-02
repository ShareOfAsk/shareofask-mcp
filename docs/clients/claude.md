# Use ShareOfAsk in Claude

**ShareOfAsk has not yet completed an end-to-end Claude verification.** The setup below follows Claude's current remote connector instructions and ShareOfAsk's OAuth requirements. Treat it as a setup path to try, not a verified compatibility claim.

## Add a custom web connector

1. Open **Customize → Connectors**, then **+ Add → Add custom connector**. In managed organizations, an authorized administrator first adds it through **Organization settings → Connectors → Add → Custom → Web**.
2. Enter **ShareOfAsk** and `https://api.shareofask.com/mcp`.
3. Review the detected OAuth authentication. Choose **Sign in now** and **Register automatically** for the OAuth client. ShareOfAsk supports DCR; Claude's published client identity uses a different registration method that ShareOfAsk does not currently support.
4. Finish adding the connector. Sign in to ShareOfAsk, choose one organization and workspace access, and review read permissions. Do not add a static API key or request header.
5. Enable ShareOfAsk for the conversation through **+ → Connectors**.

Interface availability and administrator permissions depend on your Claude account. See Anthropic's [custom remote connector guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp). Instructions checked November 2, 2026.

## Start with a read

> Use ShareOfAsk to list the workspaces this connection can access. For the workspace I choose, retrieve existing visibility data and the stored model responses behind it. Do not change any data.

Begin with the data tools. Embedded views and write behavior have not been verified in Claude. If authentication fails, confirm that the OAuth client uses automatic registration (DCR), then see [Troubleshooting](../troubleshooting.md).

[Client compatibility](compatibility.md) · [Getting started](../getting-started.md) · [Permissions](../permissions.md)
