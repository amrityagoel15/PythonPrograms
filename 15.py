# Check perfect number in Python

num = int(input("Enter a number: "))

# Find sum of divisors
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

# Check condition
if sum_of_divisors == num:
    print(f"{num} is a Perfect Number ")
else:
    print(f"{num} is not a Perfect Number ")

print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
