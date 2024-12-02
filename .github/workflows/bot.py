import discord
import random
from discord.ext import tasks
from datetime import datetime

client = discord.Client()

# アバター画像のURLリストを設定
avatars = [
    'IMG_1100.JPG',
    'IMG_1101.JPG',
    'IMG_1103.JPG',
    'IMG_1105.JPG',
    'IMG_1106.JPG',
    'IMG_1109.JPG',
    'IMG_1110.JPG'
]

# 前日のアバターを保持する変数
previous_avatar = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    change_avatar.start()

@tasks.loop(hours=24)
async def change_avatar():
    global previous_avatar

    # 前日のアバターを除外したリストを作成
    available_avatars = [avatar for avatar in avatars if avatar != previous_avatar]

    # ランダムにアバターを選択
    new_avatar = random.choice(available_avatars)

    # アバターを変更
    with open(new_avatar, 'rb') as avatar:
        await client.user.edit(avatar=avatar.read())

    # 前日のアバターを更新
    previous_avatar = new_avatar

client.run(TOKEN)
