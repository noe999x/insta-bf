import os, time
from time import sleep as barbara
from os import system as hutao
def susu_ganyu():
    hutao('clear')
    print(f""" ⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀                                                                  
⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢹⣿⣆  ___   _  _   ___   _____   _     ___   ___     _     __  __     
⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠛⠻⢿⣿⣿⣷⣶⣾⣿⣿ |_ _| | \| | / __| |_   _| /_\   / __| | _ \   /_\   |  \/  |    
⣿⣿⣿⣿⣿⡿⠋⠀⠀⣀⣠⣄⣀⠀⠀⠙⢿⣿⣿⣿⣿⣿  | |  | .` | \__ \   | |  / _ \ | (_ | |   /  / _ \  | |\/| |    
⣿⣿⣿⣿⣿⠁⠀⢠⣾⣿⣿⣿⣿⣷⡄⠀⠈⣿⣿⣿⣿⣿ |___| |_|\_| |___/   |_| /_/ \_\ \___| |_|_\ /_/ \_\ |_|  |_|    
⣿⣿⣿⣿⡇⠀⠀⢾⣿⣿⣿⣿⣿⣿⡷⠀⠀⢸⣿⣿⣿⣿ Codder : noe999x
⣿⣿⣿⣿⣿⡀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢀⣿⣿⣿⣿⣿ Special thanks to : BrayennnXD - DerrXyr
⣿⣿⣿⣿⣿⣷⣄⠀⠀⠉⠙⠋⠉⠀⠀⣠⣾⣿⣿⣿⣿⣿ Last updated on github : 12-01-2023 [FinalVer]
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿ ••••••••••••••••••••••••
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏ facebook.com/bagasekaapr
⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀ github.com/noe999x""")
def susu_nahida():
    susu_ganyu()
    print('1. Russian\n2. English\n3. Bahasa Indonesia\n0. Update SC')
    lumine=input('Mulai program dengan bahasa : ')
    if lumine in['1']:
       import insta_ru
    elif lumine in['2']:
         import insta_en
    elif lumine in['3']:
         print('• Bahasa belum tersedia');barbara(2)
         susu_nahida()
    elif lumine in['0']:
         hutao('git pull')
         hutao('pkg install play-audio')
    else:print('• Yang bener su');barbara(2);hutao('python main.py')
susu_nahida()
