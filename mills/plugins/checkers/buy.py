"""
≛ <b>Commands Available</b> ≛

──────────────────────────
- <code>/buy<code>: Check Available plans for unlocking paid checker gates.
──────────────────────────

©<a href="https://t.me/BlackBincards">BlackBincards</a>
"""
import inspect
import io
import json
import os
import time
from fuzzywuzzy.process import extractOne
from telethon import utils
# from telethon import Button
from telethon.tl.custom import Button

from mills import BOT_PIC, client
from mills.decorators import bot_cmd


@bot_cmd(pattern="buy$")
async def _(m):
    text = f"""

┌──────────────────────────┐
    • Premium Plans •

◦ 5$ - Get access to all gates for 28 days.
◦ 10$ - Get access to all gates. for 70 days
◦ 20$ - Get access to all gates. for 200 days

○ Payment methods: Crypto, Binance

└──────────────────────────┘
"""
    buttons = [
        Button.url('Buy Now', 'https://t.me/PowerDefend'),
        Button.url('Black Bincards', 'https://t.me/BlackBincards'),
    ]
    await m.reply(text,buttons= buttons, file = BOT_PIC)