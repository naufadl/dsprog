#user input
volume = int(input("Volume to be infused (ml): "))
menit = int(input("Minutes over which to infuse: "))
#menghitung
menit = menit / 60
rate = volume / menit
#output
print(f"""VTBI : {volume}ml
Rate : {rate}ml/hr""")