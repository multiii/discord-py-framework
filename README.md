# discord-py-framework

## Introduction

 A simple discord.py boiler-plate to help bot developers code faster.

## Code Samples

 Edit ``config.yaml`` as per your needs

 ```yaml
  prefix: +
  token: your token
 ```

 Create a new file in the cogs folder:
```py
#your_cog.py
from discord.ext import commands

class YourCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "your_command_name",
  description = "Command Description", aliases = ("your_command_alias",))
  async def _one(self, ctx):
    #Your Code here
    await ctx.send("Hi!")

def setup(client):
  client.add_cog(YourCog(client))
```

 Using the embed system:
```py
#your_cog.py
from templates.complete_embed import embed
#Embeds available: complete_embed, standard_embed, title_embed
from discord.ext import commands

class YourCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name = "your_command_name",
  description = "Command Description", aliases = ("your_command_alias",))
  async def _one(self, ctx):
    #Your Code here
    await ctx.send(embed = embed('Title', 'Description', ctx.author))

def setup(client):
  client.add_cog(YourCog(client))
```

> * complete_embed Syntax:
```py
await ctx.send(embed = embed('Title', 'Description', message.author, 'image_url'));
```

> * standard_embed Syntax:
```py
await ctx.send(embed = embed('Title'));
```

> * title_embed Syntax:
```py
await ctx.send(embed = embed('Title', 'Description'));
```

## Installation

* Clone the repo:
```
git clone https://github.com/multi-yt76/discord-py-framework
```
 