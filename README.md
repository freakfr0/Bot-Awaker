# Discord Bot Awaker

A multifunctional Discord bot that allows you to:
- Send messages
- Create channels and roles
- Send webhook messages
- Set bot activity status
- Enable auto-response commands via `config.json`

---

## Project Structure

Bot-Awaker/

├── bot.py # Main bot script

├── config.json # Stores token, guild ID, and auto commands

└── README.md # Documentation
 

---

## Setup

1. **Install dependencies**

```bash
pip install discord.py requests
```

##Configure your bot

Edit config.json with your bot token and guild ID:
```
{
  "token": "YOUR_BOT_TOKEN",
  "guild_id": "YOUR_GUILD_ID",
  "auto_commands": {
    "Hi": "Hello I'm Bot",
    "ping": "Pong!",
    "uptime": "Running for X minutes"
  }
}
```
## How It Works
Main Menu Options:
```
         ╔══════════════════════════════╦════════════════════════════╗
         ║         Version: 1        	 ║        Dev: Freak          ║
         ╚══════════════════════════════╩════════════════════════════╝
 ╔══════════════════════════╦══════════════════════════╦════════════════════════╗
 ║    [1] Send Message      ║    [2] Create Channel    ║      [3] Create Role   ║
 ╠══════════════════════════╬══════════════════════════╬════════════════════════╣
 ║ [4] Send Webhook Message ║  [5] Change Bot Activity ║   [6] Start AutoBot    ║
 ╚══════════════════════════╩══════════════════════════╩════════════════════════╝  
```

## Run the Bot
```
python bot.py
```

Important: Keep config.json in the same directory as vibe.exe!

## Features

    Fast, threaded message dispatch

    Auto command handler (?cmd, ?msg, etc.)

    Supports webhook spam, bot activity, and more

    Easy to convert to executable

## Developer

Freak (Discord Dev)
Version: 1.0
All credit to the original creator
⚠ Disclaimer

This tool is intended for educational and moderation purposes only.
The developer is not responsible for any misuse.


---

Let me know if you want this version in **dark-mode Markdown style**, or want me to create a `config.json` template as well.

