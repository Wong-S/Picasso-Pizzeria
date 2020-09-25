#MODULES USED:
import time
import turtle

# ==================================================================
#GLOBAL VARIABLES / LIST VARIABLES


topping_list_1 = []   #Stores the number related to the toppings
topping_list_2 = []    #Stores the name related to the toppings
size_pizza_list = []  #Stores the pizza size player chooses

TX_TAX = 0.0825     #Sales tax used in Texas

# ==================================================================
#GENERAL FUNCTIONS:

def continue_key():
    '''Function prompts user to continue via 'enter' key'''
    enter = input("Press the 'ENTER' key to continue\n> ")

def pause():
    '''Function makes a short pause between outputted text'''
    timer = 4
    while timer > 0:
        time.sleep(0.5)
        timer -= 1

def pause_long():
    '''Function makes a longer pause between outputted text'''
    timer = 6
    while timer > 0:
        time.sleep(0.5)
        timer -= 1

# ==================================================================
# PIZZA GAME STARTS: Pizza Functions

def game_start():
    '''Function asks user to start game'''
    while True:
        start_game = input("Are you ready?\n> ")
        if start_game.startswith("y") or start_game.startswith("Y") or start_game.startswith("s") or start_game.startswith("S") or start_game.startswith("o") or start_game.startswith("O"):

            # Loading game:
            timer = 5
            dot = ""
            print("\nLoading", end="")
            while timer > 0:
                dot += "." * 10
                print(dot)
                time.sleep(1)
                timer -= 1
            break

        else:
            print('"Your stomach lets out an annoyed grumble..."\n')

def player_name():
    '''Function has player's name stored/called throughout program'''

    player_name = input("> ")
    player_name = player_name.title()
    return player_name

def pizza_size_choice():
    '''Function prompts user to select 4 pizza sizes and appends to an empty list for later use'''
    while True:
        try:
            pizza_size = input("Size Selection: ")
            size = pizza_size

            if size.startswith("S") or size.startswith("s"):
                pause() #Function call
                print("Good choice!")
                size_pizza_list.append("Small Pizza")
                break

            elif size.startswith("M") or size.startswith("m"):
                pause() #Function call
                print("Superb choice!")
                size_pizza_list.append("Medium Pizza")
                break

            elif size.startswith("L") or size.startswith("l"):
                pause() #Function call
                print("Excellent selection you have made!")
                size_pizza_list.append("Large Pizza")
                break

            elif (
                size.startswith("XL")
                or size.startswith("E")
                or size.startswith("e")
                or size.startswith("xl")
            ):
                pause() #Function call
                print("Colored me surprised!! Now THAT is a pizza!")
                size_pizza_list.append("Extra Large Pizza")
                break

            else:
                print("Please enter one of the four selections above.\n")

        except:
            continue

def printed_menu_toppings():
    '''Function prints a formatted menu for user to view all toppings name by number'''
    format_string = "{meat:<22} {veg:<23} {fruit:<20}"
    print("-" * 68)
    print(
        format_string.format(
            meat="MEATS ($1.75)", veg="VEGETABLES ($1.50)", fruit="FRUITS ($1.25)"
        )
    )
    print("-" * 68)

    print(
        format_string.format(
            meat="[1] Anchovies",
            veg="[6] Artichoke Hearts",
            fruit="[11] Canned Pineapple",
        )
    )

    print()
    print(
        format_string.format(
            meat="[2] Crumbled Bacon",
            veg="[7] Bloody Beets",
            fruit="[12] Ghost Peppers",
        )
    )
    print()

    print(
        format_string.format(
            meat="[3] Imitation Sausage",
            veg="[8] Green Onions",
            fruit="[13] Red Olives",
        )
    )
    print()

    print(
        format_string.format(
            meat="[4] Pepperoni",
            veg="[9] Spoiled Spinach",
            fruit="[14] Sour Yellow Corn",
        )
    )
    print()

    print(
        format_string.format(
            meat="[5] Spam", veg="[10] White Mushrooms", fruit="[15] Tiny Tomatoes"
        )
    )
    print("-" * 68)
    print()

def player_topping_choices():
    '''Function prompts user to how many toppings and adds topping choice's number to an empty list variable'''

    print("How many total toppings would you like?")

    while True:
        try:

            print("Enter a number")
            player_decision_total_toppings = int(input("> "))

            n = player_decision_total_toppings

            if (player_decision_total_toppings >= 1) and (
                player_decision_total_toppings <= 6
            ):
                for i in range(0, n):
                    topping_choices = int(
                        input("\nEnter the topping's corresponding number:\n> ")
                    )
                    if (topping_choices not in topping_list_1) and (topping_choices > 0):
                        topping_list_1.append(topping_choices)

                    elif topping_choices in topping_list_1:
                        print("You already added this topping!")
                        while True:
                            another_top = int(input("Choose a different topping!\n> "))
                            if (another_top != topping_choices) and (another_top > 0) and (another_top not in topping_list_1):
                                topping_list_1.append(another_top)
                                break

                            else:
                                continue

                break

            elif player_decision_total_toppings > 7:
                print("Too many toppings! Please choose at least 6 toppings.")
                continue

            elif player_decision_total_toppings <= 0:
                print("You need at least one topping to complete your order.")
                continue

        except:
            print("Please input a number.")
            continue

    return topping_list_1

