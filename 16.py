# Armstrong number check in Python

num = int(input("Enter a number: "))

# Convert number to string to count digits
num_str = str(num)
power = len(num_str)

# Calculate sum of digits raised to the power
armstrong_sum = sum(int(digit) ** power for digit in num_str)

# Check condition
if armstrong_sum == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is NOT an Armstrong Number")

print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
