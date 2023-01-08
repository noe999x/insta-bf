import os
from os import system as sis
try:
    sis('git pull')
except requests.exceptions.ConnectionError:
    print('cek koneksi lo')
import insta
