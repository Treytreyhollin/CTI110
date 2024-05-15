#TReshawn Hollingsworth
#5/10/24
#P5L



import random

    

def disperse_change(dollars, change):

    num_quarters = change // .25
    change = change - num_quarters * .25
       
    num_dimes = change // .10
    change = change - num_dimes * .10
       
    num_nickels = change // .5
    change = change - num_nickels * .5
    
    num_pennies = round(change,2)
    
    if (dollars > 0):
        print(dollars, end='')
        if (dollars == 1):
            print(' Dollar')
        else:
            print(' Dollars')
    if (num_quarters > 0):
        print(num_quarters, end='')
        if (num_quarters == 1):
            print(' Quarter')
        else:
            print(' Quarters')
    if (num_dimes > 0):
        print(num_dimes, end='')
        if (num_dimes == 1):
            print(' Dime')
        else:
            print(' Dimes')
    if (num_nickels > 0):
        print(num_nickels, end='')
        if (num_nickels == 1):
            print(' Nickel')
        else:
            print(' Nickels')
    if (num_pennies > 0):
        print(num_pennies, end='')
        if (num_pennies == 1):
            print(' Penny')
        else:
            print(' Pennies')


def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print("You owe us: ", owed)
    cash = float(input("How much cash will give to us: "))

    change = cash - owed
    print(change)
    if change > 0:  

        dollars = int(change)
    

    # remaining change
    change = round(change - dollars,2)
        #print(change)
    print("Change is: ", round(change , 2))  # Print change rounded to 2 decimal places
    disperse_change(dollars,change)
    


if __name__ == "__main__":

     main()

    

