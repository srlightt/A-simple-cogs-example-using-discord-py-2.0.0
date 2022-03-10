import os
import discord
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".")


bot = Bot()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename}")
        except Exception as e:
            print(f"Failed to load {filename}")
            print(f"[ERROR] {e}")


async def startup():
    await bot.wait_until_ready()
    await bot.tree.sync() # If you want to define specific guilds, pass a discord object with id (Currently, this is global)
    print('Sucessfully synced applications commands')
    print(f'Connected as {bot.user}')


bot.loop.create_task(startup())

bot.run('token')
