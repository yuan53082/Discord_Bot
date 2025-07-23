import discord

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True  # 如需使用名稱判斷，要開啟這個

client = discord.Client(intents=intents)

# 指定目標使用者（方式一）：使用者的 Discord ID（最精確）
TARGET_USER_IDS = [
    1131866466648592455,  # 換成你要監控的使用者 ID（可多個）
    457207903351210035,
    942692337333719050,
    539449104456089609,
    1023381704687231016
]

# 指定關鍵字
KEYWORDS = ["可愛"]

# 關鍵字對應替換字典
REPLACEMENTS = {
    "小 可 愛": "小 笨 蛋",
    "小可愛": "小笨蛋",
    "好可愛": "大笨蛋",
    "可愛": "笨蛋",
    "小天使": "臭抹布",
    "天使": "抹布"
}

@client.event
async def on_ready():
    print(f"機器人已登入：{client.user}")

@client.event
async def on_ready():
    print(f"機器人已登入：{client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id not in TARGET_USER_IDS:
        return

    # 判斷訊息中是否有任一關鍵字
    if any(k in message.content for k in REPLACEMENTS.keys()):
        new_content = message.content
        # 逐個關鍵字替換
        for k, v in REPLACEMENTS.items():
            new_content = new_content.replace(k, v)

        try:
            await message.delete()
            print(f"刪除訊息：{message.content}")
            await message.channel.send(new_content)
        except discord.Forbidden:
            print("⚠️ 權限不足，無法刪除訊息")
        except discord.HTTPException as e:
            print(f"⚠️ 刪除失敗：{e}")

# 替換為你自己的 Token
client.run("MTM5NzQ4OTI2MDU0MTUwOTY5Mg.GDfxZJ.Jmbet-37KCaEHKxHjMOVKx0h_rRoTu6dsAW154")
