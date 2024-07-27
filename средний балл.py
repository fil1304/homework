grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=list(students)
a.sort()
print(a)
dlina1=len(grades[0])
dlina2=len(grades[1])
dlina3=len(grades[2])
dlina4=len(grades[3])
dlina5=len(grades[4])

nur1= sum(grades[0])/dlina1
nur2= sum(grades[1])/dlina2
nur3= sum(grades[2])/dlina3
nur4= sum(grades[3])/dlina4
nur5= sum(grades[4])/dlina5
print(nur1, nur2, nur3, nur4, nur5)
b={'Aaron':4.0,'Bilbo' : 2.25, 'Johnny':4.0, 'Khendrik':3.6666666666666665, 'Steve': 4.8}
print(b)