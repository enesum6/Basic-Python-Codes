#bir sayının tam bölenlerinin toplamını bulma
number2=int(input("Enter a value:"))
toplam=0
for x in range(1,number2):
    if(number2%x==0):
        toplam+=x


print(toplam)