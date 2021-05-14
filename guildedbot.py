import guilded
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook

load_dotenv()

bot = guilded.Bot(command_prefix='!', owner_id='GmjJZnMm')

@bot.event()
async def on_ready():
    print('Guilded bot logged in as ' + bot.user.name)

@bot.event()
async def on_message(ctx):
    if ctx.author.name == 'Gil':
        return
    cleanedcontent = ctx.content.replace('@everyone', '@​everyone')
    webhook = DiscordWebhook(url=os.getenv('DISCORD_WEBHOOK'), content=cleanedcontent, username=ctx.author.name, avatar_url=ctx.author.avatar_url)
    response = webhook.execute()

bot.run(os.getenv('GUILDED_EMAIL'), os.getenv('GUILDED_PASSWORD'))