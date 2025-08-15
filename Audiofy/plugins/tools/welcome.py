# ---------------------------------------------------------
# Audify Bot - All rights reserved
# ---------------------------------------------------------
# This code is part of the Audify Bot project.
# Unauthorized copying, distribution, or use is prohibited.
# © Graybots™. All rights reserved.
# ---------------------------------------------------------

import os
import time
import random
import asyncio
from pathlib import Path
from logging import getLogger
from typing import Union

import aiohttp
from pyrogram import Client, filters, enums
from pyrogram.errors import RPCError, FloodWait, ChatAdminRequired, ChatWriteForbidden, ChannelPrivate
from pyrogram.enums import ParseMode
from pyrogram.types import ChatMemberUpdated, Message

from Audify import app
from config import OWNER_ID
from Audify.misc import SUDOERS

LOGGER = getLogger(__name__)

# -------------------------------
# Welcome database
# -------------------------------
class WelDatabase:
    def __init__(self):
        # {chat_id: {"enabled": bool}}
        self.data = {}

    async def get_status(self, chat_id: int) -> bool:
        return self.data.get(chat_id, {"enabled": True})["enabled"]

    async def set_status(self, chat_id: int, status: bool):
        self.data[chat_id] = {"enabled": status}


wlcm = WelDatabase()


# -------------------------------
# Temporary store
# -------------------------------
class temp:
    MELCOW = {}  # {chat_id: last_welcome_message}


# -------------------------------
# Cache for member counts
# -------------------------------
_chat_count_cache = {}  # {chat_id: (count, last_update)}


async def get_cached_member_count(chat_id: int) -> Union[int, str]:
    """Get member count with caching and floodwait handling."""
    now = time.time()
    if chat_id in _chat_count_cache:
        count, last_update = _chat_count_cache[chat_id]
        if now - last_update < 600:  # 10 min cache
            return count

    try:
        count = await app.get_chat_members_count(chat_id)
        _chat_count_cache[chat_id] = (count, now)
        return count
    except FloodWait as e:
        LOGGER.warning(f"[WELCOME] FloodWait {e.value}s while fetching member count for {chat_id}")
        await asyncio.sleep(e.value)
        return await get_cached_member_count(chat_id)
    except (ChannelPrivate, ChatAdminRequired, ChatWriteForbidden):
        return "N/A"
    except RPCError as e:
        LOGGER.warning(f"[WELCOME] Could not fetch member count for {chat_id}: {e}")
        return "N/A"


# -------------------------------
# Toggle command
# -------------------------------
@app.on_message(filters.command("welcome") & ~filters.private)
async def toggle_welcome(_, message: Message):
    usage = "**Usage:**\n`/welcome on`\n`/welcome off`"

    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    if not message.from_user:
        return await message.reply("**Cannot verify user.**")

    try:
        member = await app.get_chat_member(chat_id, message.from_user.id)
    except Exception:
        return await message.reply("**Failed to check admin status.**")

    if member.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return await message.reply("**Only group admins can change welcome settings.**")

    state = message.command[1].lower()
    if state == "on":
        await wlcm.set_status(chat_id, True)
        await message.reply_text(f"✅ Enabled welcome messages in **{message.chat.title}**.")
    elif state == "off":
        await wlcm.set_status(chat_id, False)
        await message.reply_text(f"🚫 Disabled welcome messages in **{message.chat.title}**.")
    else:
        await message.reply_text(usage)


