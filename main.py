import os
from discord.ext import commands

# Author: Noah Funderburgh
# Date: 10/8/2020
# Description:
# Todo: Comment descriptions about each functions purpose, as well as parameters and return values.

client = commands.Bot(command_prefix='.')


# client.remove_command("help")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension {extension} has been reloaded')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used.")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODQ1MTIyMzYwNjAwNDI4NTk1.YKcXiA.pp3FOBDgxCyykMPnCh3p56JmIKQ")
