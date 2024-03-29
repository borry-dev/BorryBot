import discord
from discord.ext import commands
from discord.ext.commands import errors

import config
import sqlite3

db = sqlite3.connect('DB/language.sqlite3')
cursor = db.cursor()


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if cursor.execute(f"SELECT guild_id FROM english WHERE guild_id = {ctx.guild.id}").fetchone() is None:
            if isinstance(err, errors.CommandNotFound):
                pass
            elif isinstance(err, errors.NoPrivateMessage):
                pass
            elif isinstance(err, errors.MissingPermissions):
                emb = discord.Embed(title="Недостаточно прав!",
                                    description=f"У вас недостаточно прав для запуска этой команды!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.NSFWChannelRequired):
                emb = discord.Embed(title="Ошибка!",
                                    description=f"Использование данной команды разрешено только в NSFW каналах!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.CommandOnCooldown):
                emb = discord.Embed(title="У вас кулдаун!", description=f"У вас не прошёл кулдаун! Попробуйте позже!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.MemberNotFound):
                emb = discord.Embed(title="Ошибка!", description=f"Пользователь не найден!", color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.MissingRequiredArgument):
                emb = discord.Embed(title="Ошибка!", description=f"Вы не указали аргумент!", color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                channel = self.client.get_channel(config.ERR_CHANNEL)
                await ctx.send(embed=discord.Embed(title="Неизвестная ошибка!",
                                                   description=f"Произошла неизвестная ошибка: `{err}`\nОшибка уже отправлена разработчику для её исправления",
                                                   color=config.ERR_COLOR))
                emb = discord.Embed(title='Ошибка!', color=config.MAIN_COLOR)
                emb.add_field(name="Ошибка:", value=f"`{err}`", inline=False)
                emb.set_footer(text=f"Guild:{ctx.guild.name}\nGuild ID:{ctx.guild.id}", icon_url=ctx.guild.icon_url)
                emb.set_thumbnail(url=ctx.guild.icon_url)
                await channel.send(embed=emb)
        else:
            if isinstance(err, errors.CommandNotFound):
                pass
            elif isinstance(err, errors.NoPrivateMessage):
                pass
            elif isinstance(err, errors.MissingPermissions):
                emb = discord.Embed(title="Missing permissions!",
                                    description=f"You don't have permission to execute this command!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.NSFWChannelRequired):
                emb = discord.Embed(title="Error!",
                                    description=f"The use of this command is allowed only in NSFW channels!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.CommandOnCooldown):
                emb = discord.Embed(title="You have a cooldown!", description=f"Your cooldown failed! Try again later!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.MemberNotFound):
                emb = discord.Embed(title="Error!", description=f"Member not found!", color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            elif isinstance(err, commands.errors.MissingRequiredArgument):
                emb = discord.Embed(title="Error!", description=f"You didn't specify an argument!",
                                    color=config.ERR_COLOR)
                emb.set_footer(text=f'{self.client.user.name} | {config.YEAR}', icon_url=self.client.user.avatar_url)
                await ctx.send(embed=emb)
            else:
                channel = self.client.get_channel(config.ERR_CHANNEL)
                await ctx.send(embed=discord.Embed(title="Unknown error!",
                                                   description=f"An unknown error has occurred: `{err}`\nThe error has already been sent to the developer to fix it",
                                                   color=config.ERR_COLOR))
                emb = discord.Embed(title='Error!', color=config.MAIN_COLOR)
                emb.add_field(name="Error:", value=f"`{err}`", inline=False)
                emb.set_footer(text=f"Guild:{ctx.guild.name}\nGuild ID:{ctx.guild.id}", icon_url=ctx.guild.icon_url)
                emb.set_thumbnail(url=ctx.guild.icon_url)
                await channel.send(embed=emb)


def setup(client):
    client.add_cog(Errors(client))
    print('[Cog] Errors загружен!')
