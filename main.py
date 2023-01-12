import os, time
from time import sleep as turu
from os import system as sis
sis('clear')
print('1. Russian\n2. English\n3. Bahasa Indonesia\n0. Install bahan')
x=input('Pilih bahasa : ')
if x in['1']:
   sis('git pull')
   import insta_ru
elif x in['2']:
     sis('git pull')
     import insta_en
elif x in['3']:
     sis('git pull')
     print('•Bahasa belum tersedia')
     exit()
elif x in['0']:
     sis('pkg install play-audio')
else:print('yang bener su');turu(2);sis('python main.py')
