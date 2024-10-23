import numpy as np
import pandas as pd
import random

def oyunAlani():
    matris=np.zeros((10,10),dtype=int)

    mayin=0
    while mayin<15:
        x=random.randint(0,9)
        y=random.randint(0,9)
        if matris[x,y]!=-1:   #eğer mayın yoksa mayın koy
            matris[x,y]=-1
            mayin+=1
    return matris

#mayınların etradına komşu mayın sayısı yerleştirme

def komsuMayin(matris):
    for i in range(10):
        for j in range(10):
            if matris[i,j]==-1: #mayın olan hücreyi seç
                continue
            #komşu hücredeki mayınları sayma
            mayinSayisi=0
            for x in range(max(0,i-1), min(10,i+2)):
                for y in range(max(0,j-1),min(10,j+2)):
                    if matris[x,y]==-1:
                        mayinSayisi+=1
            matris[i,j]=mayinSayisi
    return matris

#matris oyun alanı oluştur komşu mayın sayılarını ekle



#oyun alanını Dataframe çevirme

#df=pd.DataFrame(gorunenAlan,columns=np.arange(10),index=np.arange(10))




def kullaniciGiris():
    while True:
        try:
            satir=int(input("Satır seççin(0-9):"))
            sutun=int(input("Sütun seççin(0-9):"))
            if 0<=satir<10 and 0<=sutun<10:
                return satir,sutun
            else:
                print("Lütfen 0 ile 9 arasında bir sayı seçiniz")

        except ValueError:
            print("Geçersiz giriş,lütfen sayı seçiniz")
#oyun durumunu kontrol etme ve hücre açma
def oyunuOyna(matris,gorunenAlan):
    while True:
        satir,sutun=kullaniciGiris()

        if matris[satir,sutun]==-1:
            print("Mayına bastınız. Oyun bitti...")
            gorunenAlan[satir,sutun]="*" #mayın olan hücre
            print(pd.DataFrame(gorunenAlan,columns=np.arange(10),index=np.arange(10)))
            break
        else:
            #seçilen hücre güvenliyse sayıyı göster
            gorunenAlan[satir,sutun]=matris[satir,sutun]
            print(pd.DataFrame(gorunenAlan,columns=np.arange(10),index=np.arange(10)))
        #oyuncu tüm güvenli hücreleri açarsa oyunu kazansın

        if np.count_nonzero(gorunenAlan==" ")==15: #15 mayın hariç tüm hücreler açık
            print("Tebrikler oyunu kazandınız!!!")
            break

matris=oyunAlani()
matris=komsuMayin(matris)

#başlangıçta tüm hücreler gizli (" " ile gösteriliyor)
gorunenAlan=np.full((10,10)," ",dtype=object)

#oyunu başlat
oyunuOyna(matris,gorunenAlan)
