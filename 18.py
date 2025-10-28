# Simple program to print Prime, Perfect and Armstrong numbers in a range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

primes, perfects, armstrongs = [], [], []

for n in range(start, end + 1):
    # Prime check
    if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        primes.append(n)

    # Perfect check
    if n > 1 and sum(i for i in range(1, n) if n % i == 0) == n:
        perfects.append(n)

    # Armstrong check
    s = str(n)
    if sum(int(d) ** len(s) for d in s) == n:
        armstrongs.append(n)

print("Primes:", primes)
print("Perfects:", perfects)
print("Armstrongs:", armstrongs)


print("This code is written and excecuted by AMRITYA GOEL with ERP 0231BCA175")

