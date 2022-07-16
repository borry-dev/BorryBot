import discord
from discord.ext import commands

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Admin(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Modules

	@commands.command()
	@commands.guild_only()
	async def modules(self, ctx):
		if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
			modules_count = len(self.client.cogs)

			if ctx.author.id == config.DEVELOPERS:
				emb = discord.Embed( title = f'Модули BorryBot\nМодулей загружено: `{modules_count}`', description = ", ".join(self.client.cogs), color = config.MAIN_COLOR )
				emb.set_thumbnail( url = self.client.user.avatar_url )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )
			else:
				pass
		else:
			modules_count = len(self.client.cogs)

			if ctx.author.id == config.DEVELOPERS:
				emb = discord.Embed(title=f'BorryBot Modules\nModules loaded: `{modules_count}`',
									description=", ".join(self.client.cogs), color=config.MAIN_COLOR)
				emb.set_thumbnail(url=self.client.user.avatar_url)
				emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
				await ctx.send(embed=emb)
			else:
				pass


	#Getinvite

	@commands.command()
	@commands.guild_only()
	async def getinvite(self, ctx, id):
		if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
			if ctx.author.id == config.DEVELOPERS:
				guild = await self.client.fetch_guild(id)
				await ctx.send([invite.code for invite in await guild.invites()])
			else:
				pass
		else:
			if ctx.author.id == config.DEVELOPERS:
				guild = await self.client.fetch_guild(id)
				await ctx.send([invite.code for invite in await guild.invites()])
			else:
				pass


def setup(client):
	client.add_cog(Admin(client))
	print('[Cog] Admin загружен!')