print("taxi fare")
#user input
odometer_awal = int(float(input("Enter beginning odometer reading: ")))
odometer_akhir = int(float(input("Enter ending odometer reading: ")))
#menghitung jarak
jarak = odometer_akhir - odometer_awal
#menghitung ongkos 
harga_permil = 1.50 
ongkos = jarak * harga_permil
ongkos = round(ongkos,2)
#output
print(f"You traveled a distance of {jarak} miles. At $1.50 per mile, your fare is ${ongkos}")