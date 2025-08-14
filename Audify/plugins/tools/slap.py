# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import logging
import html
import requests
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatWriteForbidden, ChatRestricted, RPCError
from Audify import app

log = logging.getLogger(__name__)

API_URL = "https://api.waifu.pics"

# ✅ SFW Action Categories with emojis
sfw_actions = {
    "waifu": "🌸", "neko": "🐱", "shinobu": "🍵", "megumin": "✨", "bully": "😈",
    "cuddle": "🤗", "cry": "😢", "hug": "🫂", "awoo": "🐺", "kiss": "😘",
    "lick": "👅", "pat": "🖐", "smug": "😏", "bonk": "🔨", "yeet": "📤",
    "blush": "😊", "smile": "😄", "wave": "👋", "highfive": "✋", "handhold": "🤝",
    "nom": "🍽", "bite": "😬", "glomp": "🫶", "slap": "😤", "kill": "💀",
    "kick": "🥾", "happy": "😁", "wink": "😉", "poke": "👉", "dance": "💃",
    "cringe": "😬"
}

# ✅ NSFW Action Categories with emojis
nsfw_actions = {
    "waifu": "🌸", "neko": "🐱", "trap": "👧", "blowjob": "😶‍🌫️"
}


def html_user_mention(user) -> str:
    """
    Safe HTML mention for a user. Handles None and escapes special chars.
    """
    if not user:
        return "someone"
    name = user.first_name or "User"
    name = html.escape(name, quote=True)
    return f'<a href="tg://user?id={user.id}">{name}</a>'


def build_caption(sender, category: str, emoji: str, replied_user=None) -> str:
    """
    Build a robust HTML caption. Avoids MarkdownV2 pitfalls completely.
    """
    sender_mention = html_user_mention(sender)
    category_esc = html.escape(category, quote=True)
    emoji_esc = html.escape(emoji, quote=True)

    if replied_user:
        replied_mention = html_user_mention(replied_user)
        return f"{sender_mention} sent <b>{category_esc}</b> to {replied_mention} {emoji_esc}"
    return f"{sender_mention} is feeling <b>{category_esc}</b> {emoji_esc}"


async def safe_reply_animation(message: Message, animation_url: str, caption: str):
    """
    Try replying with an animation; swallow write/permission errors gracefully.
    """
    try:
        await message.reply_animation(
            animation=animation_url,
            caption=caption,
            parse_mode="html",         # ✅ permanent fix: use HTML (no MarkdownV2)
            disable_notification=False # keep normal behavior
        )
        return True
    except (ChatWriteForbidden, ChatRestricted):
        log.warning("[Waifu.pics] Chat write restricted: %s", message.chat.id if message.chat else "unknown")
    except RPCError as e:
        # Covers CHANNEL_PRIVATE and other Telegram RPC errors
        log.warning("[Waifu.pics] Telegram RPC error in chat %s: %s", message.chat.id if message.chat else "unknown", e)
    except Exception as e:
        log.exception("[Waifu.pics] Unexpected error sending animation: %s", e)
    return False


async def safe_reply_text(message: Message, text: str):
    """
    Try replying with text; swallow write/permission errors gracefully.
    """
    try:
        await message.reply_text(text, disable_web_page_preview=True)
        return True
    except (ChatWriteForbidden, ChatRestricted):
        log.warning("[Waifu.pics] Chat write restricted (text): %s", message.chat.id if message.chat else "unknown")
    except RPCError as e:
        log.warning("[Waifu.pics] Telegram RPC error (text) in chat %s: %s", message.chat.id if message.chat else "unknown", e)
    except Exception as e:
        log.exception("[Waifu.pics] Unexpected error sending text: %s", e)
    return False


# ✅ Helper to fetch & send image safely
async def send_action_image(client, message: Message, action_type: str, category: str, emoji: str):
    # Ignore messages without a user context (e.g., anonymous admins/channel posts)
    if not (message and message.from_user):
        log.info("[Waifu.pics] Ignoring message without from_user in chat %s", message.chat.id if message.chat else "unknown")
        return

    try:
        # Use a short timeout to avoid blocking the event loop too long
        r = requests.get(f"{API_URL}/{action_type}/{category}", timeout=10)
        if r.status_code != 200:
            await safe_reply_text(message, "❌ Error occurred while fetching image.")
            return

        image_url = (r.json() or {}).get("url")
        if not image_url:
            await safe_reply_text(message, "❌ Failed to get image from API.")
            return

        replied_user = message.reply_to_message.from_user if (message.reply_to_message and message.reply_to_message.from_user) else None
        caption = build_caption(message.from_user, category, emoji, replied_user)

        sent = await safe_reply_animation(message, image_url, caption)
        if not sent:
            # If we couldn't send (e.g., CHANNEL_PRIVATE), fail silently (already logged)
            return

    except Exception as e:
        log.exception("[Waifu.pics] Fatal error: %s", e)
        # Best-effort user feedback (will be skipped if not allowed)
        await safe_reply_text(message, "❌ Something went wrong while processing your request.")


# ✅ Register SFW handlers
for _category, _emoji in sfw_actions.items():
    @app.on_message(filters.command(_category))
    async def _sfw_handler(client, message: Message, category=_category, emoji=_emoji):
        await send_action_image(client, message, "sfw", category, emoji)


# ✅ Register NSFW handlers
for _category, _emoji in nsfw_actions.items():
    @app.on_message(filters.command(_category))
    async def _nsfw_handler(client, message: Message, category=_category, emoji=_emoji):
        await send_action_image(client, message, "nsfw", category, emoji)
