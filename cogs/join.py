import discord
from discord.ext import commands

import config


class Join(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_guild_join( self, guild ):
		emb = discord.Embed( title = 'Hello!', description = f'Thank you for adding to your server!\n\n:gear: **Commands**\nTo view the list of commands, enter `{config.PREFIX}help`\n\n**:speech_balloon: Language**\nTo change the language, enter `{config.PREFIX}lang [rus/eng]`\n\n:question: Have a question?\n**Our Discord official server:** https://discord.gg/FJRj894gUn', color = config.MAIN_COLOR )
		emb.set_thumbnail( url = self.client.user.avatar_url )
		emb.set_footer( text = f'{self.client.user.name} | {config.YEAR}', icon_url = self.client.user.avatar_url )
		await guild.text_channels[0].send(embed = emb)


def setup(client):
	client.add_cog(Join(client))
	print('[Cog] Join загружен!')