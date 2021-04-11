import discord
from .colors import get_color

def embed(title, text):
  return discord.Embed(
    color = get_color(),
    title = title,
    description = text
  )