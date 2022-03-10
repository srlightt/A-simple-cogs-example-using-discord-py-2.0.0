import discord
from discord.ext import commands
from discord import app_commands


class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    #@app_commands.guilds() If you want to define specific guilds (Currently, this is global)
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message('cogs \o/')


def setup(bot):
    bot.add_cog(test(bot))
