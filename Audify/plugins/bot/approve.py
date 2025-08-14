# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

from Audify import app
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters


WELCOME_TEXT = (
    "👋 Hello {mention},\n"
    "✅ You've been approved to join **{title}**.\n\n"
    "We're glad to have you here!"
)

# Close button for welcome message
CLOSE_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("✖ Close", callback_data="close")]
])


# ========== Join Request Handler ==========

@app.on_chat_join_request()
async def handle_join_request(client, request: ChatJoinRequest):
    chat = request.chat
    user = request.from_user

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✅", callback_data=f"approve_{chat.id}_{user.id}"),
                InlineKeyboardButton("❌", callback_data=f"reject_{chat.id}_{user.id}")
            ]
        ]
    )

    await app.send_message(
        chat.id,
        f"👤 Join request from: [{user.first_name}](tg://user?id={user.id})\nApprove or Reject?",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )


# ========== Callback Handlers ==========

@app.on_callback_query(filters.regex(r"^(approve|reject)_"))
async def handle_approval_callback(client, callback: CallbackQuery):
    data = callback.data.split("_")
    action, chat_id, user_id = data[0], int(data[1]), int(data[2])

    try:
        if action == "approve":
            # Approve request
            await client.approve_chat_join_request(chat_id, user_id)
            await callback.answer("✅ User approved!", show_alert=True)

            # Send welcome message (still kept ✅)
            chat = await client.get_chat(chat_id)
            user = await client.get_users(user_id)
            await client.send_message(
                chat_id=chat_id,
                text=WELCOME_TEXT.format(mention=user.mention, title=chat.title),
                reply_markup=CLOSE_BUTTON
            )

        else:
            # Reject request
            await client.decline_chat_join_request(chat_id, user_id)
            await callback.answer("❌ User rejected!", show_alert=True)

        # Delete the inline buttons message
        await callback.message.delete()

    except Exception as e:
        await callback.answer(f"⚠️ Error: {e}", show_alert=True)
