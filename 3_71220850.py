x = int (input("masukkan pembatas: "))
y = int(input("masukkan angka yang dilarang: "))
for i in range (x):
    if i == y:
        continue
    print(i, end='')