def topping_dict():
    '''Function stores toppings into dictionary'''
    toppings_dict_2 = {
        1: "Anchovies",
        2: "Crumbled Bacon",
        3: "Imitation Sausage",
        4: "Pepperoni",
        5: "Spam",
        6: "Artichoke Hearts",
        7: "Bloody Beets",
        8: "Green Onions",
        9: "Spoiled Spinach",
        10: "White Mushrooms",
        11: "Canned Pineapple",
        12: "Ghost Peppers",
        13: "Red Olives",
        14: "Sour Yellow Corn",
        15: "Tiny Tomatoes",
    }
    return toppings_dict_2

def topping_list_to_dict():
    '''Function coverts toppings previously stored in empty list to the actual name of the topping. Adds the name to a new empty list variable'''

    toppings_dict_2 = topping_dict()

    for i in topping_list_1:
        if i == 1:
            topping_list_2.append(toppings_dict_2[1])

        elif i == 2:
            topping_list_2.append(toppings_dict_2[2])

        elif i == 3:
            topping_list_2.append(toppings_dict_2[3])

        elif i == 4:
            topping_list_2.append(toppings_dict_2[4])

        elif i == 5:
            topping_list_2.append(toppings_dict_2[5])

        elif i == 6:
            topping_list_2.append(toppings_dict_2[6])

        elif i == 7:
            topping_list_2.append(toppings_dict_2[7])

        elif i == 8:
            topping_list_2.append(toppings_dict_2[8])

        elif i == 9:
            topping_list_2.append(toppings_dict_2[9])

        elif i == 10:
            topping_list_2.append(toppings_dict_2[10])

        elif i == 11:
            topping_list_2.append(toppings_dict_2[11])

        elif i == 12:
            topping_list_2.append(toppings_dict_2[12])

        elif i == 13:
            topping_list_2.append(toppings_dict_2[13])

        elif i == 14:
            topping_list_2.append(toppings_dict_2[14])

        elif i == 15:
            topping_list_2.append(toppings_dict_2[15])

def current_topping_list():
    '''Function iterates through list variable that stored the name of toppings only. Displays topping name back to user BEFORE any changes are made'''
    length = len(topping_list_2)
    print("Your selected toppings are:")
    #Function call:
    pause()
    print("-" * 20)
    for i in range(length):
        print(f"<> {topping_list_2[i]}")
    print("-" * 20)

def reSelection_toppings():
    '''Function asks player if they want to change or add any more toppings'''

    topping_dict()

    while True:
        try:

            print("Are you satisfied with your selected toppings?")
            player_answer = input("> ")
            #Function call:
            pause()

            if player_answer.startswith("Y") or player_answer.startswith("y"):
                print("Great! Time to checkout!")
                break

            elif player_answer.startswith("N") or player_answer.startswith("n"):
                print("Okay, would you like to (D)elete or (A)dd a topping?")

                player_updated_answer = input("> ")

                if player_updated_answer.startswith(
                    "D"
                ) or player_updated_answer.startswith("d"):

                    # Show player their current topping selections
                    print("Your current selected toppings are:\n")

                    #Function call:
                    pause()

                    toppings_dict_2 = topping_dict()

                    print("-" * 20)
                    for k, v in toppings_dict_2.items():
                        if k in topping_list_1:
                            print(f"[{k}] {v}")
                    print("-" * 20)

                    while True:
                        print("Which topping do you want to delete?\n")
                        try:
                            deleted_topping = int(
                                input("Enter the topping's number.\n> ")
                            )

                            print()
                            for topping in topping_list_1:
                                if topping == deleted_topping:
                                    topping_list_1.remove(topping)

                            print("-" * 20)
                            for k, v in toppings_dict_2.items():
                                if k in topping_list_1:
                                    print(f"[{k}] {v}")
                            print("-" * 20)

                            break

                        except:
                            continue

                if player_updated_answer.startswith(
                    "A"
                ) or player_updated_answer.startswith("a"):

                    #Function call:
                    pause()

                    print(
                        "You currently have", len(
                            topping_list_1), "out of 6 toppings."
                    )

                    while True:
                        try:
                            print("How many more toppings do you want to add? ")
                            new_topping_input = int(input("> "))
                            num = new_topping_input

                            if new_topping_input <= (6 - len(topping_list_1)):


                                print("")

                                for i in range(0, num):
                                    updated_topping_choices = int(
                                        input(
                                            "Enter topping's corresponding number:\n> "
                                        )
                                    )
                                    if updated_topping_choices not in topping_list_1:
                                        topping_list_1.append(updated_topping_choices)

                                    elif updated_topping_choices in topping_list_1:
                                        print("You already have this topping!")
                                        while True:
                                            another_top = int(input("Choose a different topping!\n> "))
                                            if (another_top != updated_topping_choices) and (another_top > 0) and (another_top not in topping_list_1):
                                                topping_list_1.append(another_top)
                                                break

                                            else:
                                                continue

                                break

                        except:
                            print("Sorry! Can only have a total of 6 toppings.")
                            print(
                                "You currently have",
                                len(topping_list_1),
                                "out of 6 toppings.",
                            )
                            continue
            else:
                print("Please answer 'Yes' or 'No'.")
        except:
            continue

