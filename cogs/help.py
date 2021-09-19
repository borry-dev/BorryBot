import discord
from discord.ext import commands

import config


class Help(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.group()
	async def help(self, ctx):
		if ctx.invoked_subcommand == None:
			emb = discord.Embed( title = 'Команды', description = f'Для просмотра команд введите `{config.PREFIX}help [название модуля]`', color = config.MAIN_COLOR )
			emb.add_field( name = f'{config.PREFIX}help info', value = 'Информационные команды', inline = False )
			emb.add_field( name = f'{config.PREFIX}help moderation', value = 'Команды модерации', inline = False )
			emb.add_field( name = f'{config.PREFIX}help settings', value = 'Настройки сервера', inline = False )
			emb.add_field( name = f'{config.PREFIX}help support', value = 'Команды поддержки', inline = False )
			emb.add_field( name = f'{config.PREFIX}help fun', value = 'Развлекательные команды', inline = False )
			emb.add_field( name = f'{config.PREFIX}help premium', value = 'Премиум команды', inline = False )
			emb.add_field( name = f'{config.PREFIX}help utility', value = 'Утилиты', inline = False )
			emb.set_thumbnail( url = self.client.user.avatar_url )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )



	@help.command()
	async def info(self, ctx):
		emb = discord.Embed( title = 'Информационные команды', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}info', value = 'Узнать информацию о боте', inline = False )
		emb.add_field( name = f'{config.PREFIX}ping', value = 'Узнать пинг бота', inline = False )
		emb.add_field( name = f'{config.PREFIX}stats', value = 'Узнать статистику бота', inline = False )
		emb.add_field( name = f'{config.PREFIX}hosting', value = 'Узнать информацию о хостинге', inline = False )
		emb.add_field( name = f'{config.PREFIX}user <пинг пользователя>', value = 'Узнать информацию о пользователе', inline = False )
		emb.add_field( name = f'{config.PREFIX}server', value = 'Узнать ниформацию о сервере', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	@help.command()
	async def moderation(self, ctx):
		emb = discord.Embed( title = 'Команды модерации', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}ban <пинг нарушителя> [причина]' , value = 'Забанить участника на сервере', inline = False)
		emb.add_field( name = f'{config.PREFIX}kick <пинг нарушителя> [причина]', value = 'Выгнать участника с сервера', inline = False )
		emb.add_field( name = f'{config.PREFIX}clear [кол-во сообщений(макс. 50)]', value = 'Очистить определённое кол-во сообщений', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	@help.command()
	async def settings(self, ctx):
		emb = discord.Embed( title = 'Настройки сервера', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}slowmode <продолжительность>' , value = 'Установить медленный режим', inline = False)
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	@help.command()
	async def support(self, ctx):
		emb = discord.Embed( title = 'Команды поддержки', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}bug [суть бага]' , value = 'Отправить баг разработчику бота', inline = False)
		emb.add_field( name = f'{config.PREFIX}idea [ваша идея]', value = 'Отправить идею разработчику бота', inline = False )
		emb.add_field( name = f'{config.PREFIX}invite', value = 'Пригласить бота к себе на сервер', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )



	@help.command()
	async def fun(self, ctx):
		emb = discord.Embed( title = 'Развлекательные команды', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}bird', value = 'Показать фото птицы', inline = False )
		emb.add_field( name = f'{config.PREFIX}cat', value = 'Показать фото кота', inline = False )
		emb.add_field( name = f'{config.PREFIX}dog', value = 'Показать фото собаки', inline = False )
		emb.add_field( name = f'{config.PREFIX}fox', value = 'Показать фото лисы', inline = False )
		emb.add_field( name = f'{config.PREFIX}koala', value = 'Показать фото коалы', inline = False )
		emb.add_field( name = f'{config.PREFIX}panda', value = 'Показать фото панды', inline = False )
		emb.add_field( name = f'{config.PREFIX}eightball', value = 'Волшебный шар', inline = False )
		emb.add_field( name = f'{config.PREFIX}flip', value = 'Орёл или решка', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	@help.command()
	async def premium(self, ctx):
		emb = discord.Embed( title = 'Премиум команды', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}donate', value = 'Оформить премиум подписку', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	@help.command()
	async def utility(self, ctx):
		emb = discord.Embed( title = 'Утилиты', color = config.MAIN_COLOR )
		emb.add_field( name = f'{config.PREFIX}calc [пример]', value = 'Калькулятор', inline = False )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )
		



def setup(client):
	client.add_cog(Help(client))
	print('[Cog] Help загружен!')