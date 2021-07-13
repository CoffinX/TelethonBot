from .. import BotzHub
from TelethonBot.plugins.sql.checkuser_sql import get_all_users

@BotzHub.on("broadcast", is_args=True)
async def sedlyfsir(event):
   bot = BoztHub
   async with BotzHub.conversation("ShashankxD") as conv:
    msgtobroadcast = await BoztHub.send_message("**Ok Now Send Me The Message For Broadcast...!**")
    sed = await conv.get_response()
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            await BozHub.send_message(int(event.chat_id), sed)
        except Exception as e:
            error_count += 1
    sent_count = error_count - len(userstobc)
    await BoztHub.send_message(
        "ShashankxD",
        f"<b>Broadcast Done in <u>{sent_count}</u> Group/Users and I got <u>{error_count}</u> Error and Total Number Was <u>{len(userstobc)}</u></b>",
        parse_mode="HTML"
    )
    await BotzHub.send_message(Config.DUMB_CHAT, f"**#Broadcast\n\nYou BroadCasted A New Message.\nSent Count - {sent_count}**")
    await BotzHub.send_message(Config.DUMB_CHAT, sed)
