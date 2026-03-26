import numpy as np
import pandas as pd
import os

def create_dataset():
    # 500 sporcu
    n_athletes = 500
    
    # 1. Kimlik sütunu (1'den 500'e kadar)
    kimlik = np.arange(1, n_athletes + 1)
    
    # 2. Performans Puanı 
    # Normal dağılıma (çan eğrisi) uygun rastgele sayılar (Ortalama: 50, Standart Sapma: 15)
    performans = np.random.normal(loc=50, scale=15, size=n_athletes)
    # Puanı 0 ile 100 arasında sınırlandırıyoruz
    performans = np.clip(performans, 0, 100)
    # Virgülden sonra iki basamak olacak şekilde yuvarlama
    performans = np.round(performans, 2)
    
    # 3. Yenilgi Durumu
    # Yüksek performans = kazanma (yenilgi = 0)
    # Düşük performans = yenilgi (yenilgi = 1)
    # Performans puanına bağlı olarak yenilgi ihtimalini hesaplıyoruz (performans düştükçe yenilgi ihtimali artar)
    yenilgi_ihtimali = 1 - (performans / 100.0)
    rastgele_degerler = np.random.rand(n_athletes)
    
    # Eğer rastgele üretilen değer yenilgi ihtimalinden küçükse 1 (yenilgi), büyükse 0 (kazanma)
    yenilgi_durumu = (rastgele_degerler < yenilgi_ihtimali).astype(int)
    
    # Pandas DataFrame oluşturma
    df = pd.DataFrame({
        'Kimlik': kimlik,
        'Performans Puanı': performans,
        'Yenilgi Durumu': yenilgi_durumu
    })
    
    # Dosyanın kaydedileceği yolu ayarlama (betiğin bulunduğu klasör)
    dosya_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
    
    # data.csv olarak kaydetme
    df.to_csv(dosya_yolu, index=False)
    print(f"Veri seti başarıyla oluşturuldu: {dosya_yolu}")

if __name__ == '__main__':
    create_dataset()