def final_selected_toppings():
    '''Function iterates through list variable that stored the name of toppings only. Displays topping name back to user AFTER changes are made'''

    toppings_dict_2 = topping_dict()
    print("Your new selected toppings are:")
    pause() #Function call:
    print("-" * 20)
    for k, v in toppings_dict_2.items():
        if k in topping_list_1:
            print(f"[{k}] {v}")
    print("-" * 20)

# ==================================================================
#PAYING FOR PIZZA STARTS: Functions Related to Cost

def cost_dict():
    '''Function returns dictionary that includes pizza size prices and nested dictionary topping prices'''
    cost_dict = {
        "Small Pizza": 5.00, "Medium Pizza": 7.00, "Large Pizza": 11.00, "Extra Large Pizza": 15.00, 1: {"meat": "Anchovies", "cost": 1.75}, 2:{"meat": "Crumbled Bacon","cost" : 1.75}, 3: {"meat": "Imitation Sausage","cost": 1.75}, 4: {"meat": "Pepperoni", "cost": 1.75}, 5: {"meat": "Spam", "cost": 1.75}, 6: {"veg":"Artichoke Hearts" ,"cost": 1.50}, 7: {"veg":"Bloody Beets" ,"cost":1.50}, 8: {"veg":"Green Onions" ,"cost": 1.50}, 9: {"veg": "Spoiled Spinach" ,"cost": 1.50}, 10: {"veg": "White Mushrooms" ,"cost": 1.50}, 11: {"fruit": "Canned Pineapple" ,"cost": 1.25}, 12:{"fruit": "Ghost Peppers" ,"cost": 1.25}, 13: {"fruit": "Red Olives" ,"cost": 1.25}, 14: {"fruit": "Sour Yellow Corn" ,"cost": 1.25}, 15:{"fruit": "Tiny Tomatoes" ,"cost": 1.25},
        }

    return cost_dict

def processing_order():
    '''Function used to display the text, 'Processing Order', via use of time module'''
    timer = 4
    dot = "."
    print("\nProcessing Order", end="")
    while timer > 0:
        dot += ".." * 10
        print(dot)
        time.sleep(1)
        timer -= 1

def display_printed_cost():
    '''Function outputs a formatted display with the title, 'Final Pizza Costs' '''
    format_string = "{items:<15}"
    print("-" * 30)
    print(format_string.format(items="FINAL PIZZA COSTS"))
    print("-" * 30)

def final_item_cost_display():
    '''Function iterates through the cost_dict() function and compares values in dictionary to what user selected as their original pizza size, which was stored in a list'''
    cost = cost_dict()
    for k, v  in cost.items():
        if k in size_pizza_list:
           print(f"{k}: ${v:.2f}")

def final_item_cost():
    '''Function iterates through list that held topping number, and then compares to the cost_dict() function to see if values are in that list. Outputs the topping name and cost to user'''
    cost = cost_dict()

    for i in topping_list_1:
        if i == 1:
            print(f"{cost[1]['meat']}: ${cost[1]['cost']}")

        elif i == 2:
            print(f"{cost[2]['meat']}: ${cost[2]['cost']}")

        elif i == 3:
            print(f"{cost[3]['meat']}: ${cost[3]['cost']}")

        elif i == 4:
            print(f"{cost[4]['meat']}: ${cost[4]['cost']}")

        elif i == 5:
            print(f"{cost[5]['meat']}: ${cost[5]['cost']}")

        elif i == 6:
            print(f"{cost[6]['veg']}: ${cost[6]['cost']:.2f}")

        elif i == 7:
            print(f"{cost[7]['veg']}: ${cost[7]['cost']:.2f}")

        elif i == 8:
            print(f"{cost[8]['veg']}: ${cost[8]['cost']:.2f}")

        elif i == 9:
            print(f"{cost[9]['veg']}: ${cost[9]['cost']:.2f}")

        elif i == 10:
            print(f"{cost[10]['veg']}: ${cost[10]['cost']:.2f}")

        elif i == 11:
            print(f"{cost[11]['fruit']}: ${cost[11]['cost']}")

        elif i == 12:
            print(f"{cost[12]['fruit']}: ${cost[12]['cost']}")

        elif i == 13:
            print(f"{cost[13]['fruit']}: ${cost[13]['cost']}")

        elif i == 14:
            print(f"{cost[14]['fruit']}: ${cost[14]['cost']}")

        elif i == 15:
            print(f"{cost[15]['fruit']}: ${cost[15]['cost']}")

    return topping_list_1

