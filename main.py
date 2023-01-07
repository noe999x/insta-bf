import os, time
from os import system as sis
from time import sleep as turu
sis('git pull')
sis('clear')
def asu:
    x=input('Sudahkah anda menginstall module yang dibutuhkan? (s/b) ?')
    if x in['s','sudah','udh','udah']:
       import insta
    elif x in['b','belum','blm','belom']:
         sis('pip install play-audio')
         sis('pip install requests')
         print('Module has installed')
         turu(2)
         import insta
    elif x in['',' ']:
         print('yang bener asu')
         turu(2)
         asu()
    else:print('yang bener asu');turu(2);asu()
asu()
     
