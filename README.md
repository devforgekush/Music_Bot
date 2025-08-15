<p align="center">
	<img src="https://raw.githubusercontent.com/devforgekush/musicbot-/main/Audify/assets/play_icons.png" width="120" alt="@devforgekush Bot Logo" />
</p>

<p align="center">
	<img src="https://raw.githubusercontent.com/devforgekush/musicbot-/main/Audify/assets/play_icons.png" width="120" alt="@devforgekush Bot Logo" />
</p>

<h1 align="center">@devforgekush Telegram Music Bot</h1>

<p align="center">
	<b>High-quality music streaming, group controls, and multi-platform support for Telegram.</b><br>
	<sub>Created & maintained by <a href="https://github.com/devforgekush">@devforgekush</a></sub>
</p>


## 🚀 Features

## 🛠️ Setup & Deployment (Railway)
1. Fork or clone this repo.
2. Deploy to Railway using the Railway dashboard.
3. Set the required environment variables:
	 - `API_ID`, `API_HASH`, `BOT_TOKEN`, `LOGGER_ID`, `MONGO_DB_URI`, `OWNER_ID`, `STRING_SESSION`, `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `API_KEY`, `BOT_URL`
4. Expose your service and copy the public Railway URL for `BOT_URL`.
5. Start your bot!

## ⚙️ Environment Variables
| Variable              | Description                       |
|----------------------|-----------------------------------|
| API_ID               | Telegram API ID                   |
| API_HASH             | Telegram API Hash                 |
| BOT_TOKEN            | Telegram Bot Token                |
| LOGGER_ID            | Telegram Chat ID for logs         |
| MONGO_DB_URI         | MongoDB Atlas URI                 |
| OWNER_ID             | Telegram User ID of owner         |
| STRING_SESSION       | Pyrogram String Session           |
| SPOTIFY_CLIENT_ID    | Spotify API Client ID             |
| SPOTIFY_CLIENT_SECRET| Spotify API Client Secret         |
| API_KEY              | Optional API Key                  |
| BOT_URL              | Public Railway URL for pinger     |

## 📦 Usage

## 📄 License
This project is licensed under the terms described in the [LICENSE](LICENSE) file.

## 💬 Support


<p align="center">
</p>
# Telegram Music Bot

This project is a Telegram music bot for group and channel management. It supports music playback from multiple sources and includes admin controls and database integration.

## Features
- Play music in Telegram groups and channels
- Supports YouTube, Spotify, SoundCloud, and more
- Admin and owner controls
- MongoDB database integration

## 👑 Bot Owner & Admin Commands

Reply to a user's message and use any of the following commands:

• <code>/devforgekush ban</code> – Ban the user
• <code>/devforgekush unban</code> – Unban the user
• <code>/devforgekush mute</code> – Mute the user
• <code>/devforgekush unmute</code> – Unmute the user
• <code>/devforgekush kick</code> – Kick the user
• <code>/devforgekush promote</code> – Promote with limited rights
• <code>/devforgekush fullpromote</code> – Full admin rights
• <code>/devforgekush demote</code> – Remove admin rights

<i>⚠️ You must reply to a user's message for these commands to work.</i>
- Easy deployment on Railway, Replit, or Heroku

## License
See `LICENSE` for details.

For support, please refer to the documentation or community forums.
