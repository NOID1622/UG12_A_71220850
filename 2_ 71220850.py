name  = input("masukkan nama:")
add = 0
for i in range(len(name)):
    add += 1
    print(name[:add])
for i in range (len(name)):
    add -= 1
    print(name[:add])
