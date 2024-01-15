from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS, CMD_HNDLR as hl
from telethon import events, Button


PythonHelp = f"☞ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖬𝖾𝗇𝗎\n\n⧉  𝖳𝖺𝗉 𝗈𝗇 𝖡𝖾𝗅𝗈𝗐 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖳𝗈 𝖫𝖾𝖺𝗋𝗇 𝖬𝗈𝗋𝖾📄 𝖠𝖻𝗈𝗎𝗍 𝖡𝗈𝗍 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌."


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  "https://telegra.ph/file/46b2748409590033743a4.jpg",
                                  caption=PythonHelp,
                                  buttons=[
           [
            Button.inline("👻 sᴘᴀᴍ 👻", data="spam"),
            Button.inline("☠️ ʀᴀɪᴅ ☠️", data="raid"),
           ],
           [
            Button.inline("🕷 ᴍᴏʀᴇ 🕷", data="extra"),
           ],
           ],
           )


extra_msg = f"""
☞ 𝖬𝗈𝗋𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :

✧𝖡𝗈𝗍 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :
  1) {hl}ping ~ 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖠𝗅𝗂𝗏𝖾 𝗈𝗋 𝖣𝖾𝖺𝖽.
  2) {hl}reboot ~ 𝖳𝗈 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝗍𝗁𝖾 𝖡𝗈𝗍.

✧𝖤𝖼𝗁𝗈 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :
  1) {hl}echo ~ 𝖳𝗈 𝖲𝗍𝖺𝗋𝗍 𝖤𝖼𝗁𝗈.
  2) {hl}rmecho ~ 𝖳𝗈 𝖲𝗍𝗈𝗉 𝖤𝖼𝗁𝗈.

✧𝖫𝖾𝖺𝗏𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :
  1) {hl}leave ~ 𝖳𝗈 𝖫𝖾𝖺𝗏𝖾 𝖦𝗋𝗈𝗎𝗉/𝖢𝗁𝖺𝗇𝗇𝖾𝗅.

✧𝖮𝗐𝗇𝖾𝗋 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :
  1) {hl}sudo ~ 𝖥𝗈𝗋 𝖠𝖽𝖽𝗂𝗇𝗀 𝖲𝗎𝖽𝗈 𝖴𝗌𝖾𝗋𝗌.
  2) {hl}logs ~ 𝖥𝗈𝗋 𝖡𝗈𝗍 𝖫𝗈𝗀𝗌.
"""

                 
raid_msg = f"""
☞ 𝖱𝖺𝗂𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :

✧ 𝖱𝖺𝗂𝖽 :
  1) {hl}raid <count><username/reply> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖠𝖻𝗎𝗌𝗂𝗏𝖾 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖠𝗇𝗒 𝖴𝗌𝖾𝗋.

✧ 𝖱𝖾𝗉𝗅𝗒𝗋𝖺𝗂𝖽 :
  1) {hl}rraid <count><username/reply> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖠𝖻𝗎𝗌𝗂𝗏𝖾 𝖱𝖾𝗉𝗅𝗒 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖠𝗇𝗒 𝖴𝗌𝖾𝗋.
  2) {hl}drraid <count><username/reply> ~ 𝖲𝗍𝗈𝗉𝗌 𝖠𝖻𝗎𝗌𝗂𝗏𝖾 𝖱𝖾𝗉𝗅𝗒 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖴𝗌𝖾𝗋.

✧ 𝖫𝗈𝗏𝖾 𝖱𝖺𝗂𝖽 :
  1) {hl}mraid <count><username/reply> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖫𝗈𝗏𝖾 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖠𝗇𝗒 𝖴𝗌𝖾𝗋.

✧ 𝖲𝗁𝖺𝗒𝖺𝗋𝗂 𝖱𝖺𝗂𝖽 :
  1) {hl}sraid <count><username/reply> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗁𝖺𝗒𝖺𝗋𝗂 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖠𝗇𝗒 𝖴𝗌𝖾𝗋.

✧ 𝖫𝖾𝗍𝗍𝖾𝗋 𝖱𝖺𝗂𝖽 : 
  1) {hl}craid <count><username/reply> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖱𝖺𝗇𝖽𝗈𝗆 𝖱𝖾𝗉𝖾𝖺𝗍𝖾𝖽 𝖫𝖾𝗍𝗍𝖾𝗋𝗌 𝖱𝖺𝗂𝖽 𝗈𝗇 𝖠𝗇𝗒 𝖴𝗌𝖾𝗋.
"""

spam_msg = f"""
☞ 𝖲𝗉𝖺𝗆 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :

✧ 𝖲𝗉𝖺𝗆 :
  1) {hl}spam <count><message to spam> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝗀𝗂𝗏𝖾𝗇 𝖬𝖾𝗌𝗌𝖺𝗀𝖾.

✧ 𝖯𝗈𝗋𝗇 𝖲𝗉𝖺𝗆 :
  1) {hl}pspam <count> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝖯𝗈𝗋𝗇𝗈𝗋𝖺𝗉𝗁𝗒 𝖢𝗈𝗇𝗍𝖾𝗇𝗍𝗌.

✧ 𝖧𝖺𝗇𝗀 𝖲𝗉𝖺𝗆 :
  1) {hl}hang <count> ~ 𝖲𝗍𝖺𝗋𝗍𝗌 𝖲𝗉𝖺𝗆𝗆𝗂𝗇𝗀 𝖣𝖾𝗏𝗂𝖼𝖾 𝖥𝗋𝖾𝖾𝗓𝗂𝗇𝗀 𝖬𝖾𝗌𝗌𝖺𝗀𝖾.

# 𝖭𝗈𝗍𝖾 :- 
𝖸𝗈𝗎 𝖼𝖺𝗇 𝖺𝗅𝗌𝗈 𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝗌𝗌𝖺𝗀𝖾 𝗂𝖿 𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗌𝗉𝖺𝗆 𝗈𝗇 𝗋𝖾𝗉𝗅𝗒 𝗈𝖿 𝗍𝗁𝖺𝗍 𝗆𝖾𝗌𝗌𝖺𝗀𝖾.
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            PythonHelp,
            buttons=[
           [
            Button.inline("👻 sᴘᴀᴍ 👻", data="spam"),
            Button.inline("☠️ ʀᴀɪᴅ ☠️", data="raid"),
           ],
           [
            Button.inline("🕷 ᴍᴏʀᴇ 🕷", data="extra"),
           ],
           ],
        )           
   else:
        await event.answer("Visit @TitanXSupport for Sudo to Start Spamming.", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(spam_msg,
            buttons=[[Button.inline("🔙", data="help_back"),],],
            ) 
   else:
        await event.answer("Visit @TitanXSupport for Sudo to Start Spamming.", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("🔙", data="help_back"),],],
            )  
     else:
        await event.answer("Visit @TitanXSupport for Sudo to Start Spamming.", cache_time=0, alert=True)


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("🔙", data="help_back"),],],
            )
   else:
        await event.answer("Visit @TitanXSupport for Sudo to Start Spamming.", cache_time=0, alert=True)
