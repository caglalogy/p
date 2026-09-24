"""
04_standart_kutuphane.py
Amac     : Python'un icinde gelen standart kutuphanesini gostermek.
           Hicbir sey kurmadan tarih ve rastgele secim modullerini kullaniriz.
Calistir : python 04_standart_kutuphane.py
Cikti    : Tarih: 2026-12-19          (calistirdiginiz gunun tarihi)
           Gunun kahvesi: Latte       (her calistirmada degisebilir)
"""

import datetime  # Tarih ve saat islemleri
import random    # Rastgele sayi ve secim

bugun = datetime.date.today()
menu = ["Turk Kahvesi", "Latte", "Americano", "Ice Latte"]  # Koseli parantez: liste (Ders 5)

print("Tarih:", bugun)
print("Gunun kahvesi:", random.choice(menu))

# datetime ve random Python ile birlikte gelir, ayrica kurulmaz.
# Standart kutuphanede bunlar gibi 200'den fazla modul vardir:
# csv, json, pathlib, math, statistics, urllib...
#
# Standart kutuphanede olmayan paketler PyPI'dan pip ile kurulur:
#     pip install requests
# Bunu 2. gun API dersinde birlikte yapacagiz.

# -- DEGISTIR VE DENE (Ders 2'den sonra) -----------------------------
# 1) Dosyayi birkac kez calistirin. Gunun kahvesi her seferinde ayni mi?
# 2) Menuye "Limonata" ekleyin: menu = ["Turk Kahvesi", "Latte", "Limonata"]
# 3) print("Saat:", datetime.datetime.now()) satirini ekleyin.
