#Name: DETERMINE GRADE OF SCORE.
#Author: Ng Yi Jun Alan (NALA)
#Created: 6/2/2013
#Modified: 6/2/2013
#Description: Determine the grade of a score.

print("Determine Grade of Score")

restart="yes"
while restart=="yes":
    print()

    #Input Score
    Score= int(input("enter score for grade:"))
    while Score < 0 or Score >100:
        print("Invalid score! (0-100)")
        Score= int(input("re-enter score for grade:"))

    #Grade
    Grade=[[100, 70, "A"], [69, 60, "B"], [59, 55, "C"],
            [54, 50, "D"], [49, 45, "E"], [44, 35, "S"], [34, 0, "U"]]

    #Print Grade
    for scoring in Grade:
        if scoring[0] >= Score >= scoring[1]:
            print("Grade=",scoring[2])
        
    restart= input("Do you want to try again(yes/no)?")




