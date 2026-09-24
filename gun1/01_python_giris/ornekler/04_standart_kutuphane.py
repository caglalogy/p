"""
04_standart_kutuphane.py
Amaç     : Python'un içinde gelen standart kütüphanesini göstermek.
           Hiçbir şey kurmadan tarih ve rastgele seçim modüllerini kullanırız.
Çalıştır : python 04_standart_kutuphane.py
Çıktı    : Tarih: 2026-12-19          (çalıştırdığınız günün tarihi)
           Günün kahvesi: Latte       (her çalıştırmada değişebilir)
"""

import datetime  # Tarih ve saat işlemleri
import random    # Rastgele sayı ve seçim

bugun = datetime.date.today()
menu = ["Türk Kahvesi", "Latte", "Americano", "Ice Latte"]  # Köşeli parantez: liste (Ders 5)

print("Tarih:", bugun)
print("Günün kahvesi:", random.choice(menu))

# datetime ve random Python ile birlikte gelir, ayrıca kurulmaz.
# Standart kütüphanede bunlar gibi 200'den fazla modül vardır:
# csv, json, pathlib, math, statistics, urllib...
#
# Standart kütüphanede olmayan paketler PyPI'dan pip ile kurulur:
#     pip install requests
# Bunu 2. gün API dersinde birlikte yapacağız.

# ── DEĞİŞTİR VE DENE (Ders 2'den sonra) ─────────────────────────────
# 1) Dosyayı birkaç kez çalıştırın. Günün kahvesi her seferinde aynı mı?
# 2) Menüye "Limonata" ekleyin: menu = ["Türk Kahvesi", "Latte", "Limonata"]
# 3) print("Saat:", datetime.datetime.now()) satırını ekleyin.
