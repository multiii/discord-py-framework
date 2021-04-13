import os
import random
import yaml

from discord.ext import commands, tasks

from templates.status import status

with open("config.yaml", "r") as file:
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

for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    client.load_extension(f"cogs.{file[:-3]}")



client.run(token)