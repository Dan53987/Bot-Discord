import discord

from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(
        self, ctx, member: discord.Member, *, reason="Nessun motivo specificato."
    ):
        if not ctx.guild.me.guild_permissions.kick_members:
            await ctx.send("Non hai i permessiper effettuare questa azione.")
            return
        if member == ctx.author:
            await ctx.send("Non puoi kickare te stesso.")
            return
        if member == ctx.guild.me:
            await ctx.send("Non posso kickare me stesso.")
            return
        if ctx.author.top_role < member.top_role:
            await ctx.send(f"{ctx.author.mention} non puoi esspellere questo membro.")
            return
        else:
            await ctx.send(f"{member.mention} è stato kickato.")
            await member.send(reason)
            await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Sei stato bannato."):
        if member == ctx.author:
            await ctx.send("Non puoi bannare te stesso.")
            return
        if member == ctx.guild.me:
            await ctx.send("Non posso bannare me stesso.")
            return
        if ctx.author.top_role <= member.top_role:
            await ctx.send("Non puoi bannare questo membro.")
            return
        else:
            await ctx.send(f"{member.mention} è stato bannato.")
            await member.send(reason)
            await member.ban(reason=reason)

    # Non Funziona
    # @commands.command()
    # async def unban(self, ctx, *, user_tag=str):
    #     ban_list = ctx.guild.bans()
    #     nome = user_tag  # .split("#")
    #     print(nome)
    #     print(ban_list)
    #     # if ctx.author:
    #     #   await ctx.send("Non sei bannato.")
    #     #  return
    #     # if ctx.guild.me:
    #     #   await ctx.send("Non sono bannato.")
    #     #  return
    #     for banned in ban_list:
    #         user = banned.user
    #         print(user)
    #         if nome == user.name:  # or tag == user.discriminator:
    #             await ctx.guild.unban(user)
    #             await ctx.send(f"{user.mention} è stato sbannato.")
    #             return
    #


async def setup(bot):
    await bot.add_cog(Moderation(bot))
