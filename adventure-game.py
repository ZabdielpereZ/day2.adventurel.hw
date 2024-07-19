# hw fix this adveture game! 


# place = input("Choose a place: forest or cave? ")

# if place = "forest":
    # action = input("climb a tree or cross a river?")
    # if action = "climb a tree":
       # print("You found a bird's nest!")
    # else action = "cross a river":
       # print("You found a boat!")
# elif place = "cave":
   # print("You find a hidden treasure!")



#-----------------#
# first attempt

# place = input("Choose a place: (f)orest or (c)ave? ")

# if place == "f":
  #  action = input("climb a tree (t) or cross a river (r)? \n") 
  #  if action == "t":
   #     print("You climb a tree")
    # if action =="r":
     #   print("You found a boat!")
# elif place == "c":
  #  choice = input("Do you want to (l)ight a tourch? or (p)roceed in the dark? ")
  #  if choice == 'l':
   #     print("You found the exit, but are now faced with two paths. \n")
   # if choice == 'p':
    #    print("You are consumed by darkness.")
   # choice = input("Do you want to go (l)eft or (r)ight? \n")
   # if place == 'l': 
    #    pass
   # if place == 'r':
   #     pass
   # else: print("enter valid option")

#-----------------#
# second attempt

place = input("Choose a place: (f)orest or (c)ave? ")
if place == "f":
    action = input("climb a tree (t) or cross a river (r)? \n")
    if action == "t":
        print("You climb a tree")
    elif action =="r":
        print("You found a boat!")
    else: print("enter valid option")
elif place == "c":
    choice = input("Do you want to (l)ight a tourch? or (p)roceed in the dark? ")
    if choice == 'p':
        print("You are consumed by darkness. Try again!")
    elif choice == 'l':
        print("You found the exit, but are now faced with two paths. \n")
        choice = input("Do you want to go (l)eft or (r)ight? \n")
        if place == 'l':
            pass
        if place == 'r':
            pass
    else: print("enter valid option")
else: print("enter valid option")