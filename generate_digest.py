import os
from anthropic import Anthropic

api_key = os.environ.get('CLAUDE_API_KEY')
if not api_key:
    raise ValueError("CLAUDE_API_KEY environment variable not set")

client = Anthropic(api_key=api_key)
industry = "financial services"
region = "US"
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""Search for the latest regulatory developments in {industry} for {region} this past week.
Summarize:
1. What changed
2. Who it affects
3. What action the client should take
Keep it concise and actionable."""
        }
    ]
)
digest = message.content[0].text
print(digest)
