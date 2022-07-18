# Interactive Image
# Steven Dai Chuy
# March 15. 2021
# Takes option of input from user and output the changes as a new image

import cmpt120imageWeek9
import cmpt120imageManip

option = True

while option == True:

  img = cmpt120imageWeek9.getImage("week9-photo.jpg")

  user_input = input("\nMenu\n Please choose what you want to do with the image\n 0: Exit the program\n 1: Show the orginal image\n 2: Set all red pixels to 0\n 3: Gray scale the image \n 4: Flip the whole image\nChoose 0-4: ").strip(" ")
  if user_input == "0":
    print("See you next time!")
    option = False
  
  elif user_input == "1":
    new_img = cmpt120imageWeek9.getImage("week9-photo.jpg")
    cmpt120imageWeek9.saveImage(new_img,"Original_output.jpg")
    option = True

  elif user_input == "2":
    new_img = cmpt120imageManip.removeRed(img)
    cmpt120imageWeek9.saveImage(new_img,"removedRed_output.jpg")
    option = True

  elif user_input == "3":
    new_img = cmpt120imageManip.greyScale(img)
    cmpt120imageWeek9.saveImage(new_img,"greyScale_output.jpg")
    option = True

  elif user_input == "4":
    new_img = cmpt120imageManip.flipVertical(img)
    cmpt120imageWeek9.saveImage(new_img,"Flipped_output.jpg")
    option = True

  else:
    print("Sorry I don't understand",user_input,) 
    option = True

