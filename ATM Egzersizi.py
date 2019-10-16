print("""
*********************

ATM Programı

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

*********************

""")

B=1000
while True:
    i=input("İşlem Seçiniz")
    if(i=="q"):
        print("Kartınız İade Ediliyor....")
        break
    elif(i=="1"):
        print("Bakiye:{} TL".format(B))
    elif(i=="2"):
        print("Bakiye:{} TL".format(B))
        miktar=int(input("Çekmek İstediğiniz Miktarı Giriniz:"))
        
        while True:
            if(B>=miktar):
                B=B-miktar
                print("Bakiye:{} TL".format(B))
            else:    
                print("Bu Miktarda Para Çekemezsiniz Lütfen Başka Bir İşlem Deneyiniz.")
                break
        
    elif(i=="3"):
        print("Bakiye:{} TL".format(B))
        miktar=int(input("Yatırmak İstediğiniz Miktarı Giriniz:"))
        B=B+miktar
        print("Bakiye:{} TL".format(B))
    else:
        print("Geçersiz İşlem.Lütfen Geçerli Bir Tuşa Basınız.")



