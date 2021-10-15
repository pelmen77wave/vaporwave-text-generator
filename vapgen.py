#!/usr/bin/env python3
from colorama import Fore, init
init()

print(Fore.CYAN)

print('''
             ,-._
           _.-'  '--.
         .'      _  -`\_
        / .----.`_.'----'
        ;/     `
       /_;

    ._      ._      ._      ._
_.-._)`\_.-._)`\_.-._)`\_.-._)`\_.-._

    Vaporwave Text Generator v1
''')

print(Fore.MAGENTA)

try:
    i = input('Input --> ')
except KeyboardInterrupt:
    print("\nexit...")

else:

    a = "abcdefghijklmnopqrstuvwxyz"
    j1 = "卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙"
    j2 = "丹日亡句ヨ乍呂廾工勹片し冊几回尸甲尺己卞凵レ山メと乙"
    j3 = "ﾑ乃ᄃり乇ｷムんﾉﾌズﾚﾶ刀のｱゐ尺丂ｲひ√Ｗﾒﾘ乙"

    table1 = i.maketrans(a, j1)
    table2 = i.maketrans(a, j2)
    table3 = i.maketrans(a, j3)

    def Text(y):
        for x in range(len(i)):
            o = chr(ord(i[x]) + y)
            print(o.replace('＀', ' '), end='')

    print()
    Text(65248)
    print()
    print("≋" + ("≋".join(i)) + "≋")
    print()

    print(i.translate(table1))
    print(i.translate(table2))
    print(i.translate(table3))

    print()