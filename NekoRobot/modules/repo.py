"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Awesome-Prince]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Awesome-Prince/NekoRobot-3 ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from telethon import Button

from NekoRobot import tbot
from NekoRobot.events import register

PHOTO = "https://te.legra.ph/file/f455ad70788ebcd93a709.jpg"


@register(pattern=("/repo"))
async def awake(event):
    NEKO = """
━━━━━━━━𝗞𝗜𝗞𝗢 𝗥𝗢𝗕𝗢𝗧━━━━━━━━
  👨‍💻 𝗞𝗜𝗞𝗢 𝗥𝗢𝗕𝗢𝗧 𝗦𝗢𝗨𝗥𝗖𝗘 👨‍💻

𝗛𝗘𝗥𝗘 𝗜𝗦 𝗧𝗛𝗘 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 𝗢𝗙
[𝗞𝗜𝗞𝗢 𝗥𝗢𝗕𝗢𝗧](https://t.me/KikoManagement_Robot) 𝗪𝗛𝗜𝗖𝗛 𝗛𝗘𝗟𝗣𝗦
[𝗞𝗜𝗞𝗢 𝗥𝗢𝗕𝗢𝗧](https://t.me/KikoManagement_Robot) 𝗙𝗢𝗥 𝗙𝗨𝗡𝗖𝗧𝗜𝗢𝗡𝗜𝗡𝗚
𝗣𝗥𝗢𝗣𝗘𝗥𝗟𝗬 𝗔𝗡𝗗 𝗘𝗙𝗙𝗘𝗖𝗧𝗜𝗩𝗘𝗟𝗬

━━━━━━━━𝗞𝗜𝗞𝗢 𝗥𝗢𝗕𝗢𝗧━━━━━━━━
Powered By:- @WCFnetwork

"""

    BUTTON = [
        [
            Button.url(" 𝗦𝗼𝘂𝗿𝗰𝗲 ", "https://t.me/Tera_Bf_hu_me"),
            Button.url(" 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ", "https://t.me/Kiko_Support"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
