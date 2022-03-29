# Selfbot-Bypass
- A simple way to read `message.content` after the "patch".
```py
@Bot.event
async def on_message(Content):
  async for Message in Content.channel.history(limit = 1):
    await Lust.process_commands(Message)
```
