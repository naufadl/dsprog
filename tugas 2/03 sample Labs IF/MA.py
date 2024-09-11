#input 
data = input("berapa jumlah mobil di depan, di belakang, dan waktu ?").split()
M = int(data[0])
N = int(data[1])
T = int(data[2])
#waktu lampu
merah = 20
kuning = 5
hijau = 60
totalw = merah + kuning + hijau
#jumlah mobil yang lewat saat lampu hijau
mobil_LH = hijau // 5
#hitung siklus
full = T // totalw
sisa = T % totalw
#hitung yg lewat selama sisa 
if sisa > merah + kuning:
    Shijau = sisa - (merah + kuning)
    mobil_lewat = Shijau // 5
else:
    mobil_lewat = 0
#mobil lewat selama lampu T
totalm = totalw * mobil_LH + mobil_lewat
#mobil sisa 
Tmobil = M + N 
Smobil = Tmobil - totalm
#hasil 
if Smobil > 0:
    if Smobil <= 0:
        print(f"YES! {Smobil}")
    else: 
        print(f"NO! {Smobil}")
else:
    print(f"YES! {Smobil}")
