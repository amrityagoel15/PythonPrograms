def count_up_to(max):
    count=1
    while count<=max:
        yield count
        count+=1

def squared_numbers(numbers):
    for number in numbers:
        yield number**2

for square in squared_numbers(count_up_to(5)):
    print(square)

print("This program is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
