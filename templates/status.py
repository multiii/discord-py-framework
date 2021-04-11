import discord

def status(prefix, client):
  return [
      discord.Activity(type = discord.ActivityType.playing, name = f"{prefix}help"),
      discord.Activity(type = discord.ActivityType.listening, name = f"{prefix}help"),
      discord.Activity(type = discord.ActivityType.watching, name = f"{len(client.guilds)} servers")
  ]
