#Treshawn Hollingsworth
#P2lab2
#4/24
#Put cars in a dictionary


print("The keys in thr dictionary are:")
print('Camero, prius, silverado, Model S')
Vehicle = {"Camero":18.21, 'Model S':110,'prius':52.36,'silverado':26}

name=input("Enter a vehicle to see it's mpg:")

print(f'The {name} gets {Vehicle[name]} mpg.')
mpg=Vehicle[name]

miles=float(input('How many miles are you going to drive with the'+name+":"))
fuel=miles/mpg

print(f'{fuel:.2f} gallons of gas are needed to drive the {name} {miles}')












         
