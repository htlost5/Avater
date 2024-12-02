import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = 'YOUR_BOT_TOKEN'
client = discord.Client()

# 曜日ごとのアバター画像のURLを設定
avatars = {
    0: 'url_for_sunday_avatar',
    1: 'url_for_monday_avatar',
    2: 'url_for_tuesday_avatar',
    3: 'url_for_wednesday_avatar',
    4: 'url_for_thursday_avatar',
    5: 'url_for_friday_avatar',
    6: 'url_for_saturday_avatar'
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    change_avatar.start()

@tasks.loop(hours=24)
async def change_avatar():
    now = datetime.now()
    day_of_week = now.weekday()  # 0=月曜日, 6=日曜日
    avatar_url = avatars[day_of_week]
    with open(avatar_url, 'rb') as avatar:
        await client.user.edit(avatar=avatar.read())

client.run(TOKEN)
