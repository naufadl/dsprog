#input
n = int(input("masukkan angka (2 <= n <= 1000): "))

if n <= 1:
    print("IT IS NOT A PRIME")
elif n == 2:
    print("IT IS A PRIME")
elif n % 2 == 0:
    print("IT IS NOT A PRIME")
else: 
    prima = True
    for N in range(3, int(n ** 0.5) + 1, 2):
        if n % N == 0:
            prima = False
            break
    if prima:
        print("IT IS A PRIME")
    else:
        print("IT IS NOT A PRIME")