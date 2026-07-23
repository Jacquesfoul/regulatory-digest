import os
from anthropic import Anthropic

api_key = os.environ.get('CLAUDE_API_KEY')
if not api_key:
    raise ValueError("CLAUDE_API_KEY environment variable not set")

client = Anthropic(api_key=api_key)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[
        {
            "type": "web_search",
            "name": "web_search"
        }
    ],
    messages=[
        {
            "role": "user",
            "content": """Search for the latest news from the past week about France's presidential election campaigns. 
Focus on top news sources only (Reuters, AFP, BBC, France24, Le Monde, etc.).
Summarize:
1. Key campaign developments
2. Candidate positions and statements
3. Polling trends if available
4. Expected next steps

Keep it concise and objective."""
        }
    ]
)

digest = message.content[0].text
print(digest)
