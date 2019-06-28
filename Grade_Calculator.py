'''
Author: Sohrab Ganjian
git: https://github.com/sohrabganjian

This program will convert the grade of your assignments
to a number out of 100
'''

#===================Functions===========================:

def val_input (question):
    res = input(question)
    while res.lower() not in ["y","n"]:
        print("What you typed is not what is expected, please retype")
        res = input(question)
    return res.lower()

#===========================TOP LEVEL==========================:
print ("        Welcome to grade calculator    ")
print("=" * 50)

print ()

print ("IMPORTANT: YOU HAVE TO ADD THE TOTAL MARKS YOURSELF!!!\n"
       "THIS PROGRAM WILL ONLY GIVE YOU THE MARK YOU GET FOR\n"
       "FOR EACH ASSIGNMENT!")

print ()

want_to_calculate = val_input("Do want to calculate your grades? type 'y' for yes and 'n' for no: ")

print ()

while want_to_calculate == "y":
    print ("Now you will be asked to provide your mark OUT OF 100% for that assignment!")
    assignment_mark = float(input("Please enter the mark you got for your assignment: "))
    print ()
    worth = float(input("How much this assignment was worthed? "))
    print ()
    mark_out_of100 = (assignment_mark * worth)/100
    print ("You got", mark_out_of100, "for this assignment out of 100.")
    print ()
    want_to_calculate = val_input("Do you want to calculate another mark? type 'y' for yes and 'n' for no: ")

print ("Thanks for using the grade calculator!\n"
       "See you next time")

     
