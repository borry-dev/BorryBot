import discord
from discord import Spotify
from discord.ext import commands

import config

import sqlite3
import requests

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Calc

    @commands.command()
    @commands.guild_only()
    async def calc(self, ctx, *, exp=None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if exp is None:
                await ctx.send(
                    embed=discord.Embed(title="Ошибка!", description=f"Укажите пример", color=config.ERR_COLOR))
            else:
                link = 'http://api.mathjs.org/v4/'

                data = {"expr": [f"{exp}"]}

                try:
                    re = requests.get(link, params=data)
                    responce = re.json()

                    emb = discord.Embed(title='Калькулятор', color=config.MAIN_COLOR)
                    emb.add_field(name='Задача:', value=exp)
                    emb.add_field(name='Решение:', value=str(responce))
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                except:
                    await ctx.send(
                        embed=discord.Embed(title="Ошибка!", description=f"Нельзя использовать текст в примере",
                                            color=config.ERR_COLOR))
        else:
            if exp is None:
                await ctx.send(embed=discord.Embed(title="Error!", description=f"Enter a mathematical example",
                                                   color=config.ERR_COLOR))
            else:
                link = 'http://api.mathjs.org/v4/'

                data = {"expr": [f"{exp}"]}

                try:
                    re = requests.get(link, params=data)
                    responce = re.json()

                    emb = discord.Embed(title='Calculator', color=config.MAIN_COLOR)
                    emb.add_field(name='Task:', value=exp)
                    emb.add_field(name='Answer:', value=str(responce))
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                except:
                    await ctx.send(embed=discord.Embed(title="Error!",
                                                       description=f"You can't use text in the mathematical example",
                                                       color=config.ERR_COLOR))

    # Avatar

    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member = None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if member is None:
                emb = discord.Embed(title=f'Аватар **{ctx.author.name}**', color=config.MAIN_COLOR)
                emb.set_image(url=ctx.author.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f'Аватар **{member.name}**', color=config.MAIN_COLOR)
                emb.set_image(url=member.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
        else:
            if member is None:
                emb = discord.Embed(title=f'Avatar **{ctx.author.name}**', color=config.MAIN_COLOR)
                emb.set_image(url=ctx.author.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f'Avatar **{member.name}**', color=config.MAIN_COLOR)
                emb.set_image(url=member.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)

    # Spotify

    @commands.command()
    @commands.guild_only()
    async def spotify(self, ctx, member: discord.Member = None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if member is None:
                for activity in ctx.author.activities:
                    if isinstance(activity, Spotify):
                        emb = discord.Embed(title='Spotify', color=config.MAIN_COLOR)
                        emb.add_field(name='Трек:',
                                      value=f'[{activity.title}](https://open.spotify.com/track/{activity.track_id})',
                                      inline=False)
                        emb.add_field(name='Исполнитель:', value=activity.artist, inline=False)
                        emb.add_field(name='Альбом:', value=activity.album, inline=False)
                        m1, s1 = divmod(int(activity.duration.seconds), 60)
                        song_length = f'{m1}:{s1}'
                        emb.add_field(name='Продолжительность:', value=song_length, inline=False)
                        emb.set_thumbnail(url=activity.album_cover_url)
                        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                       icon_url=self.client.user.avatar_url)
                        await ctx.send(embed=emb)
            else:
                for activity in member.activities:
                    if isinstance(activity, Spotify):
                        emb = discord.Embed(title='Spotify', color=config.MAIN_COLOR)
                        emb.add_field(name='Трек:',
                                      value=f'[{activity.title}](https://open.spotify.com/track/{activity.track_id})',
                                      inline=False)
                        emb.add_field(name='Исполнитель:', value=activity.artist, inline=False)
                        emb.add_field(name='Альбом:', value=activity.album, inline=False)
                        m1, s1 = divmod(int(activity.duration.seconds), 60)
                        song_length = f'{m1}:{s1}'
                        emb.add_field(name='Продолжительность:', value=song_length, inline=False)
                        emb.set_thumbnail(url=activity.album_cover_url)
                        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                       icon_url=self.client.user.avatar_url)
                        await ctx.send(embed=emb)
        else:
            if member is None:
                for activity in ctx.author.activities:
                    if isinstance(activity, Spotify):
                        emb = discord.Embed(title='Spotify', color=config.MAIN_COLOR)
                        emb.add_field(name='Title:',
                                      value=f'[{activity.title}](https://open.spotify.com/track/{activity.track_id})',
                                      inline=False)
                        emb.add_field(name='Artist:', value=activity.artist, inline=False)
                        emb.add_field(name='Album:', value=activity.album, inline=False)
                        m1, s1 = divmod(int(activity.duration.seconds), 60)
                        song_length = f'{m1}:{s1}'
                        emb.add_field(name='Duration:', value=song_length, inline=False)
                        emb.set_thumbnail(url=activity.album_cover_url)
                        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                       icon_url=self.client.user.avatar_url)
                        await ctx.send(embed=emb)
            else:
                for activity in member.activities:
                    if isinstance(activity, Spotify):
                        emb = discord.Embed(title='Spotify', color=config.MAIN_COLOR)
                        emb.add_field(name='Title:',
                                      value=f'[{activity.title}](https://open.spotify.com/track/{activity.track_id})',
                                      inline=False)
                        emb.add_field(name='Artist:', value=activity.artist, inline=False)
                        emb.add_field(name='Album:', value=activity.album, inline=False)
                        m1, s1 = divmod(int(activity.duration.seconds), 60)
                        song_length = f'{m1}:{s1}'
                        emb.add_field(name='Duration:', value=song_length, inline=False)
                        emb.set_thumbnail(url=activity.album_cover_url)
                        emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                       icon_url=self.client.user.avatar_url)
                        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Utility(client))
    print('[Cog] Utility загружен!')
