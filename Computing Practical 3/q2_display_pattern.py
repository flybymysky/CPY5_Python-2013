#filename = q2_display_pattern.py
# author = Ng Yi Jun Alan (NALA) :D

def display_pattern(n):
    digits = []
    for i in range(1, n+1):
        digits.append(str(i))
        length=len(" ".join(digits))
    digits = []
    for j in range(1, n+1):
            digits.append(str(j))
            print(" ".join(digits[::-1]).rjust(length))
        
#main
integer=int(input("Input integer for pattern:"))
display_pattern(integer)

print()
print("Press enter to exit.")
