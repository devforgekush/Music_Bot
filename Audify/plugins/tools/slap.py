# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import requests
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatWriteForbidden, ChatRestricted, RPCError
from Audify import app

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


# ✅ Helper to send image safely
async def send_action_image(client, message: Message, action_type: str, category: str, emoji: str):
    try:
        response = requests.get(f"{API_URL}/{action_type}/{category}", timeout=10)
        if response.status_code == 200:
            image_url = response.json().get("url")
            if not image_url:
                raise ValueError("No image URL in API response.")

            user = message.from_user
            sender_name = f"[{user.first_name}](tg://user?id={user.id})"

            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                replied_name = f"[{replied_user.first_name}](tg://user?id={replied_user.id})"
                caption = f"{sender_name} sent **{category}** to {replied_name} {emoji}"
            else:
                caption = f"{sender_name} is feeling **{category}** {emoji}"

            try:
                await client.send_animation(
                    chat_id=message.chat.id,
                    animation=image_url,
                    caption=caption,
                    parse_mode="MarkdownV2"  # ✅ Fixed parse mode
                )
            except (ChatWriteForbidden, ChatRestricted):
                print(f"[Waifu.pics] Chat restricted: {message.chat.id}")
            except RPCError as e:
                print(f"[Waifu.pics] Telegram RPC error: {e}")

        else:
            await message.reply_text("❌ Error occurred while fetching image.")
    except Exception as e:
        print(f"[Waifu.pics] Error: {e}")
        try:
            await message.reply_text("❌ Failed to get image from API.")
        except ChatWriteForbidden:
            pass


# ✅ Register SFW handlers
for category, emoji in sfw_actions.items():
    @app.on_message(filters.command(category))
    async def sfw_handler(client, message, category=category, emoji=emoji):
        await send_action_image(client, message, "sfw", category, emoji)


# ✅ Register NSFW handlers
for category, emoji in nsfw_actions.items():
    @app.on_message(filters.command(category))
    async def nsfw_handler(client, message, category=category, emoji=emoji):
        await send_action_image(client, message, "nsfw", category, emoji)
