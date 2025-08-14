import discord
import random
import os

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# 自訂使用者名稱
USER_NAMES = {
    981937557640183858: "股東",
    587630018679537679: "投桃",
    1023381704687231016: "白桃",
    653087138073804861: "富婆",
    1023545131636359198: "涵吉",
    574633631947948042: "草莓",
    1275020381509521480: "D姐",
    558663120193847314: "桃桃",
    615182376124940289: "微微",
    1354192509521362975: "羽子",
    632090332909010974: "兔桃",
    395205143299358721: "逆風",
    942692337333719050: "鏡鏡",
    539449104456089609: "默默",
    539826100478672896: "莫奇",
    1131866466648592455: "麵茶",
    475299382426730498: "神婆",
    860442441382363148: "Ann",
}

# 感謝回覆（需要名字）
REPLIES_WITH_NAME = [
    "真客氣",
    "不用客氣",
    "不用客氣啦",
    "您太客氣了",
]

# 感謝回覆（不需要名字）
REPLIES_NO_NAME = [
    "由我來接受你的感謝",
    "You are welcome啦",
    "你怎麼那麼客氣",
    "不用謝 都是自己人",
    "地獄沒有在謝謝的",
]

# 感謝關鍵字
KEYWORDS = ["謝","謝謝", "多謝", "多蝦", "多瞎",
            "感謝", "乾蝦", "乾蝦", "甘蝦", "甘瞎", 
            "感恩", "乾溫", "甘溫", 
            "3q", "thank", "thank you", "thx", "tks",
            "阿哩嘎多", "阿哩阿多", "Danke", "Merci", "Gracias", "Grazie", "ありがとう",
            "謝天謝地", "謝主隆恩"]

# 感謝黑名單
BLACKLIST_PHRASES = ["感謝涵", "感謝祭", "不謝", "不用謝", "不感謝", "不謝謝"]

# 錯誤回覆（不需要名字）
WRONG_REPLIES = [
    "那你錯哪了？", 
    "你還知道你錯了？",
    "錯幾次了？自己算算",
    "你沒錯 是我錯了",
]

# 錯誤關鍵字
WRONG_KEYWORDS = ["錯了", "搞錯", "有錯", "我的錯",
                  "抱歉", "拍謝", "對不起",
                  "ごめん", "すみません",
                  "sorry", "sor", "my bad"]

# 錯誤黑名單
WRONG_BLACKLIST = ["不錯", "你錯", "錯過", "錯付", "錯開"]

@client.event
async def on_ready():
    print(f"✅ 機器人已登入：{client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content_lower = message.content.lower()

    # 優先判斷錯誤類型
    if any(k in content_lower for k in WRONG_KEYWORDS) and not any(b in content_lower for b in WRONG_BLACKLIST):
        reply = random.choice(WRONG_REPLIES)
        await message.reply(reply, mention_author=False)
        return

    # 再判斷感謝類型
    if any(k in content_lower for k in KEYWORDS) and not any(b in content_lower for b in BLACKLIST_PHRASES):
        if random.random() < 0.5:
            reply = random.choice(REPLIES_WITH_NAME)
            user_name = USER_NAMES.get(message.author.id, message.author.display_name)
            full_reply = f"{user_name} {reply}"
        else:
            full_reply = random.choice(REPLIES_NO_NAME)

        await message.reply(full_reply, mention_author=True)
        return
        
# 替換為你自己的 Token
client.run(TOKEN)
