#global variables, lists and dictionaries -------
loop = False
foods = {"chips": [3.99, 1], "salad": [4.49, 1], "chicken": [5.99, 2], "pie": [8.99, 2], 
         "vegan pie": [8.49, 1], "fruits": [4.99, 1], "burger": [10.49, 2], "fish": [6.49, 2],
         "sausage roll": [8.99, 2], "stir fry veggies": [12.99, 1],  "noodles": [4.49, 2], "pizza": [10.99, 2],
         "bacon bits": [7.99, 2], "garlic bread": [3.49, 1]}

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
    for food, details in foods.items():
        if newline == 5:
            print(f"{food} -- ${details[0]}")
            newline = 0
        else:
            print(f"{food} -- ${details[0]}", end=" | ")#fix this later
            newline += 1

def get_cost(food):
    """Gets the price of selected food"""
    if food in foods:
        return foods[food][0]

def vegan_option(food):
    """Checks if the food has a vegan option/is vegan"""
    if foods[food][1] == True:
        return food

def menu(cart):
    """Single menu"""
    """Shows foods and lets user order."""
    
    print("Here is the list of items that you can order. ")
    list_print()
    """prints all available food types"""
    
    loop = True
    exit = ["x", "end", "cancel", "finish", "done"]
    while loop == True:
        choice = input(f"Please order them indivisually. Enter x, end, cancel, finish or done to cancel. ").lower()
        if choice in foods:
            cart.append(choice)
            print(f"Ordered {choice} successfully!")
        elif choice in exit:
            loop = False
        else:
            print("Invalid; that choice is not available or is not a valid input")

def view(cart):
    newline = 0
    for item in cart:
        if newline == 8:
            print(item)
            newline = 0
        else:
            print(item, end=", ")#fix this later
            newline += 1

def payment(cart):
    """Payment"""
    total_Cost = 0
    for items in cart:
        print(f"Cost for {items} is {get_cost(items)}")
        total_Cost += get_cost(items)
    print(f"Total cost is {total_Cost}")

def main():
    cart = []
    
    while True:
        task = validify_int_input("What do you want to do? \n1. Browse menu | 2. View my order | 3. Proceed to payment", "Invalid; please use numbers")
        if task == 1:
            menu(cart)
        elif task == 2:
            view(cart)
        elif task == 3:
            payment(cart)
        else:print("Invalid; please use the appropriate numbers")
        print(cart)

main()