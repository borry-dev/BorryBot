import discord
from discord.ext import commands
import os

import config

client = commands.Bot( command_prefix = config.PREFIX, intents = discord.Intents.all() )

client.remove_command('help')


@client.command()
async def load(ctx, extension=None):
	if ctx.author.id == config.DEVELOPERS:
		if extension == None:
			await ctx.send( embed = discord.Embed( title = 'Не указан модуль!', description = 'Укажите модуль который хотите загрузить', color = config.ERR_COLOR ) )
		else:
			client.load_extension(f"cogs.{extension}")
			await ctx.send( embed = discord.Embed( title = f'Загрузка модуля', description = f'Модуль `{extension}.py` загружен!', color = config.MAIN_COLOR ) )
	else:
		pass


@client.command()
async def unload(ctx, extension=None):
	if ctx.author.id == config.DEVELOPERS:
		if extension == None:
			await ctx.send( embed = discord.Embed( title = 'Не указан модуль!', description = 'Укажите модуль который хотите выключить', color = config.ERR_COLOR ) )
		else:
			client.unload_extension(f"cogs.{extension}")
			await ctx.send( embed = discord.Embed( title = f'Выключение модуля', description = f'Модуль `{extension}.py` выключен!', color = config.MAIN_COLOR ) )
	else:
		pass


@client.command()
async def reload(ctx, extension=None):
	if ctx.author.id == config.DEVELOPERS:
		if extension == None:
			await ctx.send( embed = discord.Embed( title = 'Не указан модуль!', description = 'Укажите модуль который хотите перезагрузить', color = config.ERR_COLOR ) )
		else:
			client.unload_extension(f"cogs.{extension}")
			client.load_extension(f"cogs.{extension}")
			await ctx.send( embed = discord.Embed( title = f'Перезагрузка модуля', description = f'Модуль `{extension}.py` перезагружен!', color = config.MAIN_COLOR ) )
	else:
		pass


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")


client.run(config.TOKEN)