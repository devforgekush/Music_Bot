from pyrogram import Client, filters
import instaloader
import requests
import os
import re
from pyrogram.types import InputMediaPhoto, InputMediaVideo

from Audify import app 

# Create a global Instaloader instance
L = instaloader.Instaloader()

# Regex to match Instagram URLs (post/reel/tv/stories)
INSTAGRAM_REGEX = r"(https?://(?:www\.)?instagram\.com/(?:p|reel|tv|stories)/[A-Za-z0-9_-]+/?)"

# Extract Instagram URL from text
def extract_instagram_url(text: str):
    match = re.search(INSTAGRAM_REGEX, text)
    return match.group(0) if match else None

# Download Instagram media using Instaloader
def download_instagram_media(url: str):
    try:
        shortcode = url.strip("/").split("/")[-1]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        media_files = []

        if post.typename == "GraphSidecar":  # multiple media
            for index, node in enumerate(post.get_sidecar_nodes()):
                media_url = node.video_url if node.is_video else node.display_url
                ext = "mp4" if node.is_video else "jpg"
                filename = f"media_{index}.{ext}"

                r = requests.get(media_url, timeout=15)
                with open(filename, "wb") as f:
                    f.write(r.content)
                media_files.append((filename, ext))
        else:
            media_url = post.video_url if post.is_video else post.url
            ext = "mp4" if post.is_video else "jpg"
            filename = f"media.{ext}"

            r = requests.get(media_url, timeout=15)
            with open(filename, "wb") as f:
                f.write(r.content)
            media_files.append((filename, ext))

        return media_files, None

    except Exception as e:
        return None, str(e)

# Auto handler for messages with Instagram links
@app.on_message(filters.text & (filters.private | filters.group))
async def auto_reel_handler(client, message):
    url = extract_instagram_url(message.text)
    if not url:
        return  # ignore if no Instagram link

    processing = await message.reply("⏳ Downloading...")

    media_files, error = download_instagram_media(url)
    if error:
        return await processing.edit(f"❌ Error: {error}")

    group = []
    for i, (filename, ext) in enumerate(media_files):
        try:
            if ext == "mp4":
                group.append(InputMediaVideo(media=filename))
            else:
                group.append(InputMediaPhoto(media=filename))

            # Send in batches of 10 (Telegram limit)
            if len(group) == 10 or i == len(media_files) - 1:
                await client.send_media_group(chat_id=message.chat.id, media=group)
                group = []
        except Exception as e:
            await message.reply(f"⚠️ Failed to send media: {e}")

    await processing.delete()

    # Cleanup
    for filename, _ in media_files:
        try:
            os.remove(filename)
        except:
            pass
