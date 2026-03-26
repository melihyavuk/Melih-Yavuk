# 3. Hafta: Kick Boks Veri Seti Oluşturma ve Görselleştirme

Bu proje, kick boks sporcularının performans ve yenilgi istatistiklerini rastgele olarak üreten ve daha sonra bu verileri görselleştiren Python betiklerinden oluşmaktadır. 

## Dosyalar ve İşlevleri

1. **`generate_data.py`**:
   - 500 sporcunun bulunduğu bir veri seti (`data.csv`) oluşturur.
   - **Sütunlar**:
     - **Kimlik:** 1'den 500'e kadar olan numaralar.
     - **Performans Puanı:** 0 ile 100 arasında normal dağılıma (çan eğrisi) sahip puan değerleri. (Ortalama 50, Standart Sapma 15)
     - **Yenilgi Durumu:** Performans puanına göre belirlenen yenilgi ihtimaliyle üretilmiş `0` (Kazandı) veya `1` (Yenildi) değerleri.

2. **`visualize_data.py`**:
   - Oluşturulmuş olan `data.csv` dosyasını okur.
   - Matplotlib aracılığıyla istatistiksel tespitler yapar ve sonuçları `grafikler.png` olarak kaydeder.
   - Grafikler:
     1. Performans puanı frekansını gösteren **Histogram**.
     2. Yenilgi durumuna göre ayrılmış performans puanları aralığını gösteren **Kutu Grafiği (Boxplot)**.

3. **`data.csv`**:
   - Betik tarafından otomatik olarak oluşturulan ve kaydedilen oyuncu verileri tablosu.

4. **`grafikler.png`**:
   - Görselleştirme kodunun çalışmasının ardından ortaya çıkan resim/grafik çıktısı.

5. **`prompt.md`**:
   - Uygulamanın geliştirilmesi sırasındaki yönlendirmeleri veya talimatları özetleyen bir doküman.

## Kullanım Kılavuzu

### 1. Kütüphanelerin Kurulumu
Bilgisayarınızda `numpy`, `pandas` ve `matplotlib` kurulu değilse, komut istemi/terminalde şu komutu kullanarak indirebilirsiniz:
```bash
pip install numpy pandas matplotlib
```

### 2. Kodların Çalıştırılması
İlk olarak verileri oluşturmanız gerekir. Komut satırında şu komutu çalıştırın:
```bash
python generate_data.py
```
*Bu komutun tamamlanmasıyla klasörünüze `data.csv` belirecektir.*

Veri analizi ve grafikleri oluşturmak için ise ardından şu satırı çalıştırın:
```bash
python visualize_data.py
```
*Bu komut sonrasında ise `grafikler.png` dosyasının klasöre eklendiğini görebilirsiniz.*