# -------------------------------
# Greet new members (fixed)
# -------------------------------
@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    enabled = await wlcm.get_status(chat_id)
    if not enabled:
        return

    # Process only real joins
    if not member.new_chat_member:
        return
    if member.old_chat_member and member.old_chat_member.status in ["member", "administrator", "owner"]:
        return
    if member.new_chat_member.status != "member":
        return

    user = member.new_chat_member.user
    if not user:
        return

    await get_cached_member_count(chat_id)

    # -------------------
    # VIP welcome logic
    # -------------------
    if user.id == OWNER_ID:
        welcome_text = f"👑 Our Boss {user.mention} has joined {member.chat.title}! 🔥🔥"
    elif user.id in SUDOERS:
        welcome_text = f"💎 VIP {user.mention} just entered {member.chat.title}! 🚀"
    else:
        welcome_messages = [
            f"👋 Welcome {user.mention} to {member.chat.title}!",
            f"🎉 Glad to have you here, {user.mention}!",
            f"🔥 {user.mention} just landed in {member.chat.title}!",
            f"💥 Say hi to {user.mention}! Welcome aboard!",
            f"🌟 {user.mention}, welcome to the gang!",
            f"👑 A warm welcome to our newest member, {user.mention}!",
            f"🪄 Welcome {user.mention}, enjoy your stay in {member.chat.title}!",
            f"🚀 {user.mention} joined the chat. Fasten your seatbelt!",
            f"🎊 {user.mention} just arrived. Let’s celebrate!",
            f"🥳 Welcome, {user.mention}! Let the fun begin!",
            f"🤗 Glad to see you here, {user.mention}!",
            f"🫱 Give it up for {user.mention}! Welcome!",
            f"🎈 {user.mention} just joined the party in {member.chat.title}!",
            f"💫 Welcome {user.mention}! You’re going to love it here.",
            f"🙌 Say hey to {user.mention}, everyone!",
            f"🌍 {user.mention} has entered the world of {member.chat.title}.",
            f"🧡 Welcome, {user.mention}! We were waiting for you.",
            f"👾 New member alert: {user.mention} has joined {member.chat.title}!",
            f"🕺 {user.mention} just stepped in like a boss!",
            f"🧨 Boom! {user.mention} is now part of {member.chat.title}!",
            f"😎 Welcome {user.mention}! Time to vibe.",
            f"🥂 Raise your glasses for {user.mention}!",
            f"🎮 Game on! {user.mention} joined the crew!",
            f"🌊 {user.mention} just surfed into {member.chat.title}!",
            f"🦸‍♂️ {user.mention} joined us. The team is stronger now!",
            f"📢 Welcome {user.mention}! Let’s make some noise!",
            f"📬 A new message has arrived: {user.mention} joined!",
            f"🗺️ {user.mention} found their way to {member.chat.title}!",
            f"🚁 {user.mention} landed safely. Welcome!",
            f"🫡 {user.mention} has reported for duty!",
            f"🛸 Alien detected: {user.mention} joined {member.chat.title}!",
            f"🍕 Pizza for everyone! {user.mention} just joined!",
            f"🔔 Ding ding! {user.mention} is here!",
            f"🐣 Fresh member alert! Welcome {user.mention}!",
            f"💌 Welcome {user.mention}, we’ve been expecting you.",
            f"🧸 {user.mention} joined — let’s make them feel at home!",
            f"👣 New footsteps echo! {user.mention} is in!",
            f"📢 Announcement: {user.mention} is now in the chat!",
            f"🎤 {user.mention}, take the mic. Welcome!",
            f"🎩 Hats off! {user.mention} just walked in.",
            f"💬 A new voice has joined — say hi to {user.mention}!",
            f"🪄 {user.mention}, you've entered the magic circle!",
            f"🌅 A new dawn with {user.mention} in {member.chat.title}!",
            f"📍 You are now here, {user.mention}. Welcome!",
            f"💯 Welcome {user.mention}! You make us 100x better!",
            f"🎯 Bullseye! {user.mention} hit the target and joined!",
            f"🧭 Found your way here, {user.mention}? Welcome!",
            f"🔑 You just unlocked {member.chat.title}, {user.mention}!",
            f"🫶 Let’s give a warm hug to {user.mention}!",
            f"⚡ {user.mention} just boosted the energy here!",
            f"🔮 The prophecy was true — {user.mention} has arrived!",
        ]
        welcome_text = random.choice(welcome_messages)

    # -------------------
    # Send + delete old
    # -------------------
    try:
        if temp.MELCOW.get(f"welcome-{chat_id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{chat_id}"].delete()
            except Exception:
                pass

        msg = await app.send_message(
            chat_id,
            text=welcome_text,
            parse_mode=ParseMode.HTML,
        )

        if user.id != OWNER_ID and user.id not in SUDOERS:
            temp.MELCOW[f"welcome-{chat_id}"] = msg

    except Exception as e:
        LOGGER.debug(f"[WELCOME] Failed in {chat_id}: {e}")
