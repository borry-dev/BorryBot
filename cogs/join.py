import discord
from discord.ext import commands

import config


class Join(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_guild_join( self, guild ):
		emb = discord.Embed( title = 'BorryBot', description = f'Привет! Спасибо что добавил меня на свой сервер. Для просмотра команд введите `{config.PREFIX}help`', color = config.MAIN_COLOR )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await guild.text_channels[0].send(embed = emb)


def setup(client):
	client.add_cog(Join(client))
	print('[Cog] Join загружен!')