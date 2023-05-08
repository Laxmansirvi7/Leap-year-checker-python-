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

#  To be a leap year, the year must satisfy one of the following conditions:

# It is divisible by 4, but not by 100.
# It is divisible by 400.



# century lear like (1900, 2000, 2100, 2200, 2300, 2400)  %  400 = 0:
# non century year like (2004,1947,2024) % 4 = 0  then leap year

# 1900   = not divisible 
# 2000 = divisible 
# 2100 = not divisible 
# 2200 = not
# 2300 = not
# 2400 = yes divible  