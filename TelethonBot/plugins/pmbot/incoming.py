from TelethonBot.plugins.pmbot.sql.users_sql import add_user_to_db
from TelethonBot.plugins.pmbot.sql.blacklist_sql import check_is_black_list
from telethon import events
from Telethon.plugins import SMEX_USER

# if incoming


@BotzHub.on(events.NewMessage(func=lambda e: e.is_private))
async def one_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if check_is_black_list(who):
        return
    if incoming.startswith("/"):
        pass
    elif who == SMEX_USER:
        return
    else:
        await event.get_sender()
        event.chat_id
        to = await event.forward_to(OWNER_ID)
        add_user_to_db(to.id, who, event.id)
