# Print all leap years from 1 to 2025

leap_years = []

for year in range(1, 2026):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_years.append(year)

print("Leap Years from 1 to 2025:")
print(leap_years)
print(f"\nTotal Count of Leap Years: {len(leap_years)}")
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
