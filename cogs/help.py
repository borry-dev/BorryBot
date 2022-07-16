import discord
from discord.ext import commands

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def help(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if ctx.invoked_subcommand == None:
                emb = discord.Embed(title='Команды',
                                    description=f'Для просмотра команд введите `{config.PREFIX}help [название модуля]`',
                                    color=config.MAIN_COLOR)
                emb.add_field(name=f'{config.PREFIX}help info', value='Информационные команды', inline=False)
                emb.add_field(name=f'{config.PREFIX}help moderation', value='Команды модерации', inline=False)
                emb.add_field(name=f'{config.PREFIX}help settings', value='Настройки сервера', inline=False)
                emb.add_field(name=f'{config.PREFIX}help support', value='Команды поддержки', inline=False)
                emb.add_field(name=f'{config.PREFIX}help fun', value='Развлекательные команды', inline=False)
                emb.add_field(name=f'{config.PREFIX}help utility', value='Утилиты', inline=False)
                emb.set_thumbnail(url=self.client.user.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
        else:
            if ctx.invoked_subcommand == None:
                emb = discord.Embed(title='Commands',
                                    description=f'To view the commands, enter `{config.PREFIX}help [module name]`',
                                    color=config.MAIN_COLOR)
                emb.add_field(name=f'{config.PREFIX}help info', value='Information commands', inline=False)
                emb.add_field(name=f'{config.PREFIX}help moderation', value='Moderation commands', inline=False)
                emb.add_field(name=f'{config.PREFIX}help settings', value='Server Settings', inline=False)
                emb.add_field(name=f'{config.PREFIX}help support', value='Support commands', inline=False)
                emb.add_field(name=f'{config.PREFIX}help fun', value='Fun commands', inline=False)
                emb.add_field(name=f'{config.PREFIX}help utility', value='Utilities', inline=False)
                emb.set_thumbnail(url=self.client.user.avatar_url)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)

    @help.command()
    async def info(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Информационные команды', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}info', value='Узнать информацию о боте', inline=False)
            emb.add_field(name=f'{config.PREFIX}ping', value='Узнать пинг бота', inline=False)
            emb.add_field(name=f'{config.PREFIX}stats', value='Узнать статистику бота', inline=False)
            emb.add_field(name=f'{config.PREFIX}hosting', value='Узнать информацию о хостинге', inline=False)
            emb.add_field(name=f'{config.PREFIX}user <пинг пользователя>', value='Узнать информацию о пользователе',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}server', value='Узнать ниформацию о сервере', inline=False)
            emb.add_field(name=f'{config.PREFIX}vote', value='Мониторинги бота', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Information commands', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}info', value='Find out information about the bot', inline=False)
            emb.add_field(name=f'{config.PREFIX}ping', value='Find out the ping bot', inline=False)
            emb.add_field(name=f'{config.PREFIX}stats', value='Find out bot statistics', inline=False)
            emb.add_field(name=f'{config.PREFIX}hosting', value='Find out information about hosting', inline=False)
            emb.add_field(name=f'{config.PREFIX}user <member ping>', value='Find out user information', inline=False)
            emb.add_field(name=f'{config.PREFIX}server', value='Find out information about the server', inline=False)
            emb.add_field(name=f'{config.PREFIX}vote', value='Bot monitoring', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)

    @help.command()
    async def moderation(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Команды модерации', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}ban <пинг нарушителя> [причина]', value='Забанить участника на сервере',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}kick <пинг нарушителя> [причина]', value='Выгнать участника с сервера',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}clear [кол-во сообщений(макс. 50)]',
                          value='Очистить определённое кол-во сообщений', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Moderation commands', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}ban <member ping> [reason]', value='Ban a member on the server',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}kick <member ping> [reason]', value='Kick a member on the server',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}clear [number of messages(max. 50)]',
                          value='Clear a certain number of messages', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)

    @help.command()
    async def settings(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Настройки сервера', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}slowmode <продолжительность>', value='Установить медленный режим',
                          inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Server Settings', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}slowmode <duration>', value='Set Slowmode', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)

    @help.command()
    async def support(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Команды поддержки', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}review [отзыв]', value='Написать отзыв', inline=False)
            emb.add_field(name=f'{config.PREFIX}bug [суть бага]', value='Отправить баг разработчику бота', inline=False)
            emb.add_field(name=f'{config.PREFIX}idea [ваша идея]', value='Отправить идею разработчику бота',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}invite', value='Пригласить бота к себе на сервер', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Support commands', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}review [text]', value='Write a review', inline=False)
            emb.add_field(name=f'{config.PREFIX}bug [the essence of the bug]', value='Send a bug to the bot developer',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}idea [your idea]', value='Send an idea to the bot developer',
                          inline=False)
            emb.add_field(name=f'{config.PREFIX}invite', value='Invite a bot to your server', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)

    @help.command()
    async def fun(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Развлекательные команды', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}bird', value='Показать фото птицы', inline=False)
            emb.add_field(name=f'{config.PREFIX}cat', value='Показать фото кота', inline=False)
            emb.add_field(name=f'{config.PREFIX}dog', value='Показать фото собаки', inline=False)
            emb.add_field(name=f'{config.PREFIX}fox', value='Показать фото лисы', inline=False)
            emb.add_field(name=f'{config.PREFIX}koala', value='Показать фото коалы', inline=False)
            emb.add_field(name=f'{config.PREFIX}panda', value='Показать фото панды', inline=False)
            emb.add_field(name=f'{config.PREFIX}eightball', value='Волшебный шар', inline=False)
            emb.add_field(name=f'{config.PREFIX}flip', value='Орёл или решка', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Fun commands', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}bird', value='Show a photo of a bird', inline=False)
            emb.add_field(name=f'{config.PREFIX}cat', value='Show a photo of a cat', inline=False)
            emb.add_field(name=f'{config.PREFIX}dog', value='Show a photo of a dog', inline=False)
            emb.add_field(name=f'{config.PREFIX}fox', value='Show a photo of a fox', inline=False)
            emb.add_field(name=f'{config.PREFIX}koala', value='Show koala photo', inline=False)
            emb.add_field(name=f'{config.PREFIX}panda', value='Show panda photo', inline=False)
            emb.add_field(name=f'{config.PREFIX}eightball', value='Magic Ball', inline=False)
            emb.add_field(name=f'{config.PREFIX}flip', value='Heads or tails', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)

    @help.command()
    async def utility(self, ctx):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            emb = discord.Embed(title='Утилиты', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}calc [пример]', value='Калькулятор', inline=False)
            emb.add_field(name=f'{config.PREFIX}avatar <пинг пользователя>', value='Просмотр аватара', inline=False)
            emb.add_field(name=f'{config.PREFIX}spotify <пинг пользователя>', value='Информация о треке Spotify',
                          inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title='Utilities', color=config.MAIN_COLOR)
            emb.add_field(name=f'{config.PREFIX}calc [mathematical example]', value='Calculator', inline=False)
            emb.add_field(name=f'{config.PREFIX}avatar <member ping>', value='Viewing an avatar', inline=False)
            emb.add_field(name=f'{config.PREFIX}spotify <member ping>', value='Spotify Track Information', inline=False)
            emb.set_thumbnail(url=self.client.user.avatar_url)
            emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
            await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Help(client))
    print('[Cog] Help загружен!')
