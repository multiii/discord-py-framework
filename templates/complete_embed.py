import discord
from .colors import get_color

def embed(title, text, user, image_url = None):
  embed = discord.Embed(
      color = get_color(),
      title = title,
      description = text
  )

  embed.set_footer(text = f"Requested by {user.name}#{user.discriminator}", icon_url = user.avatar_url)
  
  if image_url != None:
    embed.set_image(url = image_url)

  return embed