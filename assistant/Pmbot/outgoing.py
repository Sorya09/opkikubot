# opkikubot - UserBot
# Copyright (C) 2020 opkikubot
#
# This file is a part of < https://github.com/opgohil/opkikubot/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/opgohil/opkikubot/blob/main/LICENSE/>.



from telethon import events

from . import *

# outgoing


@asst.on(events.NewMessage(func=lambda e: e.is_private))
async def on_out_mssg(event):
    x = await event.get_reply_message()
    if x is None:
        return
    who = event.sender_id
    if who == OWNER_ID:
        if event.text.startswith("/"):
            return
        to_user = udB.get(str(x.id))
        if event.media:
            if event.text:
                await asst.send_file(int(to_user), event.media, caption=event.text)
            else:
                await asst.send_file(int(to_user), event.media)
        else:
            await asst.send_message(int(to_user), event.text)