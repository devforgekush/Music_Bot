# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Audify import LOGGER, app, userbot
from Audify.core.call import Audify
from Audify.misc import sudo
from Audify.plugins import ALL_MODULES
from Audify.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
    try:
        await Audify.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Audify").warning(
            "\ud83d\udce2 No active voice chat found in log group. Bot will start without initial stream test."
        )  # Railway fix: Continue startup instead of exiting
    except:
        pass
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Audify.plugins" + all_module)
    LOGGER("Audify.plugins").info("✅ All modules successfully loaded. Audify is ready to serve 🎶")
    await userbot.start()
    await Audify.start()
    try:
        await Audify.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Audify").error(
            "📢 Please start a voice chat in your log group or linked channel!\n\n⚠️ Audify cannot stream without an active group call."
        )
        exit()
    except:
        pass
    await Audify.decorators()
    LOGGER("Audify").info(
        "🎧 Audify Music Bot started successfully.\n🛡️ Developed with passion by @i_am_alive_as_fumk 💻\nChannel: @alpha_dead4"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Audify").info("🛑 Audify Music Bot has stopped. See you soon! 👋")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
