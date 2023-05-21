from discord.ext import commands
from discord.ext.commands import Bot
import discord
import asyncio
import Pyro5.api
import dotenv
import os
import logging
from arrow import utcnow

class Voithos(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(os.getenv('PREFIX')), # type: ignore
            case_insensitive=True,
            intents=discord.Intents.all(),
            help_command=None,
            owner_id=765739254164357121,
            description="The world's first semi self-hosted Discord bot."
        )

    async def on_ready(self):
        logger.info(f"Started as {self.user} (ID: {self.user.id})")
        logger.info(f"Connected to {len(self.guilds)} guilds")
        logger.info("Connected to {len(self.users)} users")


    async def on_message(self, message):
        if message.author.bot:
            return

        logger.info(f"Started as {self.user} (ID: {self.user.id})")
        logger.info(f"Connected to {len(self.guilds)} guilds")
        logger.info("Connected to {len(self.users)} users")
        await message.channel.send("Hello, world!")

def before_startup():
    # If the logs directory doesn't exist, create it
    if not os.path.exists("logs"):
        os.mkdir("logs")



if __name__ == "__main__":
    before_startup()
    dotenv.load_dotenv()
    logger = logging.getLogger("Voithos")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename=f"logs/{utcnow().format('YYYY-MM-DD')}.log", encoding='utf-8', mode='a')
    handler.setFormatter(logging.Formatter('%(smftime)s:%(levelname)s %(name)s %(message)s'))
    logger.addHandler(handler)
    bot = Voithos()
    bot.run(os.getenv('TOKEN')) # type: ignore
    logger.info("Shutting down...")