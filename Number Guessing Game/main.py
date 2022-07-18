import random

comp_num = random.choice(range(1,100)

repeat = True 
tries = 7
user = int(input("Enter a number between 1-100: ")                         
while repeat:
    if comp_num > user:
           print("Higher. Try Again.)
           tries--
    if comp_num < user:
           print("Lower, Try Again.)
           tries--
    elif comp_num == user:
           print("You got the number {}",.format(comp_num))
                 
    if tries == 0
           print("You ran out of tries. The number was {}".format(comp_num))
           repeat = False      
