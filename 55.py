def fibonacci(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b

for num in fibonacci(10):
    print(num)

print("This program is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
