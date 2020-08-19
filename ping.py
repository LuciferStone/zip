from datetime import datetime

from telethon import functions

from userbot.events import register


@register(outgoing=True, pattern="^.ping$")
async def pingme(event):

    start = datetime.now()
    pong = await event.respond("Pong!")
    end = datetime.now()
    duration = int((end - start).microseconds / 1000)
    await pong.edit("Pong!\n%sms" % (duration))