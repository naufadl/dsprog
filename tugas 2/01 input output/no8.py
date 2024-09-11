#input
o = int(input("masukkan jumlah orang: "))
#menghitung toilet
t = o / 3
#menghitung air sekarang
airS = 15 * 14
total_sekarang = airS * t 
#menghitung air baru
airB = 2 / 14
total_baru = airB * t
#hemat brp
hemat = total_sekarang - total_baru
#biaya
biaya = 150
Tbiaya = t * biaya
#output 
print(f"""hemat air sebanyak {hemat}liter
total biaya pemasangan {Tbiaya}""")