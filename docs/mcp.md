# RO App MCP Server

RO App hosts a remote [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server that lets AI tools such
as Cursor, Claude Desktop, Claude Code and Codex interact with the RO App API and its documentation. It provides:

- **Direct API access** to RO App functionality
- **Documentation search**
- **Real-time data** from your RO App account
- **Code generation** assistance for RO App integrations

**Server URL:** `https://roapp.readme.io/mcp`

Authenticate with your RO App API key (from [Settings > API](https://web.roapp.io/settings/api)) via the
`Authorization: Bearer <API_KEY>` header, or however headers are configured in your MCP client.

## Configure Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "roapp": {
      "url": "https://roapp.readme.io/mcp",
      "headers": {
        "authorization": "Bearer YOUR_ROAPP_API_KEY"
      }
    }
  }
}
```

## Configure Claude Desktop

Add to the Claude Desktop config file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "roapp": {
      "url": "https://roapp.readme.io/mcp",
      "headers": {
        "authorization": "Bearer YOUR_ROAPP_API_KEY"
      }
    }
  }
}
```

## Configure Claude Code

```bash
claude mcp add --transport http roapp https://roapp.readme.io/mcp \
  --header "Authorization: Bearer $ROAPP_API_KEY"
```

## Configure Codex

Add to `~/.codex/config.toml`:

```toml
[mcp_servers.roapp]
url = "https://roapp.readme.io/mcp"
http_headers = { Authorization = "Bearer YOUR_ROAPP_API_KEY" }
```

## Test the setup

1. Open your AI editor and start a new chat.
2. Ask about RO App, for example:
   - "How do I get work orders from the previous month?"
   - "Show me Python code that calculates the average value of sales over the last 30 days."

The assistant should now have access to your RO App account data and documentation through the MCP server.
