#Name: Python BMI CALCULATHOR.
#Author: Nala
#Created: 1/21/2013
#Modified: 1/24/2013
#Description: BMI python CalculaThor.

# main
restart = "yes"
while restart == "yes":

    # prompt and get weight
    weight = int(input("enter weight/kg here!"))

    # prompt and get height
    height = float(input("enter height/m here!"))

    # calculate BMI
    BMI = weight / (height*height)

    # display result
    print ("this is your BMI!", "bmi = {0:.2f}".format(BMI))

    # determine Health risk
    if 18.5 < BMI < 27.5 :
        print ("health alright!!")
    elif BMI >= 27.5:
        print ("HIGH RISK HEALTH!")
    else :
        print ("risk of nutritional deficiency diseases and osteoporosis")

    restart = input("Do you want to try again (yes/no)?")



