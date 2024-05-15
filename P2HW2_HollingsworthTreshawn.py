#Treshawn Hollingsworth
#4/21/24
#P2hw2
#Creating a program that displays your grades, adds them, and averages them
print("How many scores do you want  to enter?")
m1=float(input("Enter score #1:"))
m2=float(input("Enter score #2:"))

grade=[]
grade.append(m1)
grade.append(m2)
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
    
