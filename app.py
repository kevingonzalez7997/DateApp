import time
# import time to pause code later on

print("Hello, Kevin Welcome to Matchmaker 3000\n")
time.sleep(3)

KevinsDate = input("Who is the lucky gal? \n")
time.sleep(3)

print("\nOoo, she sounds nice\n")
time.sleep(2)

# Here the budget will be stored in bucks
# Convert input to float because we are working with money

bucks = float(input("How much money are you bringing? \n"))  
MoneyLeft = bucks
time.sleep(3)
print("\nsounds good, let's start!\n")
time.sleep(3)

#####################################################################
# In this section I broke up the menu into different dictionaries to make it cleaner

Menu = {
    "Burger": 15.50,
    "Pizza": 14.25,
    "Sushi": 8.50,
    "Chicken Ceaser Salad": 12,
    "Steak": 28.50,
}

Drinks = {
    "Water bottle": 2,
    "Fountain drink": 2,
    "Signature Cocktail": 16,
    "Wine": 10,
    "Draft Beer": 12,
}

Apps = {

    "Mozzarella Sticks": 8.00,
    "Chicken Quesadilla": 9.50,
    "Side Salad": 4.00,
    "Soup of the day": 5.50
}

Desserts = {
    "Chocolate Cake": 8.00,
    "Apple Pie": 7.50,
    "Ice Cream Sundae": 5.75,
    "Cheesecake": 9.00,
    "Fruit Tart": 6.99,
}
####################################################################

# Here are all the functions
# One function for each menu category 

def FoodOrder():
    # MoneyLeft is made into a global scope b/c it will be called in other function
    global MoneyLeft 
    print('Now for our main dishes we have:\n')
    # Here a for loop is used to go through the dictionary
    # 'food' will be the item and 'price' will be the price
    # The' item()' function returns the key values in a list 
    for food, price in Menu.items():
        print(f"{food}: ${price}")

    MainDish = input("\nWhat would le donne like, perhaps a salad? \n")
    MainDishKG = input("And for you sir?")

    if MainDish in Menu:
        # Here [] are used to take the key value and assign it to the variable for later
        # The index comes from the item that the user inputs
        item_price = Menu[MainDish]
        item_priceKG = Menu[MainDishKG]
        MoneyLeft -= item_price
        MoneyLeft -= item_priceKG
        # Here MoneyLeft gets converted into a float because we are working with money
        # The item price gets subtracted from the budget 
        print(f"\nYou have ${MoneyLeft:.2f} left.\n")
    else:
        print("Sorry, that item is not on the menu.\n")

    # The functions for the other menu categories follow the same format

def DrinkOrder():
    global MoneyLeft  
    print('\nAnd to drink, we have:\n')
    for item, price in Drinks.items():
        print(f"{item}: ${price}")

    Drink = input("\nWhat would you like to drink? Might I suggest Pinot Grigio it is one of our best wines \n")
    DrinkKG = input("\nand for you sir? we have some great draft beers if you are instrested\n")
    if Drink in Drinks:
        drink_cost = Drinks[Drink]
        drink_costKG = Drinks[DrinkKG]
        MoneyLeft -= drink_cost
        MoneyLeft -= drink_costKG
        print(f"\nYou have ${MoneyLeft:.2f} left.\n")
    else:
        print("Sorry, that drink is not available.\n")


def AppsOrder():
    global MoneyLeft 
    print("\nWelcome to Tony's. Lets start with appetizers, we have:\n")
    for item, price in Apps.items():
        print(f"{item}: ${price}")

    app_choice = input("\nWhat can I bring for the tabel?\n")

    if app_choice in Apps:
        AppCost = Apps[app_choice]
        MoneyLeft -= AppCost
        print(f"\nYou have ${MoneyLeft:.2f} left.\n")
    else:
        print("Sorry, that appetizer is not available.\n")


def DesOrder():
    global MoneyLeft
    print("\nLastly we have desserts. Nothing is going to be as sweet as you hahah ('laughs in waiters') but today we have\n")
    for item, price in Desserts.items():
        print(f"{item}: ${price}")

    DessChoice = input("\nWhat would you like sweetheart?\n")
    DessChoiceKG = input("and for you?")
    if DessChoice in Desserts:
        Desscost = Desserts[DessChoice]
        DesscostKG = Desserts[DessChoiceKG]
        MoneyLeft -= Desscost
        MoneyLeft -= DesscostKG
        print(f"\nYou have${MoneyLeft:.2f} left.\n")
    else:
        print("sorry, that dessert is not available\n")
#################################################################################################################

#All functions are called in the food order 

AppsOrder()
FoodOrder()
DrinkOrder()
DesOrder()

##################################################################################################################
# Analyze if you went over the budget 

if MoneyLeft >= 0:
    print("The date went well, and you can go on another one!\n")
else:
    print("Umm can I talk to you on the side bud\n")
    time.sleep(3)
    print("Hey man I didn't want to tell you this in front of your date\n")
    time.sleep(3)
    print(f"but your card only took a partial amount of ${bucks} \n")
    time.sleep(3)
    print("I think about 2hr of dishes should cover the rest\n")
    time.sleep(3)
    print("No second date for you")
