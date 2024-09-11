#input
N = int(input("masukkan angka(-100000 <= n <= 100000) >>"))

if -100000 <= N <= 100000:
    if '4' in str(N):
        print("SEVER")
    else:
        print("UNITE")
else:
    print("gaada")