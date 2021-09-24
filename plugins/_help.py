# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from pyUltroid.dB._core import HELP, LIST
from telethon.errors.rpcerrorlist import (
    BotInlineDisabledError,
    BotMethodInvalidError,
    BotResponseTimeoutError,
)
from telethon.tl.custom import Button

from . import *

C_PIC = udB.get("INLINE_PIC")
_file_to_replace = C_PIC or "resources/extras/inline.jpg"

_main_help_menu = [
    [
        Button.inline("• Plugins", data="hrrrr"),
        Button.inline("• Addons", data="frrr"),
    ],
    [
        Button.inline("••Voice Chat", data="vc_helper"),
        Button.inline("Inline Plugins••", data="inlone"),
    ],
    [
        Button.inline("⚙️ Owner Tools", data="ownr"),
        Button.url("Settings ⚙️", url=f"https://t.me/{asst.me.username}?start=set"),
    ],
    [Button.inline("••Cʟᴏꜱᴇ••", data="close")],
]


@ultroid_cmd(pattern="help ?(.*)")
async def _help(ult):
    plug = ult.pattern_match.group(1)
    if plug:
        try:
            if plug in HELP["Official"]:
                output = f"**Plugin** - `{plug}`\n"
                for i in HELP["Official"][plug]:
                    output += i
                output += "\n© @TeamUltroid"
                await eor(ult, output)
            elif plug in HELP["Addons"]:
                kk = f"Plugin Name-{plug}\n\n✘ Commands Available -\n\n"
                kk += str(HELP["Addons"][plug])
                await eor(ult, kk)
            elif plug in HELP["VCBot"]:
                kk = f"Plugin Name-{plug}\n\n✘ Commands Available -\n\n"
                kk += str(HELP["VCBot"][plug])
                await eor(ult, kk)
            else:
                try:
                    x = f"Plugin Name-{plug}\n\n✘ Commands Available -\n\n"
                    for d in LIST[plug]:
                        x += HNDLR + d
                        x += "\n"
                    x += "\n© @TeamUltroid"
                    await eor(ult, x)
                except BaseException:
                    await eor(ult, get_string("help_1").format(plug), time=5)
        except BaseException:
            await eor(ult, "Error 🤔 occured.")
    else:
        tgbot = asst.me.username
        try:
            results = await ult.client.inline_query(tgbot, "ultd")
        except BotMethodInvalidError:
            z = []
            for x in LIST.values():
                for y in x:
                    z.append(y)
            cmd = len(z) + 10
            if udB.get("MANAGER") and udB.get("DUAL_HNDLR") == "/":
                _main_help_menu[2:3] = [[Button.inline("• Manager Help •", "mngbtn")]]
            return await ult.reply(
                get_string("inline_4").format(
                    OWNER_NAME,
                    len(HELP["Official"]) - 5,
                    len(HELP["Addons"] if "Addons" in HELP else []),
                    cmd,
                ),
                file=_file_to_replace,
                buttons=_main_help_menu,
            )
        except BotResponseTimeoutError:
            return await eor(
                ult,
                get_string("help_2").format(HNDLR),
            )
        except BotInlineDisabledError:
            return await eor(ult, get_string("help_3"))
        await results[0].click(ult.chat_id, reply_to=ult.reply_to_msg_id, hide_via=True)
        await ult.delete()
