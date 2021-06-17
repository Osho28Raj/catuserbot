import random
import requests
import re
import time
from platform import python_version
from datetime import datetime
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

plugin_category = "utils"


start = datetime.now()
@catub.cat_cmd(
    pattern="xlive$",
    command=("xlive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}xlive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)

    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    #================================================
    # credit taking time😂
    # random anime quote by [http://t.me/o_s_h_o_r_a_j]
    api_url = f"https://animechan.vercel.app/api/random"
    try:
        response = requests.get(api_url).json()
    except Exception:
        response = None
    quote = response["quote"]
    error = "You rise with the moon. I rise with the sun."
    if error in quote:
        try:
            response = requests.get(api_url).json()
        except Exception:
            response = None
    quote = response["quote"]
    name = response["character"]
    ANIME_QUOTE = f"{quote}\n                    -{name}"
    #================================================
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✘"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ANIME_QUOTE
    CAT_IMG = gvarstatus("ALIVE_PIC")
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption = f"**__{ALIVE_TEXT}__**\n\n"
        cat_caption += f"**{EMOJI} 👑 Owner : {mention}**\n"
        cat_caption += f"**{EMOJI} 😪 Not Slept For :** `{uptime}`\n"
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        cat_caption += f"**{EMOJI} 🥱 Lazyness :** `{ms} ms`\n"
        cat_caption += f"**{EMOJI} 🐱 Evolution :** `{catversion}`\n"
        cat_caption += f"**{EMOJI} 💻 Storage :** `{check_sgnirts}`\n\n"
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await edit_or_reply(
            event,
            f"**{ALIVE_TEXT}**\n\n"
            f"**✘ 👑 Owner : {mention}**\n"
            f"**{EMOJI} 😪 Not Slept For :** `{uptime}`\n"
            f"**{EMOJI} 🥱 Lazyness :** `{ms} ms`\n"
            f"**{EMOJI} 🐱 Evolution :** `{catversion}`\n"
            f"**{EMOJI} 💻 Storage :** `{check_sgnirts}`\n\n"
        )


