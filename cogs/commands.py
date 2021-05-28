=import random
import discord
from discord.ext import commands


# Author: Noah Funderburgh
# Date: 10/8/2020
# Description:
# Todo: Comment descriptions about each functions purpose, as well as parameters and return values.

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.command()
    async def helps(self, ctx):
        embed = discord.Embed(
            title="Hey Discord Command List",
        )
        embed.add_field(name=":musical_note: Music", value="`.helpMusic`", inline=True)
        embed.add_field(name=":tools: Utility", value="`.helpUtility`", inline=True)
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
