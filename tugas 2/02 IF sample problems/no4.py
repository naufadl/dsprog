#input user
warna = input("huruf pertama warna tabung: ")

match warna.lower():
    case 'o':
        print("ammonia")
    case 'b':
        print("carbon monoxide")
    case 'y':
        print("hydrogen")
    case 'g':
        print("oxygen")
    case _:
        print("Contents unknown")