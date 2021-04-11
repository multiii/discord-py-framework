import discord
from .colors import get_color

def embed(text):
  return discord.Embed(
    color = get_color(),
    description = text
  )