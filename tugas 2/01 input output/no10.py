#input 
kecepatan = float(input("Masukkan kecepatan (km/jam): "))
jarak = float(input("Masukkan jarak (meter): "))
#diubah
kecepatan = kecepatan / 3.6
#hitung percepatan
percepatan = (kecepatan ** 2) / (2 * jarak)
#hitung waktu 
waktu = kecepatan / percepatan
#output
print(f"""percepatannya adalah {percepatan}
waktu yg diperlukan {waktu}detik""")