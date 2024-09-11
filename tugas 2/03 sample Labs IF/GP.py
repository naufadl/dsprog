#input 
data = input("masukkan jarak maksimum, A ke Bee, Bee ke C, C ke D, D ke E>> ").split()
maks = int(data[0])
J1 = int(data[1])
J2 = int(data[2])
J3 = int(data[3])
J4 = int(data[4])

if J1 <= maks and J2 <= maks and J3 <= maks and J4 <= maks:
    print("YES HE CAN")
else:
    print("NO HE CAN'T")