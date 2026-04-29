#global variables, lists and dictionaries -------
loop = False
foods = {"chips": [3.99, True], "salad": [4.49, True], "chicken": [5.99, False], "pie": [8.99, False], 
         "vegan pie": [8.49, True], "fruits": [4.99, True], "burger": [10.49, False], "fish": [6.49, False],
         "sausage roll": [8.99, False], "stir fry veggies": [12.99, True],  "noodles": [4.49, False], "pizza": [10.99, False],
         "bacon bits": [7.99, False], "garlic bread": [3.49, True]}

# combo ideas: Chips + chicken, chips + fish, salad + fruits, pie + sausage roll, vegan pie + stir fry veggies, fruits + fish, stir fry veggies + noodles, stir fry veggies + bacon bits, burger + burger

#functions
def validify_int_input(prompt, invalid):
    """Validifies intergers"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(invalid)

def list_print():
    newline = 0
    for food in foods.keys():
        if newline == 5:
            print(food)
            newline = 0
        
        else:
            print(food, end=", ")#fix this later
            newline += 1


def get_cost(food):
    """Gets the price of selected food"""
    if food in foods:
        return foods[food][0]


def vegan_option(food):
    """Checks if the food has a vegan option/is vegan"""
    if foods[food][1] == True:
        return "Vegan"
    else:
        return "No" 

def menu(cart):
    """Shows foods and lets user order."""
    print("Here is the list of items that you can order. ")
    loop = True
    list_print()
    """prints all available food types"""
    
    while loop == True:
        choice = input("Please order them indivisually. Enter X or cancel to cancel, and P or pay to pay for your meal.").lower()
        if get_cost(choice):
            print(choice)
        elif choice == "x" or choice == "cancel":
            loop = False
        else:
            print("Invalid; that choice is not available or is not a valid input")
"""Single menu"""

def view(cart):
    print('temp')

def payment(cart):
    """Payment"""
    total_Cost = 0
    for items in cart:
        print(f"Total cost for {items} is {get_cost(items)}")
        total_Cost += get_cost(items)

def main():
    cart = []
    
    task = validify_int_input("What do you want to do? \n1. Browse menu | 2. View my order | 3. Proceed to payment", "Invalid; please use numbers")
    if task == 1:
        menu(cart)
    elif task == 2:
        view(cart)
    elif task == 3:
        payment(cart)
    else:print("Invalid; please use the appropriate numbers")

main()