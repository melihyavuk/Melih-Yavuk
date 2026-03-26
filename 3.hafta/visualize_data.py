import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize():
    dosya_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.csv')
    
    if not os.path.exists(dosya_yolu):
        print("data.csv bulunamadı! Lütfen önce generate_data.py dosyasını çalıştırın.")
        return

    # Veriyi okuma
    df = pd.read_csv(dosya_yolu)
    
    # 2 Alt grafikli (subplots) bir şekil oluşturma
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1. Grafik: Performans Puanı Dağılımı (Histogram)
    axes[0].hist(df['Performans Puanı'], bins=20, color='skyblue', edgecolor='black')
    axes[0].set_title('Performans Puanı Dağılımı')
    axes[0].set_xlabel('Performans Puanı')
    axes[0].set_ylabel('Frekans')
    
    # 2. Grafik: Yenilgi Durumuna Göre Performans (Kutu Grafiği / Boxplot)
    kazananlar = df[df['Yenilgi Durumu'] == 0]['Performans Puanı']
    yenilenler = df[df['Yenilgi Durumu'] == 1]['Performans Puanı']
    
    # Matplotlib için liste halinde verileri veriyoruz
    axes[1].boxplot([kazananlar, yenilenler], tick_labels=['0 (Kazandı)', '1 (Yenildi)'])
    axes[1].set_title('Yenilgi Durumuna Göre Performans')
    axes[1].set_xlabel('Yenilgi Durumu')
    axes[1].set_ylabel('Performans Puanı')
    
    plt.tight_layout()
    
    # Grafiği kaydetme işlemi
    kayit_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'grafikler.png')
    plt.savefig(kayit_yolu, dpi=300)
    print(f"Grafikler başarıyla kaydedildi: {kayit_yolu}")

if __name__ == '__main__':
    visualize()
