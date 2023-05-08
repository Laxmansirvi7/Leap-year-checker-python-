year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

 """
 To be a leap year, the year must satisfy one of the following conditions:

It is divisible by 4, but not by 100.
It is divisible by 400.
"""

"""
Century years like (1900, 2000, 2100, 2200, 2300, 2400) are leap years if they are divisible by 400.
Non-century years like (2004, 1947, 2024) are leap years if they are divisible by 4.

Examples:
- 1900 is not a leap year because it is not divisible by 400.
- 2000 is a leap year because it is divisible by 400.
- 2100 is not a leap year because it is not divisible by 400.
- 2200 is not a leap year because it is not divisible by 400.
- 2300 is not a leap year because it is not divisible by 400.
- 2400 is a leap year because it is divisible by 400.
"""
