# showing my work !!! study notes!



cat = 60


dog = str(cat)
print(dog)
print(type(dog))

# print(cat > 100) # You cant't do this
# print(dog > 100) # 'str' and 'int'

#---------------------------------------------#


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
        print("You are consumed by darkness.")
    elif choice == 'l':
        print("You found the exit, but are now faced with two paths. \n")
        choice = input("Do you want to go (l)eft or (r)ight? \n")
        if place == 'l':
            pass
        if place == 'r':
            pass
    else: print("enter valid option")
else: print("enter valid option")