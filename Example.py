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
