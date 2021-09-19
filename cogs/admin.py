import discord
from discord.ext import commands

import config


class Admin(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Modules

	@commands.command()
	@commands.guild_only()
	async def modules(self, ctx):

		modules_count = len(self.client.cogs)

		if ctx.author.id == config.DEVELOPERS:
			emb = discord.Embed( title = f'Модули BorryBot\nМодулей загружено: `{modules_count}`', description = ", ".join(self.client.cogs), color = config.MAIN_COLOR )
			emb.set_thumbnail( url = self.client.user.avatar_url )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )
		else:
			pass


	#Getinvite

	@commands.command()
	@commands.guild_only()
	async def getinvite(self, ctx, id):
		if ctx.author.id == config.DEVELOPERS:
			guild = await self.client.fetch_guild(id)
			await ctx.send([invite.code for invite in await guild.invites()])
		else:
			pass


	@commands.command()
	@commands.guild_only()
	async def eval(self, ctx, *, args):
		result = eval(args)
		await ctx.send(result)


def setup(client):
	client.add_cog(Admin(client))
	print('[Cog] Admin загружен!')