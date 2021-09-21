import discord
from discord.ext import commands

import config

import psutil
import platform
import sqlite3



db = sqlite3.connect('DB/stats.sqlite3')
cursor = db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS stats(
	name TEXT,
	count INT
)""")


class Info(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.Cog.listener()
	async def on_command(self, guild):
		if cursor.execute("SELECT name FROM stats WHERE name = 'commands'").fetchone() is None:
			cursor.execute("INSERT INTO stats VALUES ( 'commands', 0 )")
		cursor.execute("UPDATE stats SET count = count + 1 WHERE name = 'commands'")
		db.commit()


	#Info

	@commands.command()
	@commands.guild_only()
	async def info(self, ctx):

		guild_count = len(self.client.guilds)
		total_commands = len(self.client.commands)
		total_modules = len(self.client.cogs)
		python_version = platform.python_version()
		discord_version = discord.__version__

		

		emb = discord.Embed( title = f'{self.client.user.name}#{self.client.user.discriminator}', description = 'Информация о боте **BorryBot**', color = config.MAIN_COLOR )
		emb.add_field( name = 'Бота создал:', value = 'BORRY#9999', inline = True )
		emb.add_field( name = 'Серверов:', value = f"{guild_count}", inline = True )
		emb.add_field( name = 'Кол-во команд:', value = f'{total_commands}', inline = True )
		emb.add_field( name = 'Кол-во модулей:', value = f'{total_modules}', inline = True )
		emb.add_field( name = 'Префикс бота:', value = f'{config.PREFIX}', inline = True )
		emb.add_field( name = 'Версия python:', value = f'Python v{python_version}', inline = True )
		emb.add_field( name = 'Библотека бота:', value = f'Discord.py v{discord_version}', inline = True )
		emb.add_field( name = 'Версия бота:', value = config.VERSION , inline = True )
		emb.add_field( name = 'Язык бота:', value = 'Русский', inline = True )
		emb.add_field( name = 'Язык команд:', value = 'Английский', inline = True )
		emb.add_field( name = 'Пригласить бота на сервер:', value = '[Пригласить](https://discord.com/api/oauth2/authorize?client_id=862195560019001344&permissions=8&scope=bot)' )
		emb.add_field( name = 'Сервер поддержки:', value = '[Вступить](https://discord.gg/FJRj894gUn)' )
		emb.add_field( name = 'Полезные ссылки:', value = '[bots.server-discord.com](https://bots.server-discord.com/862195560019001344)\n[Boosty](https://boosty.to/borrybot)' )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#Ping

	@commands.command()
	@commands.guild_only()
	async def ping(self, ctx):
		emb = discord.Embed( title = f'Пинг', color = config.MAIN_COLOR )
		emb.add_field( name = 'Пинг бота:', value = f'{self.client.ws.latency*1000:.0f} мс' )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#Stats

	@commands.command()
	@commands.guild_only()
	async def stats(self, ctx):
		def bytes2human(number, typer=None):

			if typer == "system":
				symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')
			else:
				symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

			prefix = {}

			for i, s in enumerate(symbols):
				prefix[s] = 1 << (i + 1) * 10

			for s in reversed(symbols):
				if number >= prefix[s]:
					value = float(number) / prefix[s]
					return '%.1f%s' % (value, s)

			return f"{number}B"




		channels = []
		for guild in self.client.guilds:
			for channel in ctx.guild.channels:
				channels.append(channel)

		guild_count = len(self.client.guilds)
		all_members = len(set(self.client.get_all_members()))
		mem = psutil.virtual_memory()
		all_channels = len(channels)
		total_commands = len(self.client.commands)
		total_modules = len(self.client.cogs)

		emb = discord.Embed( title = "BorryBot в цифрах", color = config.MAIN_COLOR )
		emb.add_field( name = "Серверов:", value= f"`{guild_count}`", inline = True )
		#emb.add_field( name = "Участников:", value = f"`{all_members}`", inline = True )
		emb.add_field( name = 'Выполнено команд', value = f"""`{cursor.execute("SELECT count FROM stats WHERE name = 'commands'").fetchone()[0]}`""", inline = True)
		emb.add_field( name = 'Кол-во команд:', value = f'`{total_commands}`', inline = True )
		emb.add_field( name = 'Кол-во модулей:', value = f'`{total_modules}`', inline = True )
		emb.add_field( name = 'Всего каналов:', value = f'`{all_channels}`', inline = True )
		emb.add_field( name ='RAM:',value = f'`{mem.percent}% / {bytes2human(mem.total, "system")}`', inline=True )
		emb.add_field( name ='CPU:',value = f'`{psutil.cpu_percent()}%`', inline= True )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#Hosting

	@commands.command()
	@commands.guild_only()
	async def hosting(self, ctx):

		def bytes2human(number, typer=None):

			if typer == "system":
				symbols = ('KБ', 'МБ', 'ГБ', 'TБ', 'ПБ', 'ЭБ', 'ЗБ', 'ИБ')
			else:
				symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

			prefix = {}

			for i, s in enumerate(symbols):
				prefix[s] = 1 << (i + 1) * 10

			for s in reversed(symbols):
				if number >= prefix[s]:
					value = float(number) / prefix[s]
					return '%.1f%s' % (value, s)

			return f"{number}B"

		mem = psutil.virtual_memory()



		emb = discord.Embed( title = 'Информация о хостинге', color=config.MAIN_COLOR )
		emb.add_field( name = 'CPU:', value ='`1 vCPU`', inline=False )
		emb.add_field( name = 'RAM:',value =f'`{bytes2human(mem.total, "system")}`',inline=False )
		emb.add_field( name = 'OS:', value ='`Ubuntu 20.04 LTS`', inline=False )
		emb.add_field( name = 'SSD NVMe:', value ='`15 GB`', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#User

	@commands.command()
	@commands.guild_only()
	async def user(self, ctx, member:discord.Member=None):
		if member is None:
			if ctx.author.status == discord.Status.online:
				status = 'В сети'
			if ctx.author.status == discord.Status.idle:
				status = 'Неактивен'
			if ctx.author.status == discord.Status.dnd:
				status = 'Не беспокоить'
			if ctx.author.status == discord.Status.offline:
				status = 'Не в сети'
			emb = discord.Embed( title = f'Информация о {ctx.author.name}', color = config.MAIN_COLOR )
			emb.add_field( name = 'Имя пользователя:', value = f'{ctx.author.name}#{ctx.author.discriminator}', inline = False )
			emb.add_field( name = 'ID:', value = f'{ctx.author.id}', inline = False )
			emb.add_field( name = 'Пользователь зарегистрировался:', value = ctx.author.created_at.strftime('%d.%m.%Y %H:%M:%S'), inline = False )
			emb.add_field( name = 'Пользователь присоединился:', value = ctx.author.joined_at.strftime('%d.%m.%Y %H:%M:%S') )
			#emb.add_field( name = 'Статус:', value = status, inline = False )
			emb.set_thumbnail( url = ctx.author.avatar_url )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )
		else:
			if member.status == discord.Status.online:
				status = 'В сети'
			if member.status == discord.Status.idle:
				status = 'Неактивен'
			if member.status == discord.Status.dnd:
				status = 'Не беспокоить'
			if member.status == discord.Status.offline:
				status = 'Не в сети'
			emb = discord.Embed( title = f'Информация о {member.name}', color = config.MAIN_COLOR )
			emb.add_field( name = 'Имя пользователя:', value = f'{member.name}#{member.discriminator}', inline = False )
			emb.add_field( name = 'ID:', value = f'{member.id}', inline = False )
			emb.add_field( name = 'Пользователь зарегистрировался:', value = member.created_at.strftime('%d.%m.%Y %H:%M:%S'), inline = False )
			emb.add_field( name = 'Пользователь присоединился:', value = member.joined_at.strftime('%d.%m.%Y %H:%M:%S') )
			#emb.add_field( name = 'Статус:', value = status, inline = False )
			emb.set_thumbnail( url = member.avatar_url )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )


	#Server

	@commands.command()
	@commands.guild_only()
	async def server(self, ctx):
		if ctx.guild.verification_level == discord.VerificationLevel.none:
			verification_level = 'Отсутствует'
		if ctx.guild.verification_level == discord.VerificationLevel.low:
			verification_level = 'Низкий'
		if ctx.guild.verification_level == discord.VerificationLevel.medium:
			verification_level = 'Средний'
		if ctx.guild.verification_level == discord.VerificationLevel.high:
			verification_level = 'Высокий'
		if ctx.guild.verification_level == discord.VerificationLevel.extreme:
			verification_level = 'Очень выскоий'
		emb = discord.Embed( title = f'Информация о сервере {ctx.guild.name}', color = config.MAIN_COLOR )
		emb.add_field( name = 'ID:', value = f'{ctx.guild.id}', inline = False )
		#emb.add_field( name = 'Владелец:', value = f'{ctx.guild.owner}', inline = False )
		emb.add_field( name = 'Уровень верификации:' , value = verification_level, inline = False )
		#emb.add_field( name = 'Кол-во участников:', value = f'{len(ctx.guild.members)}', inline = False )
		#emb.add_field( name = 'В сети:', value = len({m.id for m in ctx.guild.members if m.status is not discord.Status.offline}), inline = False )
		emb.add_field( name = 'Каналы:', value = f'{len(ctx.guild.channels)} ({len(ctx.guild.text_channels)} Текстовых | {len(ctx.guild.voice_channels)} Голосовых) ', inline = False )
		emb.add_field( name = 'Кол-во ролей:', value = f'{len(ctx.guild.roles)}', inline = False )
		emb.add_field( name = 'Регион сервера:', value = ctx.guild.region, inline = False )
		emb.set_thumbnail( url = ctx.guild.icon_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


def setup(client):
	client.add_cog(Info(client))
	print('[Cog] Info загружен!')