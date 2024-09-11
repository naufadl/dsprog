#user input
n = float(input("data used: "))

if 0.0 < n <= 1.0:
    print("bayar 250")
elif 1.0 < n <= 2.0:
    print("bayar 500")
elif 2.0 < n <= 5.0:
    print("bayar 1000")
elif 5.0 < n <= 10.0:
    print("bayar 1500")
elif n > 10.0:
    print("bayar 2000")
else:
    print("data tidak valid")