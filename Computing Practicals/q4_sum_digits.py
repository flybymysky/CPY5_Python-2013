integer = int(input("enter integer:"))

sumofdigits = 0
while integer > 0:
    sumofdigits = sumofdigits + integer%10
    frontnumbers = integer//10
    integer = frontnumbers

print(sumofdigits)

