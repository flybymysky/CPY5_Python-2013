#Name: Summing digits in an integer :D


integer = input("type in a number! :D")

if  int(integer) < 10:
    print(integer)

elif 10 <= int(integer) < 100:
    print(int(integer[0])+int(integer[1]))

elif 100 <= int(integer) <1000:
    print(integer[0]+integer[1]+integer[2])

end = input("press enter to end :)")

