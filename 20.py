# Perfect numbers from 1 to 2025

perfect_numbers = []

for n in range(1, 2026):
    if sum(i for i in range(1, n) if n % i == 0) == n:
        perfect_numbers.append(n)

print("Perfect Numbers from 1 to 2025:")
print(perfect_numbers)
print(f"\nTotal Count of Perfect Numbers: {len(perfect_numbers)}")
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
