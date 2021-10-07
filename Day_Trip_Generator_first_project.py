import random

destinations = ['museum', 'beach', 'strip club', 'church', 'lake']
item = random.choice(destinations)

notSatisfied = True

while notSatisfied :
    print("Current destination: " + item)
    value = input("Do you like this destination we've chosen for you?: ")
    if value == "no":
        print("We will try again")
        item = random.choice(destinations)
    else:
        print("That's awesome")      
        notSatisfied = False


resturaunts = ['fast food', 'chinese', 'soul food', 'jamaican', 'mexican']
thingtoeat = random.choice(resturaunts)

foodKitchen = True

while foodKitchen:
    print("Current resturaunts: " + thingtoeat)
    value = input("Do you like this resturaunt we've chosen for you?: ")
    if value == "no":
        print("We will try again")
        thingtoeat = random.choice(resturaunts)
    else:
        print("That's awesome")      
        foodKitchen = False




mode_of_transportation = ['car', 'plane', 'train', 'boat', 'motorcycle']
waytogetthere = random.choice(mode_of_transportation)

way_to_travel = True

while way_to_travel:
    print("Current mode of transportation: " + waytogetthere)
    value = input("Do you like this mode of travel we've chosen for you?: ")
    if value == "no":
        print("We will try again")
        waytogetthere = random.choice(mode_of_transportation)
    else:
        print("That's awesome")      
        way_to_travel = False


entertainment = ['football game', 'play' , 'music concert', 'water center', 'mountain']
thingtodo = random.choice(entertainment)

stuff_to_do = True

while stuff_to_do:
    print("Current selection of entertainment: " + thingtodo)
    value = input("Do you like this selection of entertainment we've chosen for you?: ")
    if value == "no":
        print("We will try again")
        thingtodo = random.choice(entertainment)
    else:
        print("That's awesome")      
        stuff_to_do = False




daytrip_complete = True

while daytrip_complete:
    value = input("Are you satisfied with your daytrip we helped you plan?: ")
    if value == "no":
        print("You can always try again until you get a daytrip you do like. ")
    else:
        print("That's incredible and may you enjoy your day trip! ")
        daytrip_complete = False







