<p align="center">
  <img src="https://raw.githubusercontent.com/devforgekush/musicbot-/main/Audify/assets/play_icons.png" width="120" alt="Audiofy Bot Logo" />
</p>

<h1 align="center">Audiofy Telegram Music Bot</h1>

<p align="center">
  <b>High-quality music streaming, group controls, and multi-platform support for Telegram.</b><br>
  <sub>Created & maintained by <a href="https://github.com/devforgekush">@devforgekush</a></sub>
</p>

---

## 🚀 Features
- 🎵 Play music in Telegram groups and channels
- 📺 Supports YouTube, Spotify, SoundCloud, and more
- 👑 Powerful admin and owner controls
- 🗄️ MongoDB database integration
- ⚡ Fast, reliable, and easy deployment on Railway
- 🔒 Secure and privacy-focused

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
- Add the bot to your Telegram group/channel.
- Use `/play <song name>` to start streaming.
- Admins can use `/pause`, `/resume`, `/skip`, `/stop`, etc.
- For help, use `/help` or check the documentation.

## 📄 License
This project is licensed under the terms described in the [LICENSE](LICENSE) file.

## 💬 Support
- For issues, open a GitHub issue.
- For questions, contact <a href="https://t.me/devforgekush">@devforgekush</a> on Telegram.

---

<p align="center">
  <i>© @devforgekush. All rights reserved. Audiofy Bot</i>
</p>
