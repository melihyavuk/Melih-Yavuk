import numpy as np
import pandas as pd
import os

def create_dataset():
    np.random.seed(42) # Tekrar üretilebilirlik için
    n_athletes = 500
    
    kimlik = np.arange(1, n_athletes + 1)
    
    performans = np.random.normal(loc=50, scale=15, size=n_athletes)
    performans = np.clip(performans, 0, 100)
    performans = np.round(performans, 2)
    
    yenilgi_ihtimali = 1 - (performans / 100.0)
    rastgele_degerler = np.random.rand(n_athletes)
    yenilgi_durumu = (rastgele_degerler < yenilgi_ihtimali).astype(int)
    
    df = pd.DataFrame({
        'Kimlik': kimlik,
        'Performans Puanı': performans,
        'Yenilgi Durumu': yenilgi_durumu
    })
    
    dosya_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
    df.to_csv(dosya_yolu, index=False)
    print(f"Veri seti başarıyla oluşturuldu: {dosya_yolu}")

if __name__ == '__main__':
    create_dataset()
