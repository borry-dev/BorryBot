import discord
from discord.ext import commands

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, sec: int = None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if sec is None:
                emb = discord.Embed(title='Ошибка!', description=f'Укажите продолжительность медленного режима',
                                    color=config.ERR_COLOR)
                await ctx.send(embed=emb)
            else:
                if sec > 0:
                    await ctx.channel.edit(slowmode_delay=sec)
                    emb = discord.Embed(title='Установлен медленный режим!',
                                        description=f'Для канала `{ctx.channel.name}` установлен медленный режим в `{sec}s`',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                if sec < 0:
                    emb = discord.Embed(title='Ошибка!', description=f'Введите число выше 0!', color=config.ERR_COLOR)
                    await ctx.send(embed=emb)
                if sec == 0:
                    await ctx.channel.edit(slowmode_delay=sec)
                    emb = discord.Embed(title='Отключён медленный режим!',
                                        description=f'Для канала `{ctx.channel.name}` отключён медленный режим',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
        else:
            if sec is None:
                emb = discord.Embed(title='Error!', description=f'Specify the duration of the slow mode',
                                    color=config.ERR_COLOR)
                await ctx.send(embed=emb)
            else:
                if sec > 0:
                    await ctx.channel.edit(slowmode_delay=sec)
                    emb = discord.Embed(title='Slow mode is enabled!',
                                        description=f'For the channel `{ctx.channel.name}` slow mode is set to `{sec}s`',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                if sec < 0:
                    emb = discord.Embed(title='Error!', description=f'Enter a number above 0!', color=config.ERR_COLOR)
                    await ctx.send(embed=emb)
                if sec == 0:
                    await ctx.channel.edit(slowmode_delay=sec)
                    emb = discord.Embed(title='Slow mode is disabled!',
                                        description=f'For the channel `{ctx.channel.name}` slow mode disabled',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def review(self, ctx, *, text=None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if text is None:
                emb = discord.Embed(title='Ошибка!', description='Вы не указали текст!', color=config.MAIN_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                channel = self.client.get_channel(config.REVIEWS_CHANNEL)
                emb = discord.Embed(title='Отзыв!', color=config.MAIN_COLOR)
                emb.add_field(name="Отзыв:", value=text, inline=False)
                emb.set_footer(text=f"Автор:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}",
                               icon_url=ctx.author.avatar_url)
                await channel.send(embed=emb)
                embed = discord.Embed(title='Отзыв отправлен!', description=f'Отзыв: {text}', color=config.MAIN_COLOR)
                embed.set_thumbnail(url=self.client.user.avatar_url)
                embed.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)
        else:
            if text is None:
                emb = discord.Embed(title='Error!', description='You didn\'t specify the text!',
                                    color=config.MAIN_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                channel = self.client.get_channel(config.REVIEWS_CHANNEL)
                emb = discord.Embed(title='Review!', color=config.MAIN_COLOR)
                emb.add_field(name="Review:", value=text, inline=False)
                emb.set_footer(text=f"Username:{ctx.author.name}#{ctx.author.discriminator}\nID:{ctx.author.id}",
                               icon_url=ctx.author.avatar_url)
                await channel.send(embed=emb)
                embed = discord.Embed(title='The review has been sent!', description=f'Review: {text}',
                                      color=config.MAIN_COLOR)
                embed.set_thumbnail(url=self.client.user.avatar_url)
                embed.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Settings(client))
    print('[Cog] Settings загружен!')
