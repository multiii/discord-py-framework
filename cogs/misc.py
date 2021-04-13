from discord.ext import commands
from templates.complete_embed import embed

class Misc(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(name = 'help', description = 'Display the help menu', aliases = ("h",))
  async def help(self, ctx):
    desc = ""

    for cog in list(self.client.cogs.keys()):
      desc += f"**{cog}**\n"

      for command in self.client.get_cog(cog.lower().capitalize()).walk_commands():
        desc += f"**`{command.name}`** - {command.description}\n"

      desc += "\n"

    await ctx.send(embed = embed('Help Menu', desc, ctx.author))

  @commands.command(name = 'test', description = 'Testing the bot', aliases = ("t",))
  async def test(self, ctx):
    await ctx.send(embed = embed('Testing', '**Test Successful**', ctx.author))

def setup(client):
  client.add_cog(Misc(client))