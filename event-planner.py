# Event planner code correction 

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)


#-------------------------------#
# frist attempt



# attendees = input("Enter number of attendees: ")
# venue = ("large hall") if ('attendees' > 100) else ("conference room")
# attendees = int(input("Enter number of attendees: "))
# attendees >= 100
# print(attendees)
# print(type(attendees))
#--------------------------------#
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".



attendees = int(input("Enter number of attendees: "))
venue = ("large hall") if (attendees > 100) else ("conference room")
print(venue)
print(type(attendees))
food = input("Are you a vegetarian? (y) or (n) \n")
if food == 'y':
    print("We Recommended Veggie Delight Caterers!")
elif food == 'n':
    print("We Recommended Gourmet Meals Caterers!")
else:
    print("Enter a valid option.")

