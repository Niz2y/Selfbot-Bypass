# Selfbot-Bypass
- A simple way to read `message.content` after the patch.
```py
@Bot.event
async def on_message(Content):
  async for Message in Content.channel.history(limit = 1):
    await Bot.process_commands(Message)
```

# Example Code
- Found [here](https://github.com/Niz2y/Selfbot-Bypass/blob/main/Example.py).
```py
import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix = ".", self_bot = False)

@Bot.event
async def on_ready():
  print("Connected.")

@Bot.command()
async def test(ctx):
  await ctx.reply("Success.")

@Bot.event
async def on_message(Content):
  async for Message in Content.channel.history(limit = 1):
    await Bot.process_commands(Message)

Bot.run("Token", bot = False)
```
