#user input
jam = int(input("masukkan jam: "))
menit = int(input("masukkan menit: "))
menit = menit / 60
#menghitung waktu
t = jam + menit
#menghitung suhu
T = 4 * t ** 2 / ( t + 2) - 20
#output
print(f"dengan waktu {t}, suhunya {T}")