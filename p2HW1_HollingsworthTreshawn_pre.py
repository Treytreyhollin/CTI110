print("This program calculates and displays travel expenses")
bu=int(input("Enter Budget:"))
lo=(input("Enter your travel destination:"))
ga=int(input("How much do you think you will spend on gas?"))
ac=int(input("Approximately, how much will you need for accomodation/hotel?"))
fo=int(input("Last, how much do you need for food?"))
print("----Travel Expenses----")
print(f"Location:{lo}")
print(f"Initial Budget:{bu}")

print(f"Fuel:{ga}")
print(f"Accomodation:{ac}")
print(f"Food:{fo}")

print("Remaining Balance:",bu-ga-ac-fo)
