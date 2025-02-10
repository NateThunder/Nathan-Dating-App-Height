# I like to learn with silly examples, trying to do it as fast as I can.
# This code describes percieved height on dating apps 

#define gender
gender = input("What is your gender? M = Male F = Female and O = Other ").capitalize()
#and statement used rather than or statement to break the code is invalid input
if gender != "M" and gender != "F" and gender != "O":
    print("Wait a minuit... That is not an option!")
    exit()
#define orientation
orient = input("What is you orientation S = Streight G = Gay B = By ").capitalize()
if orient != "S" and orient != "G" and orient != "B":
    print("Wait a minuit... That is not an option!")
    exit()
#define height in fee first
print("You will now be asked your height firsly in feet, then in inches.\n")
height = int(input('Feet= '))
inches = int(input("Inches = "))

#For stright men

if gender == "M" and orient =="S":
    if height >= 6 and inches >= 0:
        print("You are tall! Well done!")
    else:
        print("You are short")
#For gay men:
elif gender == "M":
    if orient == "G":
        print("You are as tall as you need to be!")
#For streight female
elif gender == "F":   
#Orientation does not really matter in this category    
    if height >= 6:
        print("You are a very tall girl")
    if height >= 5:
        if inches >=9:
            print("You are a tall girl")
        elif inches > 9 or inches >= 4:
            print("you are average heaight")
        elif inches < 4:
            print("You are quite short")
    if height < 5:
        print("You are very short! ")
#For others
elif gender ==  "O":
    print("You are encelent in every way!")
