import discord

from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        ping_embed = discord.Embed(
            title="Latency", description="Latency in ms", color=discord.Color.green()
        )
        ping_embed.add_field(
            name=f"{self.bot.user}'s Latency",
            value=f"{self.bot.latency * 1000}ms",
            inline=False,
        )
        ping_embed.set_footer(
            text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar
        )
        print("hi")
        await ctx.send(embed=ping_embed)

    @commands.command()
    async def hi(self, ctx):
        print("hi")
        await ctx.send(f"Hello {ctx.author.name}")

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        #    async def user_info(self, ctx):

        user_embed = discord.Embed(
            title=f"{member.name} Infos", color=discord.Color.purple()
        )

        user_embed.add_field(name="Nick", value=f"\n{member.nick}")

        user_embed.add_field(name="Status", value=f"\n{member.status}", inline=False)

        user_embed.add_field(name="Role", value=f"{member.top_role}", inline=False)

        user_embed.add_field(
            name="Join time", value=f"{member.joined_at.strftime('%d/%m/%Y')}"
        )

        user_embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=user_embed)


async def setup(bot):
    await bot.add_cog(Basic(bot))