def new_list_pizza_size_cost():
    '''Function makes a new list with only the cost value of pizza sizes from the key dictionary'''
    cost = cost_dict()

    for k in cost.keys():
        if "Small Pizza" in size_pizza_list:
            list_with_pizza_size_cost = [(cost["Small Pizza"])]

            return list_with_pizza_size_cost

        if "Medium Pizza" in size_pizza_list:
            list_with_pizza_size_cost = [(cost["Medium Pizza"])]

            return list_with_pizza_size_cost

        if "Large Pizza" in size_pizza_list:
            list_with_pizza_size_cost = [(cost["Large Pizza"])]

            return list_with_pizza_size_cost

        if "Extra Large Pizza" in size_pizza_list:
            list_with_pizza_size_cost = [(cost["Extra Large Pizza"])]

            return list_with_pizza_size_cost

def new_list_cost():
    '''Function makes a new list with only the cost value from the key dictionary'''
    cost = cost_dict()
    list_with_costs = []

    for k in cost:
        if k in topping_list_1:
            if k == 1:
                list_with_costs.append(cost[1]["cost"])

            elif k == 2:
                list_with_costs.append(cost[2]["cost"])

            elif k == 3:
                list_with_costs.append(cost[3]["cost"])

            elif k == 4:
                list_with_costs.append(cost[4]["cost"])

            elif k == 5:
                list_with_costs.append(cost[5]["cost"])

            elif k == 6:
                list_with_costs.append(cost[6]["cost"])

            elif k == 7:
                list_with_costs.append(cost[7]["cost"])

            elif k == 8:
                list_with_costs.append(cost[8]["cost"])

            elif k == 9:
                list_with_costs.append(cost[9]["cost"])

            elif k == 10:
                list_with_costs.append(cost[10]["cost"])

            elif k == 11:
                list_with_costs.append(cost[11]["cost"])

            elif k == 12:
                list_with_costs.append(cost[12]["cost"])

            elif k == 13:
                list_with_costs.append(cost[13]["cost"])

            elif k == 14:
                list_with_costs.append(cost[14]["cost"])

            elif k == 15:
                list_with_costs.append(cost[15]["cost"])

            elif k == 16:
                list_with_costs.append(cost[16]["cost"])

            elif k == 17:
                list_with_costs.append(cost[17]["cost"])

            elif k == 18:
                list_with_costs.append(cost[18]["cost"])
    return list_with_costs

def pre_recipt_cost():
    '''Function adds the total cost of toppings and pizza size BEFORE tip and tax to a list'''
    updated_pizza_size_cost = new_list_pizza_size_cost()
    final_topping_cost = new_list_cost()

    recipt_list_combined = updated_pizza_size_cost + final_topping_cost

    return recipt_list_combined

def get_total():
    '''Function iterates through pre_recipt_cost() function and returns the total cost BEFORE tip and tax are added'''
    values = pre_recipt_cost()
    total = 0
    for num in values:
        total += num

    return total

def player_tip():
    '''Function gets input tip from player. Else, returns 0 tip'''

    tip = float(input())
    if tip >= 0:
        return tip
    else:
        tip = 0
        return tip

def calculate_total_bill(bill, tip):
    '''Function calculates total pizza, tip, and service fee'''

    calculated_tip = bill + tip
    bill_with_tax = bill * TX_TAX
    total_bill = calculated_tip + bill_with_tax

    return total_bill

# ==================================================================
# TURTLE GRAPHICS START: Pizza Drawing and Topping Drawing Functions

def pizza_preview():
    '''Function prompts user to enable pizza drawing preview'''
    while True:
        pizza_preview_response = input("> ")
        if pizza_preview_response.startswith("y") or pizza_preview_response.startswith("Y") or pizza_preview_response.startswith("s") or pizza_preview_response.startswith("S") or pizza_preview_response.startswith("o") or pizza_preview_response.startswith("O"):
            timer = 3
            print("Pre-cooking preview in....")
            while timer > 0:
                print(f"........{timer}")
                time.sleep(2)
                timer -= 1
            break

        else:
            print('"The anticipation is killing you..."\n')
            continue

