import discord

from discord.ext import commands

# client objet
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
# check if the bot is online
async def on_ready():
    print("Bot is ready")


@bot.command(name="Hi")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")


@bot.command(aliases=["gn", "buonasera"])
async def goodnight(ctx):
    await ctx.send(f"goodnight {ctx.author.mention}")


# @bot.command()
# async def sendembed(ctx):
#     embeded_msg = discord.Embed(
#         title="Title of embed",
#         description="Description of embed",
#         color=discord.Color.green(),
#     )
#     embeded_msg.set_thumbnail(url="https://icanhazdadjoke.com")
#     embeded_msg.add_field(name="Dad joke", value="Value of field", inline=False)
#     embeded_msg.set_image(url=ctx.author.avatar)
#     embeded_msg.set_footer(text="Footer of embed", icon_url=ctx.author.avatar)
#     await ctx.send(embed=embeded_msg)


@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(
        title="Ping", description="Latency in ms", color=discord.Color.green()
    )
    ping_embed.add_field(
        name=f"{bot.user}'s latency(ms): ",
        value=f"{round(bot.latency * 1000)}ms.",
        inline=False,
    )
    ping_embed.set_footer(
        text=f"Requested by {ctx.author.name}.", icon_url=ctx.author.avatar
    )
    await ctx.send(embed=ping_embed)


with open("token.txt", "r") as f:
    token = f.read()
bot.run(token)
