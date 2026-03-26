# 3. Hafta Görevleri

## Görev 1: `generate_data.py` (Veri Seti Oluşturma)
Bu kod, kick boks sporcularının performans verilerini oluşturup `data.csv` olarak kaydeder.
- 500 sporcunun verisi bulunur.
- **Kimlik:** 1'den 500'e kadar gider.
- **Performans Puanı:** Normal dağılıma (çan eğrisi) uygun rastgele sayılardır.
- **Yenilgi Durumu:** Performans puanına bağlı olarak 0 (kazanma) veya 1 (yenilgi) değerleri üretilir.
- `numpy` ve `pandas` kullanılır.

## Görev 2: `visualize_data.py` (Görselleştirme)
Bu kod `data.csv` okuyarak grafikler oluşturur ve `grafikler.png` dosyasını çizer.
- Performans puanının çan eğrisi dağılımını (Histogram).
- Yenilgi durumuna göre performans puanı değişimini (Kutu grafiği) gösterir.
- Kod çalıştırıldığında çıktı direkt PNG olarak kaydedilir.
