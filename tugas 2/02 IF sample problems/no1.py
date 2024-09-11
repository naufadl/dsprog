#user input 
a = input("apakah anda mahasiswa?(iya/tidak)")
tp = float(input("total pembelian: "))
#info
diskon = 0.20
pajak = 0.05

if a == 'iya' :
    d = tp * diskon
    d = round(d,2)
    hargad = tp - d
    hargad = round(hargad,2)
    p = hargad * pajak
    p = round(p,2)
    total = hargad + p
    total = round(total,2)
    print(f"""Total purchases ${tp}
Student’s discount (20%) {d}
Discounted total {hargad}
Sales tax (5%) {p}
Total {total}""")
else :
    p = tp * pajak
    p = round(p,2)
    total = tp + p
    total = round(total,2)
    print(f"""Total purchases ${tp}
Sales tax (5%) {p}
Total {total}""")