print("menghitung BMI")
#user input
jenisB = input("kg/pounds?")
jenisT = input("cm/inch?")
berat = float(input("masukkan berat: "))
tinggi = float(input("masukkan tinggi: "))
#menghitung 
if jenisB == 'pounds' and jenisT == 'inch':
    BMI = 703 * berat / tinggi ** 2
    BMI = float(BMI)
else:
    BMI = berat / (tinggi / 100) ** 2 
    BMI = float(BMI)

if BMI < 18.5:
    print("underweight")
elif 18.5 < BMI < 24.9:
    print("normal")
elif 25.0 < BMI < 29.9:
    print("overweight")
else:
    print("obese")