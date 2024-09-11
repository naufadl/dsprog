#user input
tinggi = int(input("masukkan tinggi(m): "))
volume_air_mengalir = int(input("masukkan volume air(m^3/s): "))
#menghitung usaha
massa = volume_air_mengalir / 1000
gravitasi = 9.80 
usaha = massa * gravitasi * tinggi
#menghitung listrik yang dihasilkan
listrik = usaha * 0.9 
listrik = listrik / 10 ** 6
listrik= round(listrik,2)
#output
print(f"energi listrik yang dihasilkan {listrik}")