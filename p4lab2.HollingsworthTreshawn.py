def print_increments(start, end):
# Output the first integer
# Increment by 5 until the value is less than or equal to the second integer
if num2 < num1:
  print("Second integer can't be less than the first.", end="")
elif num1 ==num2:
  print(num1,end=" ")
else:
  print(start, end=" ")
while start + 5 <= end:
  start += 5
  print(start, end=" ")
# Input two integers
num1 = int(input())
num2 = int(input())
# Call the function with input integers
print_increments(num1, num2)
print()
# Print newline after outpu
