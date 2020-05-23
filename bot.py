from urllib.request import urlopen
import random

import discord
from discord.ext import commands
import json

BotToken = ''

bot = commands.Bot(command_prefix='')


@bot.command(pass_context=True)
async def get_post(ctx):
    html_doc = urlopen(
        "http://api.vk.com/method/wall.get?v=5.3&domain=nashanus&count=20&access_token=").read()
    JSON = json.loads(html_doc)
    response = JSON['response']
    items = response['items']
    i = random.randint(0, len(items) - 1)
    embed = discord.Embed(
        title='Открыть в ВК',
        url="https://vk.com/nashanus?w=wall" + str(items[i]['from_id']) + '_' + str(items[i]['id']),
        description=items[i]['text']
    )

    try:
        attachments = items[i]['attachments'][0]
        print(attachments)
        if attachments['type'] == 'photo':
            try:
                photos = attachments['photo']
                photo = photos['photo_604']
            except:
                photo = str(attachments)[str(attachments).find('http'):str(attachments).find('.jpg') + 4]
            print(photo)
            embed.set_image(url=photo)
    except:
        print()
    await ctx.send(embed=embed)


bot.run(BotToken)
