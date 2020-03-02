import discord
from discord.ext import commands
from logs import Logs
import CONF
import asyncio
from background.warn import warn_to_discord


class CBSParse(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=[CONF.PREFIX])
        self.logger = Logs.create_logger(self)
        self.loop = asyncio.get_event_loop()
        for i in CONF.EXTENSIONS:
            self.load_extension(i)

    async def on_ready(self):
        self.logger.info("Bot Ready.")
        self.loop.create_task(warn_to_discord(self))


bot = CBSParse()
bot.run(CONF.BOT_TOKEN)
