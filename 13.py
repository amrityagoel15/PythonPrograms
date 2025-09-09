# Input date of birth
dob_day = int(input("Enter birth day: "))
dob_month = int(input("Enter birth month: "))
dob_year = int(input("Enter birth year: "))

# Input given date
g_day = int(input("Enter given day: "))
g_month = int(input("Enter given month: "))
g_year = int(input("Enter given year: "))

# Calculate age
age = g_year - dob_year

# Adjust if birthday not reached yet
if (g_month, g_day) < (dob_month, dob_day):
    age -= 1

print(f"\nYour age on {g_day}-{g_month}-{g_year} is: {age} years")
