#user input waktu streaming
Wstreaming = input("masukkan waktu streaming (HH:MM:SS)>> ")
Wstreaming = Wstreaming.split(':')
WSt_jam = int(Wstreaming[0])
WSt_menit = int(Wstreaming[1])
WSt_detik = int(Wstreaming[2])
#user input waktu saat ini
Wsekarang = input("masukkan waktu sekarang (CH:CM:CS)>> ")
Wsekarang = Wsekarang.split(':')
WSk_jam = int(Wsekarang[0])
WSk_menit = int(Wsekarang[1])
WSk_detik = int(Wsekarang[2])
#mengubah menjadi detik
DWstreaming = (WSt_jam * 3600) + (WSt_menit * 60) + WSt_detik
DWsekarang = (WSk_jam * 3600) + (WSk_menit * 60) + WSk_detik
#sesuaikan
Wstreaming_sesuai = DWstreaming + (5 * 3600)
#selisih 
selisih = Wstreaming_sesuai - DWsekarang
if selisih < 0:
    print("see u on the next pear event!")
else:
    Jtunggu = selisih // 3600
    Mtunggu = (selisih % 3600) // 60
    Dtunggu = selisih % 60 
    print(f"{Jtunggu}:{Mtunggu}:{Dtunggu}")