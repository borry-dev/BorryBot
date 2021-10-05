import discord
from discord.ext import tasks, commands
import aiohttp
from aiohttp import FormData
import asyncio

import config

class SDC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sdc.start()

    
    def cog_unload(self):
        self.sdc.cancel()


    @tasks.loop(minutes = 10)
    async def sdc(self):
        try:
            guildscount = str(len(self.bot.guilds))
            tok   = config.SDC_TOKEN
            token = f"SDC {tok}"
            botid = "862195560019001344"
            headers={"Authorization": token}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(f'https://api.server-discord.com/v2/bots/{botid}/stats', json={"servers": guildscount, "shards": "1"}) as response:
                    js = await response.json()
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(SDC(bot))
    print('[Cog] SDC запущен!')