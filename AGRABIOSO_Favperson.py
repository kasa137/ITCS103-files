import openpyxl as unak
workbook = unak.Workbook()
sheet = workbook.active

fav = []
fav1 = []
fav2 = []

print(" Person 1")
#filename1 = "person1.xlsx"

fname1 = input("First Name : ")
lname1 = input("Last Name : ")
year1 = eval(input("Birthyear : "))

yearb1 = 2026 - year1

sheet['A1'] = "first name"
sheet['B1'] = "Last name"
sheet['c1'] = "Age"
sheet['A2'] = fname1
sheet['B2'] = lname1
sheet['C2'] = yearb1
#workbook.save("person1.xlsx")


#\n
print("\n Person 2")
filename2 = "person3.xlsx"

fname2 = input("First Name : ")
lname2 = input("Last Name : ")
year2 = eval(input("Birthyear : "))

yearb2 = 2026 - year2

sheet['A1'] = "first name"
sheet['B1'] = "Last name"
sheet['c1'] = "Age"
sheet['A2'] = fname2
sheet['B2'] = lname2
sheet['C2'] = yearb1
#workbook.save("person2.xlsx")

print("\n Person 3")
filename3 = "person3.xlsx"

fname3 = input("First Name : ")
lname3 = input("Last Name : ")
year3 = eval(input("Birthyear : "))

yearb3 = 2026 - year3

sheet['A1'] = "first name"
sheet['B1'] = "Last name"
sheet['c1'] = "Age"
sheet['A2'] = fname3
sheet['B2'] = lname3
sheet['C2'] = yearb1
workbook.save("person3.xlsx")

def show():{
fav.append(fname1),
fav.insert(1 ,lname1),
fav.insert(2,year1),
fav.insert(3,yearb1),
print(fav),

fav1.append(fname2),
fav1.insert(1,lname2),
fav1.insert(2,year2),
fav1.insert(3,yearb2),
print(fav1),

fav2.append(fname3),
fav2.insert(1,lname3),
fav2.insert(2,year3),
fav2.insert(3,yarb3),
print(fav2),

}

#fav.append(fname2,lname2,year2,yearb2)
#fav.append(fanme3,lname3,yaer3,yearb3)

print("~~~~~* Fav Person *~~~~~~")
print(show)

