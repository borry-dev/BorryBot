import discord
from discord.ext import commands

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Ban

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if member is None:
                emb = discord.Embed(title='Ошибка!', description='Не указан пользователь!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif member.id == ctx.author.id:
                emb = discord.Embed(title='Ошибка!', description='Нельзя забанить самого себя!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                await member.ban(reason=reason)
                emb = discord.Embed(title='Бан', color=config.MAIN_COLOR)
                emb.add_field(name='Модератор:', value=ctx.message.author.mention, inline=False)
                emb.add_field(name='Нарушитель', value=member.mention, inline=False)
                emb.add_field(name='Причина', value=reason, inline=False)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
        else:
            if member is None:
                emb = discord.Embed(title='Error!', description='No user specified!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif member.id == ctx.author.id:
                emb = discord.Embed(title='Error!', description='You can\'t ban yourself!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                await member.ban(reason=reason)
                emb = discord.Embed(title='Ban', color=config.MAIN_COLOR)
                emb.add_field(name='Moderator:', value=ctx.message.author.mention, inline=False)
                emb.add_field(name='Offender', value=member.mention, inline=False)
                emb.add_field(name='Reason', value=reason, inline=False)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)

    # Kick

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if member is None:
                emb = discord.Embed(title='Ошибка!', description='Не указан пользователь!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif member.id == ctx.author.id:
                emb = discord.Embed(title='Ошибка!', description='Нельзя кикнуть самого себя!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                await member.kick(reason=reason)
                emb = discord.Embed(title='Кик', color=config.MAIN_COLOR)
                emb.add_field(name='Модератор', value=ctx.message.author.mention, inline=False)
                emb.add_field(name='Нарушитель', value=member.mention, inline=False)
                emb.add_field(name='Причина', value=reason, inline=False)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
        else:
            if member is None:
                emb = discord.Embed(title='Error!', description='No user specified!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif member.id == ctx.author.id:
                emb = discord.Embed(title='Error!', description='You can\'t kick yourself!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                await member.kick(reason=reason)
                emb = discord.Embed(title='Kick', color=config.MAIN_COLOR)
                emb.add_field(name='Moderator', value=ctx.message.author.mention, inline=False)
                emb.add_field(name='Offender', value=member.mention, inline=False)
                emb.add_field(name='Reason', value=reason, inline=False)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)

    # Clear

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if amount is None:
                emb = discord.Embed(title='Ошибка!', description='Не указан аргумент!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                if amount > 50:
                    emb = discord.Embed(title='Ошибка!', description='За раз можно удалить максимум 50 сообщений',
                                        color=config.ERR_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                elif amount <= 0:
                    emb = discord.Embed(title='Ошибка!', description='Бот не может восстанавливать команды!',
                                        color=config.ERR_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                else:
                    await ctx.channel.purge(limit=amount + 1)
                    emb = discord.Embed(title='Отчистка сообщений',
                                        description=f'{ctx.author.mention} удалил {amount} сообщений',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
        else:
            if amount is None:
                emb = discord.Embed(title='Error!', description='No argument specified!', color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                if amount > 50:
                    emb = discord.Embed(title='Error!', description='You can delete a maximum of 50 messages at a time',
                                        color=config.ERR_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                elif amount <= 0:
                    emb = discord.Embed(title='Error!', description='The bot cannot restore commands!',
                                        color=config.ERR_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)
                else:
                    await ctx.channel.purge(limit=amount + 1)
                    emb = discord.Embed(title='Clear', description=f'{ctx.author.mention} deleted {amount} messages',
                                        color=config.MAIN_COLOR)
                    emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}',
                                   icon_url=self.client.user.avatar_url)
                    await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Moderation(client))
    print('[Cog] Moderation загружен!')
