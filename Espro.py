import os
import pyrogram
from pyrogram import Client

api_id = 19181985
api_hash = "a2b23ca3a1c9b5dab4bf42dda7de4e79"

try:
   os.remove("Espro.session")
except:
     pass
with Client("Espro", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [𝐄𝐬𝐩𝐫𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/EsproSupport) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("EsproSupport")
        app.join_chat("EsproUpdate")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("Espro.session")

