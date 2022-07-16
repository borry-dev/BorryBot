import discord
from discord.ext import commands

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS english(
    guild_id BIGINT
)""")


class Language(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def lang(self, ctx, lang=None):
        if lang is None:
            if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
                emb = discord.Embed(title='На сервере установлен русский язык!',
                                    description=f'Для смены языка введите `{config.PREFIX}lang [rus/eng]`',
                                    color=config.MAIN_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title='English is installed on the server!',
                                    description=f'To change the language, enter `{config.PREFIX}lang [rus/eng]`',
                                    color=config.MAIN_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
        else:
            if lang == 'rus':
                if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
                    emb = discord.Embed(title='На этом сервере уже используется русский язык!', color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                else:
                    cursor.execute(f"DELETE FROM english WHERE guild_id = {ctx.guild.id}")
                    db.commit()
                    emb = discord.Embed(title='Для вашего сервера установлен русский язык!', color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
            elif lang == 'eng':
                if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
                    cursor.execute(f"INSERT INTO english VALUES({ctx.guild.id})")
                    db.commit()
                    emb = discord.Embed(title='English is installed for your server!', color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                else:
                    emb = discord.Embed(title='English is already used on this server!', color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
            else:
                if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
                    emb = discord.Embed(title='Выбран недоступный язык!',
                                        description='`rus` - установить русский язык\n`eng` - установить английский язык',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                else:
                    emb = discord.Embed(title='An unavailable language is selected!',
                                        description='`rus` - install the Russian language\n`eng` - install the English language',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Language(client))
    print('[Cog] Language загружен!')
