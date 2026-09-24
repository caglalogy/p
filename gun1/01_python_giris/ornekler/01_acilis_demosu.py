"""
01_acilis_demosu.py
Amaç     : Python'un neler yapabildiğini göstermek. Kahve Durağı'nın 3 şubesinden
           gelen satış dosyalarını birleştirir ve gün sonu raporunu saniyeler
           içinde hazırlar.
Çalıştır : python 01_acilis_demosu.py
Çıktı    : Şube cirolarını, en çok satan ürünleri ve raporun kaç saniyede
           hazırlandığını ekrana yazar. Ayrıca bu klasörde demo_veri/ klasörünü
           ve gun_sonu_raporu.txt dosyasını oluşturur.

Not: Bu dosyayı Ders 1'de eğitmen gösterir. İçindeki yapıların hepsini
(değişkenler, döngüler, sözlükler, fonksiyonlar, dosya işlemleri) eğitim
boyunca tek tek öğreneceğiz. Şimdilik çalıştırın ve sonucu izleyin.
2. günün sonunda bu dosyayı satır satır okuyabiliyor olacaksınız.
"""

import csv
import random
import time
from pathlib import Path

# Dosyaların oluşturulacağı klasör: bu dosyanın yanındaki demo_veri/
KLASOR = Path(__file__).parent / "demo_veri"

# Dosya adlarında Türkçe karakter kullanmıyoruz, ekranda ise doğru yazıyoruz
SUBELER = {
    "kucukcekmece": "Küçükçekmece",
    "kadikoy": "Kadıköy",
    "besiktas": "Beşiktaş",
}

# Ürün adı: fiyat (TL)
MENU = {
    "Türk Kahvesi": 60,
    "Latte": 85,
    "Americano": 75,
    "Ice Latte": 95,
    "Limonata": 70,
    "Simit": 25,
    "Cheesecake": 120,
    "Kurabiye": 40,
}


def tl(tutar):
    """1234567 sayısını '1.234.567 TL' biçiminde yazar."""
    return f"{tutar:,.0f} TL".replace(",", ".")


def ornek_veri_olustur():
    """Her şube için bir günlük satış dosyası (CSV) üretir."""
    KLASOR.mkdir(exist_ok=True)
    rastgele = random.Random(19)  # Sabit başlangıç: her çalıştırmada aynı veri
    for dosya_adi in SUBELER:
        yol = KLASOR / f"{dosya_adi}_satislar.csv"
        with open(yol, "w", newline="", encoding="utf-8") as dosya:
            yazici = csv.writer(dosya)
            yazici.writerow(["saat", "urun", "adet"])
            for _ in range(rastgele.randint(80, 120)):
                saat = f"{rastgele.randint(8, 21):02d}:{rastgele.randint(0, 59):02d}"
                urun = rastgele.choice(list(MENU))
                adet = rastgele.randint(1, 3)
                yazici.writerow([saat, urun, adet])


def rapor_hazirla():
    """Üç şubenin dosyasını okur; şube cirolarını ve ürün satış adetlerini hesaplar."""
    sube_cirosu = {}
    urun_adedi = {}
    for dosya_adi, sube in SUBELER.items():
        with open(KLASOR / f"{dosya_adi}_satislar.csv", encoding="utf-8") as dosya:
            for satir in csv.DictReader(dosya):
                urun = satir["urun"]
                adet = int(satir["adet"])
                sube_cirosu[sube] = sube_cirosu.get(sube, 0) + adet * MENU[urun]
                urun_adedi[urun] = urun_adedi.get(urun, 0) + adet
    return sube_cirosu, urun_adedi


def raporu_yaz(sube_cirosu, urun_adedi):
    """Raporu satır satır hazırlar; hem ekrana hem dosyaya yazar."""
    satirlar = ["KAHVE DURAĞI · GÜN SONU RAPORU", "=" * 34, "", "Şube cirosu:"]
    for sube, ciro in sube_cirosu.items():
        satirlar.append(f"  {sube:<14}{tl(ciro):>14}")
    satirlar.append(f"  {'TOPLAM':<14}{tl(sum(sube_cirosu.values())):>14}")

    satirlar += ["", "En çok satan 3 ürün:"]
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
print(f"Rapor {sure:.3f} saniyede hazırlandı.")
print("Kaydedildi: gun_sonu_raporu.txt")

# ── DEĞİŞTİR VE DENE (Ders 2'den sonra) ─────────────────────────────
# 1) demo_veri/ klasöründeki CSV dosyalarından birini açıp inceleyin.
#    Excel'deki bir tabloya ne kadar benziyor?
# 2) MENU içinde Latte'nin fiyatını 100 yapın ve tekrar çalıştırın.
#    Hangi rakamlar değişti?
# 3) random.Random(19) satırındaki 19'u başka bir sayıyla değiştirin.
#    Neden bu sefer farklı bir rapor çıktı?
