from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from TitanSpam.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("🕸 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ 🕸", url=f"https://t.me/{BotId}}?startgroup=true")
        ],
        [
        Button.url("🛠 ᴄᴏᴍᴍᴀɴᴅs 🛠", data="help_back")
        ],
        [
        Button.url("🔎 sᴜᴘᴘᴏʀᴛ 🔍", "https://t.me/TitanXSupport"),
        Button.url("🏴‍☠ ɴᴇᴛᴡᴏʀᴋ 🏴‍☠", "https://t.me/TitanNetwrk")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        TitanBot = await event.client.get_me()
        BotName = TitanBot.first_name
        BotId = TitanBot.id
        TEXT = f"𝐻𝑒𝑦 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n๏ Ｍʏsᴇʟғ [{BotName}](tg://user?id={BotId})​ !\n"
        TEXT += f"⧉ 𝖠ɴ 𝖠ᴅᴠᴀɴᴄᴇ 🔍, 𝖥ᴀꜱᴛ⚡️& 🦾𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖲𝗉𝖺𝗆 𝖡𝗈𝗍👨‍💻 𝗐𝗂𝗍𝗁 𝖢ᴏᴏʟ 𝖥ᴇᴀᴛᴜʀᴇs.\n"
        TEXT += f"⧉ 𝖨𝗍 𝗁𝖺𝗌 𝗆𝖺𝗇𝗒👻 𝗍𝗒𝗉𝖾𝗌 𝗈𝖿 𝖲𝗉𝖺𝗆☠️ 𝖬𝗈𝖽𝗎𝗅𝖾𝗌 𝖫𝗂𝗄𝖾 𝖫𝗈𝗏𝖾❤️ 𝗌𝗉𝖺𝗆, 𝖲𝗁𝖺𝗒𝖺𝗋𝗂😜 𝖲𝗉𝖺𝗆, 𝖱𝖺𝗂𝖽☠️, 𝖯𝗈𝗋𝗇 𝖲𝗉𝖺𝗆😱, 𝖱𝖾𝗉𝗅𝗒 𝖱𝖺𝗂𝖽💀 𝖾.𝗍.𝖼.\n"
        TEXT += f"⧉  𝖳𝖺𝗉 𝗈𝗇 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖫𝖾𝖺𝗋𝗇 𝖬𝗈𝗋𝖾📄 𝖠𝖻𝗈𝗎𝗍 𝗁𝗈𝗐 𝗍𝗈 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖡𝗈𝗍."
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/46b2748409590033743a4.jpg",
                caption=TEXT, 
                buttons=PythonButton)
