"""This program is a food ordering program."""
# global variables, lists and dictionaries -------
FOODS = {"chips": [3.99, 1], "salad": [4.49, 1], "chicken": [5.99, 1], "pie": [8.99, 2],
         "vegan pie": [8.49, 2], "fruits": [4.99, 1], "burger": [10.49, 2], "fish": [6.49, 1],
         "sausage roll": [8.99, 1], "stir fry veggies": [12.99, 3],  "noodles": [4.49, 1], "pizza": [10.99, 2],
         "bacon bits": [7.99, 1], "garlic bread": [3.49, 1]}

EXIT = ["x", "end", "cancel", "finish", "done"]


# functions
def validify_int_input(prompt, invalid):
    """Validifies intergers."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(invalid)


def get_cost(food):
    """Get the cost of selected food."""
    if food in FOODS:
        return FOODS[food][0]


def get_order_scale(cart):
    """Get the discount weight of the item."""
    scale = 0
    for item in cart:
        if item in FOODS:
            scale += FOODS[item][1]
    return scale


def menu(cart):
    """Show foods and lets user order."""
    new_line = 0  # used for counting number of prints before a new line is created
    print("Here is the list of items that you can order. ")
    for food, details in FOODS.items():
        if new_line == 5:
            print(f"{food} -- ${details[0]}")
            new_line = 0
        else:
            print(f"{food} -- ${details[0]}", end=" | ")
            new_line += 1
    print("")  # stops the next print from merging with the previous print statement

    loop = True
    while loop is True:
        choice = input("Please order them indivisually. Enter x, end, cancel, finish or done to cancel. \n").lower()
        if choice in FOODS:
            cart.append(choice)
            print(f"Ordered {choice} successfully!")
        elif choice in EXIT:
            loop = False
        else:
            print("Invalid; that choice is not available or is not a valid input")


def view(cart):
    """View and remove items from cart."""
    new_line = 0  # same as line 37
    for item in cart:
        if new_line == 8:
            print(item)
            new_line = 0
        else:
            print(item, end=", ")
            new_line += 1
    print("")  # same as line 46

    loop = True
    while loop is True:
        item = input("If you want to remove an item, then enter the name of the item. Otherwise enter x, end, cancel, finish or done. \n").lower()
        if item in cart:
            cart.remove(item)
        elif item in EXIT:
            loop = False
        else:
            print("Invalid; the item is not in your cart or your input is invalid.")


def payment(cart):
    """Payment."""
    total_cost = 0
    for items in cart:
        total_cost += get_cost(items)
        total_cost = round(total_cost, 2)
    discount_rate = get_order_scale(cart)
    if discount_rate > 14:
        total_cost = round(total_cost * 0.8, 2)
    elif discount_rate > 6:
        total_cost = round(total_cost * 0.9, 2)

    print(f"{len(cart)} items are in the cart and the total cost is {total_cost} with discounts applied.")
    print("You can get a 10% discount for having an order size greater than 6, and a 20% discount for an order size greater than 14.")
    payment_process = input("Do you want to pay and finish or return? \ny/n \n").lower()
    if payment_process == 'y':
        print("Paid successfully!")
        return False
    elif payment_process == 'n':
        print("Returning...")
        return True
    else:
        print("Invalid; please put y for yes or n for no. Returning...")
        return True


def main():
    """Call other functions."""
    cart = []
    shopping = True
    while shopping is True:
        task = validify_int_input("What do you want to do? \n1. Browse menu | 2. View my order | 3. Proceed to payment \n", "Invalid; please use numbers")
        if task == 1:
            menu(cart)
        elif task == 2:
            view(cart)
        elif task == 3:
            shopping = payment(cart)
        else:
            print("Invalid; please use the appropriate numbers")


main()
