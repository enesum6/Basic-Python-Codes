str1="Enes Menal"
type(str1)
print(str1[1:10:2])
print(str1[:-1])
list1=['abcd',786,2.23,'Ankara',78]
print(list1)
print(type(list1))
print(list1[0])
print(list1[0][0])
#print(list1[10])  İndex out of range hatası verir çünkü list1 dizisinde 10. eleman yoktur
#  print(list1[-1]) başında boşluk bıraktığımız için innedetaion hatası verir
list1[0]="Yasin"
print(list1)
#tuple[0]="abcd"
#print(list1) tuple değeri güncellenemezken list değeri güncellenebilir

dict={'a':1,'b':2,'c':3}
print(dict['b'])