def pizza_outline():
    '''Function outputs the pizza circle shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pensize = 2)
    t.pen(pencolor="brown", fillcolor="orange", pensize=10, speed=9)
    t.begin_fill()
    t.penup()
    t.home()
    t.pendown()
    t.circle(100)
    t.end_fill()
    t.penup()

def cutting_pizza():
    '''Function outputs the pizza cutting lines that divide the pizza_outline() function'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pensize=3)
    t.color("brown")
    t.penup()
    t.home()
    t.pendown

    t.left(90)
    t.fd(200)
    t.penup()
    t.goto(0, 100)
    t.right(90)
    t.pendown()
    t.fd(100)
    t.bk(200)

    t.penup()
    t.goto(0, 100)
    t.right(135)
    t.pendown()
    t.fd(100)
    t.bk(200)

    t.penup()
    t.goto(0, 100)
    t.left(275)
    t.pendown()
    t.fd(100)
    t.bk(200)

    t.penup()
    t.home()
    t.left(90)
    t.pendown()
    t.fd(200)
    t.penup()

def anch_bowtie():
    '''Function outputs topping #1 Anchovies as bowtie shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("blue")
    t.penup()

    t.home()
    t.goto(3, 25)

    t.pendown()
    t.fd(50)
    t.right(120)
    t.fd(20)
    t.right(120)
    t.fd(50)
    t.left(120)
    t.fd(30)

    t.penup()
    t.home()
    t.goto(25, 170)


    t.pendown()
    t.fd(40)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(40)
    t.left(120)
    t.fd(30)

    t.penup()

    t.home()
    t.goto(-50, 150)

    t.pendown()
    t.fd(50)
    t.right(120)
    t.fd(20)
    t.right(120)
    t.fd(50)
    t.left(120)
    t.fd(30)

    t.penup()
    t.home()
    t.goto(-50, 50)


    t.pendown()
    t.fd(40)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(40)
    t.left(120)
    t.fd(30)

def bacon_star():
    '''Function outputs topping #2 Crumbled Bacon as star shape'''

    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pencolor="yellow", fillcolor="yellow")
    t.begin_fill
    t.penup()
    t.home()
    t.goto(-50, 100)
    t.pendown()
    for i in range(10):
        t.forward(50)
        t.right(144)

    t.end_fill()

    t.penup()
    t.home()
    t.goto(-25, 170)
    t.pendown()
    for i in range(10):
        t.forward(50)
        t.right(144)

    t.penup()
    t.home()
    t.goto(50, 150)
    t.pendown()

    for i in range(10):
        t.forward(50)
        t.right(144)

def sausage_rec():
    '''Function outputs topping #3 Imitation Sausage as rectangle shape'''

    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("yellow")

    t.penup()
    t.home()
    t.goto(15, 50)
    t.pendown()
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)

    t.penup()
    t.home()
    t.goto(80, 90)
    t.pendown()
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.left(90)

    t.penup()
    t.home()
    t.goto(25, 160)
    t.pendown()
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)

    t.penup()
    t.home()
    t.goto(-80, 97)
    t.pendown()
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(25)
    t.left(90)

    t.penup()
    t.home()
    t.goto(-40, 24)
    t.pendown()
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)
    t.forward(7)
    t.left(90)
    t.forward(27)
    t.left(90)

def pepperoni_circle():
    '''Function outputs topping #4 Pepperoni as circle shape'''

    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("red")

    t.penup()
    t.home()
    t.goto(50, 30)
    t.pendown()
    t.circle(10)

    t.penup()
    t.home()
    t.goto(50, 100)
    t.pendown()
    t.circle(15)

    t.penup()
    t.home()
    t.goto(25, 170)
    t.pendown()
    t.circle(10)

    t.penup()
    t.home()
    t.goto(-50, 150)
    t.pendown()
    t.circle(15)

    t.penup()
    t.home()
    t.goto(-20, 90)
    t.pendown()
    t.circle(10)

    t.penup()
    t.home()
    t.goto(-20, 10)
    t.pendown()
    t.circle(15)

def spam_square():
    '''Function outputs topping #5 Spam as square shape'''

    t = turtle.Turtle()
    t.pen(speed = 10)
    t.fillcolor("purple")

    t.penup()
    t.home()
    t.goto(10, 50)
    t.pendown()
    t.begin_fill()
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(50, 70)
    t.pendown()
    t.begin_fill()
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(50, 120)
    t.pendown()
    t.begin_fill()
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-10, 125)
    t.pendown()
    t.begin_fill()
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-40, 80)
    t.pendown()
    t.begin_fill()
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.end_fill()

