import discord
from discord.ext import commands
from discord import app_commands


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    #@app_commands.guilds() If you want to define specific guilds (Currently, this is global)
    async def test(self, interaction: discord.Interaction):
        """command description"""
        await interaction.response.send_message('cogs \o/')


async def setup(bot): # set async function
    await bot.add_cog(Test(bot)) # Use await
