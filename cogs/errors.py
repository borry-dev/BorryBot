import discord
from discord.ext import commands
from discord.ext.commands import errors

import config


class Errors(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.Cog.listener()
	async def on_command_error(self, ctx, err):
		if isinstance(err, errors.CommandNotFound):
			embed = discord.Embed( title = '-', description = '-', color = config.MAIN_COLOR )
		elif isinstance(err, errors.NoPrivateMessage):
			pass
		elif isinstance(err, errors.MissingPermissions):
			await ctx.send( embed = discord.Embed( title = "Недостаточно прав!", description = f"У вас недостаточно прав для запуска этой команды!", color= config.ERR_COLOR) )
		elif isinstance(err, commands.errors.NSFWChannelRequired):
			await ctx.send( embed = discord.Embed( title = "Ошибка!", description = f"Использование данной команды разрешено только в NSFW каналах!", color = config.ERR_COLOR) )
		elif isinstance(err, commands.CommandOnCooldown):
			await ctx.send( embed = discord.Embed( title = "У вас кулдаун!", description = f"У вас не прошёл кулдаун! Попробуйте позже!", color = config.ERR_COLOR) )
		else:
			channel = self.client.get_channel(config.ERR_CHANNEL)
			await ctx.send( embed = discord.Embed( title = "Неизвестная ошибка!", description = f"Произошла неизвестная ошибка: `{err}`\nОшибка уже отправлена разработчику для её исправления", color= config.ERR_COLOR) )
			emb = discord.Embed( title = 'Ошибка!', color = config.MAIN_COLOR )
			emb.add_field( name = "Ошибка:", value = f"`{err}`", inline = False )
			emb.set_footer( text = f"Guild:{ctx.guild.name}\nGuild ID:{ctx.guild.id}", icon_url = ctx.guild.icon_url )
			emb.set_thumbnail( url = ctx.guild.icon_url )
			await channel.send( embed = emb )



def setup(client):
	client.add_cog(Errors(client))
	print('[Cog] Errors загружен!')