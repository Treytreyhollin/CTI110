#Treshawn Hollingsworth
#4/28
#pay in python


name=input('name of employee')
hours=float(input('Enter number of hours worked this week'))
rate=float(input('enter pay rate'))
print('----------------------------------------')

if hours >40:
    oth=hours-40
    otp=oth*(rate*1.5) 
    
else:
    otp=0
 
normpay=40*rate
tot_pay=normpay+otp
    
print('------------------------------------------------------------------------')
print(f'Employee name:{name}') 
print(f"{Hours worked:<5} {pay rate:<5} {overtime:<5} {overtime pay:<5} {regular hour pay:<5} {gross pay:<5}")
print('------------------------------------------------------------------------')
print(f'{hours:<5} {rate:<5} {oth:<5} {otp:<5} {normpay:<5} {tot_pay:<5}')

choice=done
choice=input('Enter employees name or "done" to terminate:')
count =0
while choice !='':

#counts user inputs
    count +=1

uinput=input("Enter employee's entered:")
print('The user entered', count, 'values')
choice=Done
