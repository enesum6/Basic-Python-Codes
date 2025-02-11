try:
    sayi1=input("ilk sayiyi girin: ")
    sayi2=input("ilk sayiyi girin: ")
    sonuc=int(sayi1)/int(sayi2)
    print(sonuc)
    
except ValueError:
    print("yanlis deger")
except ZeroDivisionError:
    print("0'a bölme yapamazsınız")
finally:
    print("işlem gerçekleştirildi")