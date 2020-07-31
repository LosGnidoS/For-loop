#!/usr/bin/python3
#created by Kirill Shvedov

from collections import Counter

names = ["Johg", "Kirill", "James",
 "Andrew", "Dasha", "Parker"]

for name in names:
	if name == "John":
		print(name)
		break

	else:
		print("Nothing found...")
		break

me = ("Kirill", "Shvedov", 22) 
tien = ("Tien","Tien", None) 
omega = ("Omega","Omega", 41) 
marion = ("Marion","Marion", 41) 
dionna = ("Dionna","Dionna", None) 
elise = ("Elise","Elise", 42) 
amparo = ("Amparo","Amparo", None) 
janetta = ("Janetta","Janetta", 41) 
leslee = ("Leslee","Leslee", 54) 
wendi = ("Wendi","Wendi", 32) 
chantell = ("Chantell","Chantell", None) 

names = [me, tien, omega, marion, dionna, elise,
 amparo, janetta, leslee, wendi, chantell]

#sorting out the tuples for the 2 element.
age = [me[2],tien[2],omega[2],marion[2],dionna[2],
elise[2],amparo[2],janetta[2],leslee[2],wendi[2],
chantell[2]]

#summing up age in tuples
result = 0
for i in age:
	if i == None:
		continue
	result += i
print(result)

#Function to determine the number of itirations.
x = Counter(age)
None_number = (x[tien[2]])

#AGE - number of None elements
Number_age = (len(age)) - None_number
print(Number_age)

#Average age in tuples
average_age = result / Number_age
print(int(average_age))


#OLD OR YOUNG in list[age]
for i in age:
	if i == None:
		continue
	elif i >= 40:
		print("Old")
	else:
		print("Young")
		








#average_age = result / len[age]

#result = 0
#for age in names:
#		result += age
#		print(result)
