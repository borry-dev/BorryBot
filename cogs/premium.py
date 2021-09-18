import discord
from discord.ext import commands

import config

class Premium(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Donate

	@commands.command()
	@commands.guild_only()
	async def donate(self, ctx):
		await ctx.send( embed = discord.Embed( title = "Ошибка!", description = f"Команда находится в разработке", color = config.ERR_COLOR ) )


def setup(client):
	client.add_cog(Premium(client))
	print('[Cog] Premium загружен!')