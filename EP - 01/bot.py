import json
import discord
from discord.ext import commands

with open("settings.json", "r") as f:
    settings = json.load(f)
TOKEN = settings["bot_token"]

bot = commands.Bot(command_prefix="t!")


@bot.event
async def on_ready():
    print(f"Logged In Successfully\nLogged In As: {bot.user}\nLatency: {round(bot.latency*1000)}ms")

@bot.event
async def on_message(message):
    if message.content.lower() == "hi":
        await message.channel.send("Hello!")
    await bot.process_commands(message)

@bot.command(aliases=["latency"])
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")


bot.run(TOKEN)