def artichoke_ellipse():
    '''Function outputs topping #6 Artichoke as ellipse shape'''

    t = turtle.Turtle()
    t.pen(speed = 10)
    t.fillcolor("blue")

    t.penup()
    t.home()
    t.goto(50, 50)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.forward(10)
    t.circle(20)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(25, 170)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.forward(5)
    t.circle(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-30, 155)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.forward(10)
    t.circle(20)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-70, 50)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.forward(5)
    t.circle(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-20, 20)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.forward(10)
    t.circle(20)
    t.end_fill()

def beets_turt():
    '''Function outputs topping #7 Beets as turtle shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("red")

    t.penup()
    t.home()
    t.goto(15, 70)
    t.pendown()
    t.shape("turtle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(80, 100)
    t.pendown()
    t.shape("turtle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(-15, 110)
    t.pendown()
    t.shape("turtle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(-75, 90)
    t.pendown()
    t.shape("turtle")
    t.stamp()

def onions_oval():
    '''Function outputs topping #8 Green Onions as oval shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pencolor="green", fillcolor="green")
    t.begin_fill

    t.penup()
    t.home()
    t.goto(50, 50)
    t.pendown()
    for _ in range(6):
        t.forward(20)
        t.right(-60)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-15, 115)
    t.pendown()
    for _ in range(6):
        t.forward(20)
        t.right(-60)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-50, 45)
    t.pendown()
    for _ in range(6):
        t.forward(20)
        t.right(-60)
    t.end_fill()

def spinach_line():
    '''Function outputs topping #9 Spinach as zig line shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("green")

    t.penup()
    t.home()
    t.goto(10, 60)
    t.pendown()
    t.fd(25)
    t.right(120)
    t.fd(25)
    t.left(120)
    t.fd(25)

    t.penup()
    t.home()
    t.goto(10, 150)
    t.pendown()
    t.fd(25)
    t.right(120)
    t.fd(25)
    t.left(120)
    t.fd(25)

    t.penup()
    t.home()
    t.goto(-50, 60)
    t.pendown()
    t.fd(25)
    t.right(120)
    t.fd(25)
    t.left(120)
    t.fd(25)

    t.penup()
    t.home()
    t.goto(-50, 150)
    t.pendown()
    t.fd(25)
    t.right(120)
    t.fd(25)
    t.left(120)
    t.fd(25)

def mushroom_circles():
    '''Function outputs topping #10 Artichoke as two concentric circle shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("blue")

    t.penup()
    t.home()
    t.goto(10, 30)
    t.pendown()
    t.circle(10)
    t.circle(5)

    t.penup()
    t.home()
    t.goto(40, 50)
    t.pendown()
    t.circle(17)
    t.circle(10)

    t.penup()
    t.home()
    t.goto(45, 90)
    t.pendown()
    t.circle(10)
    t.circle(5)

    t.penup()
    t.home()
    t.goto(50, 130)
    t.pendown()
    t.circle(10)
    t.circle(5)

    t.penup()
    t.home()
    t.goto(15, 177)
    t.pendown()
    t.circle(10)
    t.circle(5)

    t.penup()
    t.home()
    t.goto(-20, 163)
    t.pendown()
    t.circle(17)
    t.circle(10)

    t.penup()
    t.home()
    t.goto(-50, 140)
    t.pendown()
    t.circle(10)
    t.circle(5)

    t.penup()
    t.home()
    t.goto(-45, 70)
    t.pendown()
    t.circle(17)
    t.circle(10)

    t.penup()
    t.home()
    t.goto(-24, 50)
    t.pendown()
    t.circle(10)
    t.circle(5)

def pineapple_tri():
    '''Function outputs topping #11 Pineapple as triangle shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("yellow")

    t.penup()
    t.home()
    t.goto(20, 30)
    t.pendown()
    t.fd(30)
    t.lt(120)
    t.fd(30)
    t.lt(120)
    t.fd(30)

    t.penup()
    t.home()
    t.goto(50, 70)
    t.pendown()
    t.fd(20)
    t.lt(120)
    t.fd(20)
    t.lt(120)
    t.fd(20)

    t.penup()
    t.home()
    t.goto(50, 150)
    t.pendown()
    t.fd(30)
    t.lt(120)
    t.fd(30)
    t.lt(120)
    t.fd(30)

    t.penup()
    t.home()
    t.goto(-30, 160)
    t.pendown()
    t.fd(20)
    t.lt(120)
    t.fd(20)
    t.lt(120)
    t.fd(20)

    t.penup()
    t.home()
    t.goto(-70, 100)
    t.pendown()
    t.fd(20)
    t.lt(120)
    t.fd(20)
    t.lt(120)
    t.fd(20)

    t.penup()
    t.home()
    t.goto(-40, 50)
    t.pendown()
    t.fd(25)
    t.lt(120)
    t.fd(25)
    t.lt(120)
    t.fd(25)

    t.penup()
    t.home()
    t.goto(-20, 20)
    t.pendown()
    t.fd(15)
    t.lt(120)
    t.fd(15)
    t.lt(120)
    t.fd(15)

def peppers_chi():
    '''Function outputs topping #12 Ghost Peppers as X-shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.color("purple")

    t.penup()
    t.home()
    t.goto(30, 50)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(25)
    t.right(120)
    t.pendown()
    t.fd(25)
    t.bk(50)

    t.penup()
    t.home()
    t.goto(20, 160)
    t.pendown()
    t.fd(25)
    t.penup()
    t.bk(15)
    t.right(120)
    t.pendown()
    t.fd(15)
    t.bk(25)

    t.penup()
    t.home()
    t.goto(-40, 170)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(25)
    t.right(120)
    t.pendown()
    t.fd(25)
    t.bk(50)

    t.penup()
    t.home()
    t.goto(-40, 85)
    t.pendown()
    t.fd(25)
    t.penup()
    t.bk(15)
    t.right(120)
    t.pendown()
    t.fd(15)
    t.bk(25)

