awal = int(input("masukkan awal deret:"))
akhir = int(input("masukkan akhir deret:"))
for i in range(awal,akhir):
    if i%2==1 and i%6!=0 and i%3!=0:
        print(i)


