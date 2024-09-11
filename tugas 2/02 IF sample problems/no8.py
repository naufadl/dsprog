print(f"""(1) First Free Service 
(2) Second Free Service""")
#user input
FSnumber = int(input("Enter the Free Service number>>"))
miles = int(input("Enter number of Miles>>"))

if FSnumber == 1:
    if 1500 < miles <= 3000:
        print("Vehicle must be serviced")
    else:
        print("Vehicle doesn't need servicing")
elif FSnumber == 2:
    if 3001 < miles <= 4500:
        print("Vehicle must be serviced")
    else:
        print("Vehicle doesn't need servicing")
else:
    print("invalid service number")