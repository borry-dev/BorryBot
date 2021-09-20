import discord
from discord.ext import commands

import config


class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client


	#Ban

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions( ban_members = True )
	async def ban( self, ctx, member:discord.Member=None, *, reason = None ):
		if member is None:
			emb = discord.Embed( title = 'Ошибка', description = 'Не указан пользователь!', color = config.ERR_COLOR )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )
		else:
			await member.ban( reason = reason )
			emb = discord.Embed( title = 'Бан', color = config.MAIN_COLOR )
			emb.add_field( name = 'Модератор:', value = ctx.message.author.mention, inline = False )
			emb.add_field( name = 'Нарушитель', value = member.mention, inline = False )
			emb.add_field( name = 'Причина', value = reason, inline = False )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )


	#Kick

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions( kick_members = True )
	async def kick( self, ctx, member:discord.Member=None, *, reason = None ):
		if member is None:
			emb = discord.Embed( title = 'Ошибка', description = 'Не указан пользователь!', color = config.ERR_COLOR )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )
		else:
			await member.kick( reason = reason )
			emb = discord.Embed( title = 'Кик', color = config.MAIN_COLOR )
			emb.add_field( name = 'Модератор', value = ctx.message.author.mention, inline = False )
			emb.add_field( name = 'Нарушитель', value = member.mention, inline = False )
			emb.add_field( name = 'Причина', value = reason, inline = False )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )


	#Clear

	@commands.command()
	@commands.guild_only()
	@commands.has_permissions( manage_messages = True )
	async def clear( self, ctx, amount:int=None ):
		if amount is None:
			emb = discord.Embed( title = 'Ошибка', description = 'Не указан аргумент!', color = config.ERR_COLOR )
			emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
			await ctx.send( embed = emb )
		else:
			if amount > 50:
				emb = discord.Embed( title = 'Ошибка', description = 'За раз можно удалить максимум 50 сообщений', color = config.ERR_COLOR )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )
			if amount <= 0:
				emb = discord.Embed( title = 'Ошибка', description = 'Бот не может восстанавливать команды!', color = config.ERR_COLOR )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )
			else:
				await ctx.channel.purge( limit = amount + 1 )
				emb = discord.Embed( title = 'Отчистка сообщений', description = f'{ctx.author.mention} удалил {amount} сообщений', color = config.MAIN_COLOR )
				emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
				await ctx.send( embed = emb )

			


def setup(client):
	client.add_cog(Moderation(client))
	print('[Cog] Moderation загружен!')