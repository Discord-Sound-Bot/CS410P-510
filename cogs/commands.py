import random
import discord
from discord.ext import commands


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('yourself'))
        print('Bot is ready.')

    @commands.command()
    async def helps(self, ctx):
        embed = discord.Embed(
            title="Step Sis Command List",
            # description="HI",
        )
        embed.add_field(name=":musical_note: Music", value="`.helpMusic`", inline=True)
        embed.add_field(name=":joy: Reddit", value="`.helpReddit`", inline=True)
        embed.add_field(name=":game_die: Games", value="`.helpGame`", inline=True)
        embed.add_field(name=":tools: Utility", value="`.helpUtility`", inline=True)
        embed.add_field(name=":fire: Admin", value="`.helpAdmin`", inline=True)
        embed.add_field(name=":video_game: RPG", value="`.helpRPG`", inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['helputility'])
    async def helpUtility(self, ctx):
        embed = discord.Embed(
            title=":tools: Utility Commands",
            description="`ping`,`8ball`",
            colour=discord.Colour.greyple()
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Your ping is {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Commands(client))
