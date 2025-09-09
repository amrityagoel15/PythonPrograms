# Prime number check in Python

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a Prime Number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is NOT a Prime Number")

print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
