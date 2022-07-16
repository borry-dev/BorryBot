import discord
from discord.ext import commands

import config


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel = self.client.get_channel(config.SERVER_CHANNEL)

        emb = discord.Embed( title = f'Меня добавили на сервер {guild.name}', description = f'Кол-во участников: `{len(guild.members)}`', color = config.MAIN_COLOR)
        emb.set_thumbnail(url=guild.icon_url)
        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
        await channel.send(embed=emb)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channel = self.client.get_channel(config.SERVER_CHANNEL)

        emb = discord.Embed( title = f'Меня выгнали с сервера {guild.name}', description = f'Кол-во участников: `{len(guild.members)}`', color = config.MAIN_COLOR)
        emb.set_thumbnail(url=guild.icon_url)
        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
        await channel.send(embed=emb)


def setup(client):
    client.add_cog(Events(client))
    print('[Cog] Events загружен!')