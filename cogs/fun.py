import discord
from discord.ext import commands

import requests
import json
import random

import config


answers = ["Конечно!", "Можешь быть уверен(а)","Возмжно!","Нет!","Никак нет!", "Не думаю!"]


class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Bird

	@commands.command()
	@commands.guild_only()
	async def bird(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/birb' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':bird:', color = config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	
	#Cat

	@commands.command()
	@commands.guild_only()
	async def cat(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/cat' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':cat:', color =config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	
	#Dog

	@commands.command()
	@commands.guild_only()
	async def dog(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/dog' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':dog:', color = config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )

	
	#Fox

	@commands.command()
	@commands.guild_only()
	async def fox(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/fox' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':fox:', color = config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )

	
	#Koala

	@commands.command()
	@commands.guild_only()
	async def koala(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/koala' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':koala:', color = config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )

	
	#Panda

	@commands.command()
	@commands.guild_only()
	async def panda(self, ctx):
		response = requests.get( 'https://some-random-api.ml/img/panda' )
		json_data = json.loads( response.text )
		emb = discord.Embed( title = ':panda_face:', color = config.MAIN_COLOR )
		emb.set_image( url = json_data['link'] )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#Flip

	@commands.command()
	@commands.guild_only()
	async def flip(self, ctx):
		a = random.choice(['Орёл', 'Решка'])
		emb = discord.Embed( title = 'Орёл или решка?', description = f'Вам выпало: **{a}**', color = config.MAIN_COLOR )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


	#8ball
	
	@commands.command()
	@commands.guild_only()
	async def eightball(self, ctx, arg=None):
		if arg == None:
			await ctx.send( embed = discord.Embed( title = "Вы не ввели вопрос!", color = config.ERR_COLOR ) )
		else:
			embed = discord.Embed( title = "🔮 Магический шар", description = random.choice(answers), color = config.MAIN_COLOR )
			await ctx.send( embed = embed )


def setup(client):
	client.add_cog(Fun(client))
	print('[Cog] Fun загружен!')