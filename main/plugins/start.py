#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Kirimi saya gambar apa saja untuk thumbnail sebagai `balas` untuk pesan ini.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("Tidak ada media di temukan.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("Tidak menemukan gambar.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Mencoba.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail tersimpan!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Drone = event.client            
    await event.edit('Mencoba.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Terhapus!')
    except Exception:
        await event.edit("Tidak ada thumbnail tersimpan.")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "Kirimi saya Tautan pesan apa pun untuk mengkloningnya di sini, Untuk pesan saluran pribadi, kirim tautan undangan terlebih dahulu.\n\n**Owner:**@tuhanalamsemesta"
    await start_srb(event, text)
    
