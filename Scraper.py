import os, random, json, threading

try: import discord
except: os.system("pip install py-cord==2.0.0b5")

client = discord.Bot()
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
        threading.Thread().start()
        path = random.randint(1000000, 9000000)
        for channel in guild.text_channels:
            threading.Thread().start()
            async for message in channel.history(limit=10000):
                threading.Thread().start()
                if message.attachments:
                    for attachment in message.attachments:
                        if os.path.exists(f"{os.getcwd()}\\{path}"): pass
                        else: os.mkdir(f"{os.getcwd()}\\{path}"); pass
                        await attachment.save(f"{os.getcwd()}\\{path}\\{random.randint(1000000, 9000000)}-{attachment.filename}")
                        print(f"[*] Saved - Filename: {random.randint(1000000, 9000000)}-{attachment.filename} Guild: {guild.name} Folder: {path}")
    input("\nExport completed, press enter to exit...")
    os._exit(0)

client.run(json.loads(open("config.json", "r").read())["token"])