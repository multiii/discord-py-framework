import random
import yaml

from discord.ext import commands, tasks

from templates.status import status
from templates import complete_embed

with open("config.json", "r") as file:
  f = yaml.safe_load(file)
  prefix = f["prefix"]
  token = f["token"]

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

# Set Status
async def set_status():
  options = status(prefix, client)
  option = random.choice(options)

  await client.change_presence(activity=option)

@client.event
async def on_ready():
  print("Ready!")
  loop.start()

@client.event
async def on_command_error(ctx, error):
  if not isinstance(error, commands.CommandNotFound):
    await ctx.send(f'{ctx.author.mention}, There was an error trying to execute that command!')
  raise error

@tasks.loop(minutes=50)
async def loop():
  await set_status()

@client.command(name = 'help', description = 'Display the help menu')
async def help(ctx):
  desc = ""
  for command in client.commands:
    desc += f"**`{command.name}`** - {command.description}\n"

  await ctx.send(embed = complete_embed.embed('Help Menu', desc, ctx.author))

@client.command(name = 'test', description = 'Testing the bot')
async def test(ctx):
  await ctx.send(embed = complete_embed.embed('Testing', '**Test Successful**', ctx.author))

client.run(token)