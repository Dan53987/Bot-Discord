import discord

from discord.ext import commands
import os
import asyncio

# client objet
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
# check if the bot is online
async def on_ready():
    print("Bot is ready")


with open("token.txt", "r") as f:
    token = f.read()


# -
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"Errore: {error}")
    raise error


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f"Loading {filename}")
            await bot.load_extension(f"cogs.{filename[:-3]}")  # [:-3]


async def main():
    async with bot:
        await load()
        await bot.start(token)


asyncio.run(main())
# bot.run(token)
