#Treshawn Hollingsworth
#4/21/24
#P3HW1
#Creating a program that displays your grades, adds them, and averages them
print("Enter info below")
m1=float(input("Enter grade for module 1:"))
module2=float(input("Enter grade for module 2:"))
m3=float(input("Enter grade for module 3:"))
m4=float(input("Enter grade for module 4:"))
m5=float(input("Enter grade for module 5:"))
m6=float(input("Enter grade for module 6:"))

grade=[]
grade.append(m1)
grade.append(module2)
grade.append(m3)
grade.append(m4)
grade.append(m5)
grade.append(m6)

print("------------RESULTS------------")
print(f' Highest grade: {max(grade)}')
print(f'Lowest grade: {min(grade)}')
print (f'Sum of grade: {sum(grade)}')
avg= sum(grade) / 6
print (f'Average:{avg}:')
print('--------------------------------------')

if avg >=90:
    print('Your grade is: A')
if avg< 90 and avg >= 80:
    print('Your grade is: B')
if avg< 80 and avg >= 70:
    print('Your grade is: C')
if avg< 70 and avg >= 60:
    print('Your grade is: C')
    
