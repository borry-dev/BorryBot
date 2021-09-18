import discord
from discord.ext import commands

import config


class Settings(commands.Cog):
	def __init__(self,client):
		self.client = client


	@commands.command()
	@commands.guild_only()
	@commands.has_permissions( manage_messages = True )
	async def slowmode(self, ctx, sec:int = None):
		if sec is None:
			emb = discord.Embed( title = 'Ошибка!', description = f'Укажите продолжительность медленного режима', color = config.ERR_COLOR )
			await ctx.send( embed = emb )
		else:
			if sec > 0:
				await ctx.channel.edit( slowmode_delay = sec )
				emb = discord.Embed( title = 'Установлен медленный режим!', description = f'Для канала `{ctx.channel.name}` установлен медленный режим в `{sec}s`', color = config.MAIN_COLOR )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )
			if sec < 0:
				emb = discord.Embed( title = 'Ошибка!', description = f'Введите число выше 0!', color = config.ERR_COLOR )
				await ctx.send( embed = emb )
			if sec == 0:
				await ctx.channel.edit( slowmode_delay = sec )
				emb = discord.Embed( title = 'Отключён медленный режим!', description = f'Для канала `{ctx.channel.name}` отключён медленный режим', color = config.MAIN_COLOR )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )


def setup(client):
	client.add_cog(Settings(client))
	print('[Cog] Settings загружен!')