"""
01_acilis_demosu.py
Amac     : Python'un neler yapabildigini gostermek. Kahve Duragi'nin 3 subesinden
           gelen satis dosyalarini birlestirir ve gun sonu raporunu saniyeler
           icinde hazirlar.
Calistir : python 01_acilis_demosu.py
Cikti    : Sube cirolarini, en cok satan urunleri ve raporun kac saniyede
           hazirlandigini ekrana yazar. Ayrica bu klasorde demo_veri/ klasorunu
           ve gun_sonu_raporu.txt dosyasini olusturur.

Not: Bu dosyayi Ders 1'de egitmen gosterir. Icindeki yapilarin hepsini
(degiskenler, donguler, sozlukler, fonksiyonlar, dosya islemleri) egitim
boyunca tek tek ogrenecegiz. Simdilik calistirin ve sonucu izleyin.
2. gunun sonunda bu dosyayi satir satir okuyabiliyor olacaksiniz.
"""

import csv
import random
import time
from pathlib import Path

# Dosyalarin olusturulacagi klasor: bu dosyanin yanindaki demo_veri/
KLASOR = Path(__file__).parent / "demo_veri"

SUBELER = ["Kucukcekmece", "Kadikoy", "Besiktas"]

# Urun adi: fiyat (TL)
MENU = {
    "Turk Kahvesi": 60,
    "Latte": 85,
    "Americano": 75,
    "Ice Latte": 95,
    "Limonata": 70,
    "Simit": 25,
    "Cheesecake": 120,
    "Kurabiye": 40,
}


def tl(tutar):
    """1234567 sayisini '1.234.567 TL' biciminde yazar."""
    return f"{tutar:,.0f} TL".replace(",", ".")


def ornek_veri_olustur():
    """Her sube icin bir gunluk satis dosyasi (CSV) uretir."""
    KLASOR.mkdir(exist_ok=True)
    rastgele = random.Random(19)  # Sabit baslangic: her calistirmada ayni veri
    for sube in SUBELER:
        yol = KLASOR / f"{sube.lower()}_satislar.csv"
        with open(yol, "w", newline="", encoding="utf-8") as dosya:
            yazici = csv.writer(dosya)
            yazici.writerow(["saat", "urun", "adet"])
            for _ in range(rastgele.randint(80, 120)):
                saat = f"{rastgele.randint(8, 21):02d}:{rastgele.randint(0, 59):02d}"
                urun = rastgele.choice(list(MENU))
                adet = rastgele.randint(1, 3)
                yazici.writerow([saat, urun, adet])


def rapor_hazirla():
    """Uc subenin dosyasini okur; sube cirolarini ve urun satis adetlerini hesaplar."""
    sube_cirosu = {}
    urun_adedi = {}
    for sube in SUBELER:
        with open(KLASOR / f"{sube.lower()}_satislar.csv", encoding="utf-8") as dosya:
            for satir in csv.DictReader(dosya):
                urun = satir["urun"]
                adet = int(satir["adet"])
                sube_cirosu[sube] = sube_cirosu.get(sube, 0) + adet * MENU[urun]
                urun_adedi[urun] = urun_adedi.get(urun, 0) + adet
    return sube_cirosu, urun_adedi


def raporu_yaz(sube_cirosu, urun_adedi):
    """Raporu satir satir hazirlar; hem ekrana hem dosyaya yazar."""
    satirlar = ["KAHVE DURAGI - GUN SONU RAPORU", "=" * 34, "", "Sube cirosu:"]
    for sube, ciro in sube_cirosu.items():
        satirlar.append(f"  {sube:<14}{tl(ciro):>14}")
    satirlar.append(f"  {'TOPLAM':<14}{tl(sum(sube_cirosu.values())):>14}")

    satirlar += ["", "En cok satan 3 urun:"]
    en_cok_satanlar = sorted(urun_adedi.items(), key=lambda x: x[1], reverse=True)[:3]
    for sira, (urun, adet) in enumerate(en_cok_satanlar, start=1):
        satirlar.append(f"  {sira}. {urun:<14}{adet:>4} adet")

    metin = "\n".join(satirlar)
    print(metin)
    (Path(__file__).parent / "gun_sonu_raporu.txt").write_text(metin + "\n", encoding="utf-8")


baslangic = time.perf_counter()

ornek_veri_olustur()
ciro, adetler = rapor_hazirla()
raporu_yaz(ciro, adetler)

sure = time.perf_counter() - baslangic
print()
print(f"Rapor {sure:.3f} saniyede hazirlandi.")
print("Kaydedildi: gun_sonu_raporu.txt")

# -- DEGISTIR VE DENE (Ders 2'den sonra) -----------------------------
# 1) demo_veri/ klasorundeki CSV dosyalarindan birini acip inceleyin.
#    Excel'deki bir tabloya ne kadar benziyor?
# 2) MENU icinde Latte'nin fiyatini 100 yapin ve tekrar calistirin.
#    Hangi rakamlar degisti?
# 3) random.Random(19) satirindaki 19'u baska bir sayiyla degistirin.
#    Neden bu sefer farkli bir rapor cikti?
