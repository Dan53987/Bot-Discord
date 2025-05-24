import discord

from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def ball(self, ctx):
        responses = [
            "Sì.",
            "No.",
            "Forse.",
            "Non lo so.",
            "Certo che sì.",
            "Non penso proprio.",
            "Assolutamente.",
            "Non è una buona idea.",
        ]
        random.shuffle(responses)
        await ctx.send(f"🎱 {ctx.author.mention}, {responses[0]}")


async def setup(bot):
    await bot.add_cog(Fun(bot))
