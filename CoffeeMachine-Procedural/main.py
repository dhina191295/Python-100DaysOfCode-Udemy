MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from art import cofee_emoji

money = 0
machine_state = True


def resource_availability(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]

    if drink != "espresso":
        milk = MENU[drink]["ingredients"]["milk"]
        if resources["water"] >= water and resources[
                "milk"] >= milk and resources["coffee"] >= coffee:
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            return True
        else:
            return False
    else:
        if resources["water"] >= water and resources["coffee"] >= coffee:
            resources["water"] -= water
            resources["coffee"] -= coffee
            return True
        else:
            return False


def get_money(drink):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (
        pennies * 0.01)
    drink_cost = MENU[drink]["cost"]
    if drink_cost <= total_amount:
        change_amount = total_amount - drink_cost
        return change_amount
    else:
        print(
            f"You have provided insufficient funds.\nHere is your {total_amount}. /nMoney refunded."
        )
        return 0


while machine_state:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        machine_state = False
        break
    elif drink == "report":
        for i in resources:
            if i == "coffee":
                print(f"{i.title()}: {resources[i]}g")
            else:
                print(f"{i.title()}: {resources[i]}ml")
        print(f"Money: ${money}")
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        resource_available = resource_availability(drink)
        if (resource_available):
            change_amount = get_money(drink)
            money += MENU[drink]["cost"]
            if change_amount == 0:
                break
            else:
                format_change_amount = "{:.2f}".format(change_amount)
                # print(format_change_amount)
                print(f"Here is {format_change_amount} in change.")
                print(f"Here is your {drink} {cofee_emoji}. Enjoy!")
        else:
            if MENU[drink]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water.")
            elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee.")
            elif drink != "espresso":
                if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
                    print("Sorry there is not enough milk.")


# Instructor Solution
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
