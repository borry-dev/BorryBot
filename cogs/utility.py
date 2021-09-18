import discord
from discord.ext import commands

import config

import requests
import json

class Utility(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Calc
	
	@commands.command()
	@commands.guild_only()
	async def calc(self, ctx, *, exp = None):
		if exp is None:
			await ctx.send( embed = discord.Embed( title = "Ошибка!", description = f"Укажите пример", color= config.ERR_COLOR ) )
		else:
			link = 'http://api.mathjs.org/v4/'

			data = {"expr": [f"{exp}"]}

			try:
				re = requests.get( link, params = data )
				responce = re.json()

				emb = discord.Embed( title = 'Калькулятор', color = config.MAIN_COLOR)
				emb.add_field( name = 'Задача:', value = exp )
				emb.add_field( name = 'Решение:', value = str( responce ) )
				emb.set_thumbnail( url = self.client.user.avatar_url )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )
			except:
				await ctx.send( embed = discord.Embed( title = "Ошибка!", description = f"Нельзя использовать текст в примере", color= config.ERR_COLOR ) )	


def setup(client):
	client.add_cog(Utility(client))
	print('[Cog] Utility загружен!')