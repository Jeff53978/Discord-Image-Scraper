import os, random, json, threading, asyncio

try: import discord
except: os.system("pip install discord.py")

client = discord.Client(self_bot=True)
try: os.system("cls")
except: os.system("clear")

@client.event
async def on_ready():
    print(f"Logged in as: {client.user.name}")
    print("Loading Guilds... \n")
    for guild in client.guilds:
        print(f"Loaded - {guild.name}")
    print("")
    for guild in client.guilds:
        path = random.randint(1000000, 9000000)
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=10000):
                    if message.attachments:
                        for attachment in message.attachments:
                            if os.path.exists(f"{os.getcwd()}\\{path}"): pass
                            else: os.mkdir(f"{os.getcwd()}\\{path}"); pass
                            await attachment.save(f"{os.getcwd()}\\{path}\\{random.randint(1000000, 9000000)}-{attachment.filename}")
                            print(f"[*] Saved - Filename: {random.randint(1000000, 9000000)}-{attachment.filename} Guild: {guild.name} Folder: {path}")
            except:
                break
    input("\nExport completed, press enter to exit...")
    os._exit(0)
client.run(json.loads(open("config.json", "r").read())["token"], bot=False)