import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed
# import urllib.request
import re

load_dotenv()

bot = commands.Bot(command_prefix='W!')

@bot.event
async def on_ready():
    print('Discord bot logged in as ' + bot.user.name)
    await bot.change_presence(activity=discord.Game(name="guilded.gg/WiiLink24"))

@bot.event
async def on_message(ctx):
    if str(ctx.webhook_id) == re.findall("discord.com\/api\/webhooks\/([^\/]+)\/", os.getenv('DISCORD_WEBHOOK'))[0]:
        return
    if str(ctx.channel.id) != os.getenv('DISCORD_CHANNEL_ID'):
        return

    displayname = ctx.author.name

    try:
        if ctx.author.nick:
            displayname = ctx.author.nick + ' (' + ctx.author.name + ')'
    except:
        pass

    webhook = DiscordWebhook(url=os.getenv('GUILDED_WEBHOOK'), content='<' + displayname + '> ' + ctx.content)
    attachment_urls = []

    if ctx.attachments:
        for attachment in ctx.attachments:
        # When Guilded supports file uploads, we can use this. For now, we'll leave it there.
        #    req = urllib.request.Request(
        #        attachment.url,
        #        headers={'User-Agent':'DiscordBot (https://wiilink24.com, 1.0.0)'}
        #    )
        #    webhook.add_file(file=urllib.request.urlopen(req), filename=attachment.filename)
            attachment_urls.append(attachment.url)
        webhook = DiscordWebhook(url=os.getenv('GUILDED_WEBHOOK'), content='<' + displayname + '> ' + ctx.content + " " + " ".join(attachment_urls))

    response = webhook.execute()

bot.run(os.getenv('DISCORD_TOKEN'))