from .. import BotzHub

from telethon import event, client, buttons

fkx2 = [[custom.Button.inline("➕ Aʟʟ CᴏᴍᴍᴀᴅS ➕", data="all_cmds2")]]
fkx2 += [[custom.Button.inline("👥 Bᴀsɪᴄ Gʀᴏᴜᴘ CᴏᴍᴍᴀɴᴅS", data="BGC"),custom.Button.inline("🛠 Aᴅᴠᴀɴᴄᴇᴅ CᴏᴍᴍᴀɴᴅS", data="ADC")]]
fkx2 += [[custom.Button.inline("📖 Fᴜɴ Tᴏᴏʟs & ExᴛʀᴀS", data="FTAE"),custom.Button.inline("🔎 Iɴʟɪɴᴇ CᴏᴍᴍᴀɴᴅS", data="ICMD")]]
fkx2 += [[custom.Button.inline("« Bᴀᴄᴋ", data="full_bck")]]

omk += [[custom.Button.inline(">> Skem", data="skemh")]]
omk += [[custom.Button.inline(">> Ping", data="pingh")]]
omk += [[custom.Button.inline(">> Eval", data="evalh")]]
omk += [[custom.Button.inline(">> Broadcast", data="Broadcasth")]]

@BoztHub.on(event.NewMessage(pattern="/help"))
async def shashankop(event):
  await BotzHub.reply(event.chat_id, "Help menu of skemer bot", button=fkx2)

@BotzHub.on(events.callbackquery.CallbackQuery(data="all_cmd2"))
async def amll(event):
  await BotzHub.edit(event.chat_id, "Here is all skem commands", button=omk)
