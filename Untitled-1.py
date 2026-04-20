#global variables, lists and dictionaries -------
foods = [["Chips", 3.99, True], ["Salad", 4.49, True], ["Chicken", 5.99, False], ["Pie", 8.99, False], 
         ["Vegan pie", 8.49, True], ["Fruits", 4.99, True], ["Burger", 10.49, False], ["Fish", 6.49, False],
         ["Sausage roll", 8.99, False], ["Stir fry", 12.99, False],  ["Noodles", 4.49, False], ["Pizza", 10.99, False]]

# combo = ["Fish and chips", "Fruit salad", "Stir fry with chicken", "Pizza pie"]

#functions
def validify_int_input(prompt, invalid):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(invalid)

def menu(order):
    print("money")

def main():
    order = {}
    
    task = validify_int_input("What do you want to do? \n1. Order from menu | 2. View my order", "Invalid; please use numbers")
    if task == 1:
        menu(order)
    else:print("Invalid; please use the appropriate numbers")

