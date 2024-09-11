#user input
a = input("Enter desired grade: ")
b = int(float(input("Enter minimum average required: ")))
c = int(float(input("Enter current average in course: ")))
d = int(float(input("Enter how much the final counts as a percentage of the course grade: "))) 
d = d / 100
#kontribusi c
kontribusi = c * (1 - d)
#nilai yg harus ditutup
tutup = b - kontribusi
#nilai yg harus didapatkan
nilai = tutup / d
print(f"You need a score of {nilai} on the final to get a {a}.")