def olives_triangle():
    '''Function outputs topping #13 Olives as triangle stamp shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.penup()
    t.home()
    t.goto(60, 50)
    t.pendown()
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(40, 100)
    t.pendown()
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(55, 150)
    t.pendown()
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(25, 175)
    t.pendown()
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(-25, 165)
    t.pendown()
    t.shape("triangle")
    t.stamp()

    t.penup()
    t.home()
    t.goto(-50, 50)
    t.pendown()
    t.shape("triangle")
    t.stamp()

def corn_arrow():
    '''Function outputs topping #14 Corn as arrow shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pencolor="yellow", fillcolor="yellow")
    t.begin_fill

    t.penup()
    t.home()
    t.goto(50, 100)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

    t.penup()
    t.home()
    t.goto(20, 150)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-50, 150)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

    t.penup()
    t.home()
    t.goto(50, 50)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-30, 100)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-10, 50)
    t.pendown()
    t.shape("classic")
    t.stamp()
    t.end_fill()

def tomat_dot():
    '''Function outputs topping #15 Tomatoe as small dot shape'''
    t = turtle.Turtle()
    t.pen(speed = 10)
    t.pen(pencolor="red", fillcolor="red")
    t.begin_fill

    t.penup()
    t.home()
    t.goto(25, 50)
    t.pendown()
    t.dot(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(25, 50)
    t.pendown()
    t.dot(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(25, 100)
    t.pendown()
    t.dot(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(25, 165)
    t.pendown()
    t.dot(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-55, 145)
    t.pendown()
    t.dot(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-20, 50)
    t.pendown()
    t.dot(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-45, 80)
    t.pendown()
    t.dot(10)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(-10, 130)
    t.pendown()
    t.dot(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(75, 75)
    t.pendown()
    t.dot(15)
    t.end_fill()

    t.penup()
    t.home()
    t.goto(70, 145)
    t.pendown()
    t.dot(15)
    t.end_fill()

def pizza_turtle_drawing():
    '''Function iterates through topping list that stored the number related to that topping. Outputs the topping for display'''
    t = turtle.Turtle()
    t.pen(pensize = 2)
    for k in topping_list_1:
        if k == 1:
            anch_bowtie()

        if k == 2:
            bacon_star()

        if k == 3:
            sausage_rec()

        if k == 4:
            pepperoni_circle()

        if k == 5:
            spam_square()

        if k == 6:
            artichoke_ellipse()

        if k == 7:
            beets_turt()

        if k == 8:
            onions_oval()

        if k == 9:
            spinach_line()

        if k == 10:
            mushroom_circles()

        if k == 11:
            pineapple_tri()

        if k == 12:
            peppers_chi()

        elif k == 13:
            olives_triangle()

        elif k == 14:
            corn_arrow()

        elif k == 15:
            tomat_dot()

def closing_game():
    '''Function displays 'Exiting Picasso's Pizzeria' via using time module'''
    print()
    timer = 5
    dot = ""
    print("\nExiting Picasso's Pizzeria", end="")
    while timer > 0:
        dot += ".." * 15
        print(dot)
        time.sleep(1)
        timer -= 1

# ==================================================================
#PICASSO'S DRAWING:

def picasso_drawing():
    '''Function displays Picasso's drawing piece to player'''
    a = "*************************************************************************************************************"
    b = "******         **********************************************************************************************"
    c = "*****    ***    *********************************************************************************************"
    d = "*****   *    *   ***    *************************************************************************************"
    e = "*****    ***    ****    ************************** **********************************************************"
    f = "*****          *********************************     ***********         ***         *****          *********"
    g = "*****     *******************         *******   **     *********     *******    ********       *      *******"
    h = "*****     *********     *****     *********    *  *      *******     *******    ********     *   *     ******"
    i = "*****     *********     *****     ********      **   *    *********     *******     ****      * *      ******"
    j = "*****     *********     *****         ****         ****    *****         ***         *****           ********"
    k = "*************************************************************************************************************"
    l = "*************************************************************************************************************"

    alpha = [a, b, c, d, e, f, g, h, i, j, k, l]

    for i in alpha:
        print(i)

# ==================================================================
# MAIN FUNCTION STARTS:

def main():
    print()
    print(
        '"You groggily wake up from your long afternoon nap. Your mouth feeling like cotton and your stomach faintly growling, you notice your clock reads 8:30pm."\n'
    )

    #Function call:
    pause_long()

    print(
        '"As you search on your phone to order from your favorite pizza restaurant, you notice that the ordering time will be delayed. Seems like everyone else is ordering in tonight. Not bothering to wait, you notice an advertisement for a new pizza ordering app from a restaurant called "Picasso\'s Pizzeria". Curious, you download their app and decide to take the plunge..."\n'
    )
    print()

    #Function call:
    pause_long()

    # Function call:
    game_start()

    print()

    print(
        "Welcome to Picasso's Pizzeria! Where we give you freedom on making the pizza you want!\n"
    )
    print("My name is Picasso! Yep, THE Picasso! I am here to be your personal pizza making guide.")
    print("To get started, what is your name?")

    # Function call:
    name = player_name()

    #Function call:
    pause()

    print(f"Nice to meet you, {name}!\n")

    #Function call:
    pause()

    print("First, you'll pick what sized pizza you want. We have a four pizza sizes.\n")
    print("-" * 20)
    print("<> Small (S), 10'\n<> Medium (M), 12'\n<> Large (L), 14'\n<> Extra Large (XL), 17'")
    print("-" * 20)


    #Function call:
    pause_long()

    print(f"What size do you fancy, {name}?")

    #Function call:
    size_choice = pizza_size_choice()
    size_pizza_list = [size_choice]
    final_list_items = size_pizza_list

    #Function call:
    pause()

    print()
    print(
        "Now, for the fun part! Dressing up your pizza with our mouth-watering toppings. Feast your very eyes on our unique menu!"
    )
    print()

    #Function call:
    pause_long()
    pause()
    # Function call Menu:
    printed_menu_toppings()

    #Function call:
    pause_long()

    print(
        "You can choose up to 6 different toppings from any of the categories. Just enter the number corresponding to the topping, and we will add it to your pizza.\n"
    )

    # Function call:
    player_topping_choices()
    topping_list_to_dict()

    # Function call:
    current_topping_list()

    # Function call:
    reSelection_toppings()
    final_selected_toppings()

    # Function call:
    processing_order()

    print()

    # Function call:
    display_printed_cost()

    #Function call:
    final_item_cost_display()
    #Function call:
    final_item_cost()

    print('-'*30)
    final_total_cost = get_total()
    print(f"Total cost is: ${final_total_cost:.2f}")
    print('-'*30)
    print("How much tip would you like to add today?")
    print("$", end="")
    tip = player_tip()

    #Tip Function call:
    total_final_bill = calculate_total_bill(final_total_cost, tip)

    print(f"Your total bill including tax and tip, comes out to ${total_final_bill:.2f}.\n")

    #Function call:
    pause()

    print("Looks like your pizza's estimated delivery time is about 30min...")

    #Function call:
    pause()

    print("In the meantime, would you like a sneak peak of what you can expect your pizza to look like?")

    #TURTLE graphics time:
    #Function call:
    pizza_preview()
    pizza_outline()

    #Function call: Pizza design output
    pizza_turtle_drawing()

    cutting_pizza()

    #END GAME:
    print()

    #Function call:
    continue_key()

    print()
    print(f"We hope this pizza preview made your mouth water, {name}!")
    print()
    print("It has been a pleasure being your guide for today. Please, come order again from Picasso's Pizzeria soon!")

    #Function call:
    closing_game()

    #Function call:
    pause()

    print()
    print('"As your eyes view the supposed "creation" that your pizza will look like when it is delivered.\nYou feel all sorts of mixed emotions--dread, excitement, anxious, but mostly you wonder whether this was worth it."')

    #Function call:
    pause()

    print()
    print('"Guess the only way is for you to find out later tonight..."')


    #Function call:
    pause_long()
    pause_long()
    pause_long()

    print()
    print()
    print("Thanks for playing Picasso's Pizzeria!!\nFeel free to play the game again and see what other fun pizza creations and combinations you can make!")
    print("Picasso has also been working hard on a piece and would like to show you as thanks.\nEnjoy!\n" )

    #Function call:
    continue_key()
    pause()

    #Function call
    picasso_drawing()

# Calling main function:
main()
