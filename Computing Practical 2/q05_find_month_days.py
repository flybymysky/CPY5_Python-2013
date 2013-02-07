#Name: DAYS IN MONTH OF YEAR.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/6/2013
#Modified: 2/6/2013
#Description: Find days in a certain month of a certain year.

print("Enter month and year for the no. of days for that month :D")

restart="yes"
while restart=="yes":
    print()

    #Provide onth and Year
    month = int(input("input month:"))
    year =int(input("input year:"))

    #Month names and days List
    monthnames = ["January", "February", "March", "April", "May", "June", "July",
                 "August", "September", "October", "November", "December"]
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31,]

    #Print no. of days for Month
    #(for February in Leap Year)
    if year%4 ==0 and month==2:
        print(monthnames[month-1],year,"has",int(monthdays[month-1])+1,"days")
    else:
        print(monthnames[month-1],year,"has",monthdays[month-1],"days")

    print()
    restart = input("do you want to try again? (yes/no)")
        
    
    


