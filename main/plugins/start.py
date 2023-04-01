import os
import requests
from .. import bot as Drone, AUTH
from telethon import events, Button
from datetime import datetime
from time import time

S = '/' + 's' + 't' + 'a' + 'r' + 't'

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("Lepin", url="t.me/tuhanfwb")]])
                              

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Kirimi saya gambar apa pun untuk thumbnail sebagai `balas` untuk pesan ini.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Gambar mini sementara disimpan!")


@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Mencoba.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Dihapus!')
    except Exception:
        await event.edit("No thumbnail saved.")                        


@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Kirimi saya Tautan pesan apa pun untuk mengkloningnya di sini, Untuk pesan saluran pribadi, kirim tautan undangan terlebih dahulu."
    await start_srb(event, text)
    

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/ping'))
async def ping_pong(event):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await event.reply("Pinging...")
    delta_ping = time() - start
    await m_reply.edit(
        "**PONG!!**🏓 \n"
        f"**• Pinger -** `{delta_ping * 1000:.3f}ms`\n"
        f"**• Uptime -** `{uptime}`\n"
    )


@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/uptime'))
async def get_uptime(event):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await event.reply(
        "🤖 **Bot Status:**\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **Start Time:** `{START_TIME_ISO}`"
    )


@Drone.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    await event.reply("**Untuk konten Saluran Publik yang Dibatasi.**\nCukup kirim tautan Posting Anda, saya akan memberi Anda posting itu tanpa Mengunduh.\n\n**Untuk konten Saluran Pribadi yang Dibatasi.**\nPertama-tama kirimkan saya tautan undangan Saluran sehingga saya dapat bergabung dengan saluran Anda setelah itu kirimkan saya tautan kiriman dari Saluran Anda yang dibatasi untuk mendapatkan kiriman itu.") 
