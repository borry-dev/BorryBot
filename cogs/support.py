import discord
from discord.ext import commands

import config


class Support(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Bug

	@commands.command()
	@commands.guild_only()
	@commands.cooldown( 1, 10800, commands.BucketType.user )
	async def bug(self, ctx, *, bug=None):
		if bug is None:
			await ctx.send( embed = discord.Embed( title = "Ошибка!", description = "Вы не указали баг!", color= config.MAIN_COLOR ) )
		else:
			channel = self.client.get_channel(config.BUG_CHANNEL)
			emb = discord.Embed( title = 'Баг!', color = config.MAIN_COLOR )
			emb.add_field( name = "Баг:", value = bug, inline = False )
			emb.set_footer( text = f"Username:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}", icon_url = ctx.author.avatar_url )
			await channel.send( embed = emb )
			embed = discord.Embed( title = 'Баг отправлен!',description = f'Баг: {bug}',color = config.MAIN_COLOR )
			embed.set_thumbnail( url = self.client.user.avatar_url )
			embed.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = embed )




	#Idea

	@commands.command()
	@commands.guild_only()
	@commands.cooldown( 1, 10800, commands.BucketType.user )
	async def idea(self, ctx, *, idea=None):
		if idea is None:
			await ctx.send( embed = discord.Embed( title = "Ошибка!", description = "Вы не указали идею!", color= config.MAIN_COLOR ) )
		else:
			channel = self.client.get_channel(config.IDEA_CHANNEL)
			emb = discord.Embed( title = 'Идея!', color = config.MAIN_COLOR )
			emb.add_field( name = "Идея:", value = idea, inline = False )
			emb.set_footer( text = f"Username:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}", icon_url = ctx.author.avatar_url )
			await channel.send( embed = emb )
			embed = discord.Embed( title = 'Идея отправлена!',description = f'Идея: {idea}',color = config.MAIN_COLOR )
			embed.set_thumbnail( url = self.client.user.avatar_url )
			embed.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = embed )


	#Invite

	@commands.command()
	@commands.guild_only()
	async def invite(self, ctx):
		emb = discord.Embed( title = ':link: | Пригласить бота', description = f'[Пригласить](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions={config.SCOPE}&scope=bot)', color = config.MAIN_COLOR )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await ctx.send( embed = emb )


def setup(client):
	client.add_cog(Support(client))
	print('[Cog] Support загружен!')