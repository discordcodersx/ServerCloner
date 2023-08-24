from os import system
import psutil
import time
import discord
import asyncio
import ctypes
from pypresence import Presence
import colorama
from colorama import Fore, init, Style
import platform


from serverclone import Clone
intents = discord.Intents().all()
bot = discord.Client(intents=intents)
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}


███    ███ ███████ ██    ██ ███████ ███████ ██   ██  ██████  ██████  
████  ████ ██       ██  ██     ███  ██      ██   ██ ██    ██ ██   ██ 
██ ████ ██ █████     ████     ███   ███████ ███████ ██    ██ ██████  
██  ██  ██ ██         ██     ███         ██ ██   ██ ██    ██ ██      
██      ██ ███████    ██    ███████ ███████ ██   ██  ██████  ██      
                                                                     
                                                                                           
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}by MeyzShop{Style.RESET_ALL}
                                                         
        """)
if os == "Windows":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Discord Server Cloner By MeyzShop")
else:
    system("Discord Server Cloner By MeyzShop")
token = input(f'Lütfen Token Giriniz:\n >')
guild_s = input('Klonlamak İstediğiniz Sunucu ID si girin:\n >')
guild = input('Klonlanacak Sunucu ID si girin:\n >')
input_guild_id = guild_s  
output_guild_id = guild  
token = token  


print("  ")
print("  ")

@bot.event
async def on_ready():
    print(f"Logged In as : {bot.user}")
    print("Sunucu Klonlanıyorrrrr")
    guild_from = bot.get_guild(int(input_guild_id))
    guild_to = bot.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                            ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
                                            ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
                                            ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
                                            ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
                                            ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
                                            ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░

    {Style.RESET_ALL}""")
    if os == "Windows":
        ctypes.windll.user32.MessageBoxW(0, "sunucu klonlandı!", "Discord Server Cloner by MeyzShop", 0x0 | 0x40)
    else:
        return
    await asyncio.sleep(5)
    await bot.close()


bot.run(token, bot=False)
