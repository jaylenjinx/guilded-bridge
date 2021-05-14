from discord.ext import commands
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed
import urllib.request

load_dotenv()

bot = commands.Bot(command_prefix='W!')

@bot.event
async def on_ready():
    print('Discord bot logged in as ' + bot.user.name)

@bot.event
async def on_message(ctx):
    if ctx.webhook_id:
        return
    if str(ctx.channel.id) != os.getenv('DISCORD_CHANNEL_ID'):
        return

    webhook = DiscordWebhook(url=os.getenv('GUILDED_WEBHOOK'), content='<' + ctx.author.name + '> ' + ctx.content)
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
        webhook = DiscordWebhook(url=os.getenv('GUILDED_WEBHOOK'), content='<' + ctx.author.name + '> ' + ctx.content + " " + " ".join(attachment_urls))

    response = webhook.execute()

bot.run(os.getenv('DISCORD_TOKEN'))