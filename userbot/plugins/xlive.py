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
from . import StartTime, catub, catversion, hmention

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
    """
    error = "You rise with the moon. I rise with the sun."
    if error in quote:
        try:
            response = requests.get(api_url).json()
        except Exception:
            response = None
    """
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
        cat_caption = f"<b><i>{ALIVE_TEXT}</i></b>\n\n"
        cat_caption += f"<b>{EMOJI} 👑 Owner : {hmention}</b>\n"
        cat_caption += f"<b>{EMOJI} 😪 Not Slept For :</b> <code>{uptime}</code>\n"
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        cat_caption += f"<b>{EMOJI} 🥱 Lazyness :</b> <code>{ms} ms</code>\n"
        cat_caption += f"<b>{EMOJI} 🐱 Evolution :</b> <code>{catversion}</code>\n"
        cat_caption += f"<b>{EMOJI} 💻 Storage :</b> <code>{check_sgnirts}</code>\n\n"
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id, parse_mode = "html"
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"<b>Media Value Error!!</b>\n<i>Change the link by </i><code>.setdv</code>\n\n<b><i>Can't get media from this link :-</b></i> <code>{PIC}</code>",
            )
    else:
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await edit_or_reply(
            event,
            f"<b><i>{ALIVE_TEXT}</i></b>\n\n"
            f"<b>✘ 👑 Owner : {hmention}</b>\n"
            f"<b>{EMOJI} 😪 Not Slept For :</b> <code>{uptime}</code>\n"
            f"<b>{EMOJI} 🥱 Lazyness :</b> <code>{ms} ms</code>\n"
            f"<b>{EMOJI} 🐱 Evolution :</b> <code>{catversion}</code>\n"
            f"<b>{EMOJI} 💻 Storage :</b> <code>{check_sgnirts}</code>\n\n"
        )


