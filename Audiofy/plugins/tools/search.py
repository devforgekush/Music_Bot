# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

from traceback import format_exc
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.stackoverflow import Search as StackSearch
from search_engine_parser.core.exceptions import NoResultsFound, NoResultsOrTrafficError

from Audify import app

# Initialize search engines
gsearch = GoogleSearch()
stsearch = StackSearch()


def build_keyboard(results):
    buttons = []
    for result in results[:5]:
        title = result.get("titles", "Result")
        url = result.get("links", "#")
        buttons.append([InlineKeyboardButton(text=title, url=url)])

    buttons.append([
        InlineKeyboardButton("❌ Close", callback_data="close")
    ])
    return InlineKeyboardMarkup(buttons)


@app.on_message(filters.command("google"))
async def search_google(app, msg: Message):
    query = msg.text.split(None, 1)
    if len(query) == 1:
        return await msg.reply_text("🔍 Please provide something to search.")
    
    wait_msg = await msg.reply_text("🔎 Searching Google...")
    try:
        results = await gsearch.async_search(query[1])
        keyboard = build_keyboard(results)
        await wait_msg.delete()
        await msg.reply_text(
            f"🔗 Here are the top results for: **{query[1].title()}**",
            reply_markup=keyboard
        )
    except NoResultsFound:
        await wait_msg.delete()
        await msg.reply_text("❌ No results found for your query.")
    except NoResultsOrTrafficError:
        await wait_msg.delete()
        await msg.reply_text("🚫 Google temporarily blocked traffic. Try again later.")
    except Exception as e:
        await wait_msg.delete()
        await msg.reply_text("⚠️ Something went wrong while searching. Try again later.")
        print(f"[ERROR - Google Search]: {e}\n{format_exc()}")


@app.on_message(filters.command("stack"))
async def search_stackoverflow(app, msg: Message):
    query = msg.text.split(None, 1)
    if len(query) == 1:
        return await msg.reply_text("📘 Please provide a query to search StackOverflow.")
    
    wait_msg = await msg.reply_text("💻 Searching StackOverflow...")
    try:
        results = await stsearch.async_search(query[1])
        keyboard = build_keyboard(results)
        await wait_msg.delete()
        await msg.reply_text(
            f"🧠 StackOverflow results for: **{query[1].title()}**",
            reply_markup=keyboard
        )
    except NoResultsFound:
        await wait_msg.delete()
        await msg.reply_text("❌ No StackOverflow results found for your query.")
    except NoResultsOrTrafficError:
        await wait_msg.delete()
        await msg.reply_text("🚫 StackOverflow is under traffic pressure. Try again soon.")
    except Exception as e:
        await wait_msg.delete()
        await msg.reply_text("⚠️ Something went wrong. Please report to @iam_Audify.")
        print(f"[ERROR - Stack Search]: {e}\n{format_exc()}")
