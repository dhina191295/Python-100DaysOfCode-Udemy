from MoneyMachine import MoneyMachine
from art import logo
from MenuList import MenuObj as Menu
from CoffeeMachine import CoffeeMachine
from Resources import Resources


print(logo)
machine_state = True

tmp_money = MoneyMachine()

while machine_state:
    new_drink = CoffeeMachine()
    new_drink.print_menu()
    drink = new_drink.get_user_choice()

    if drink == "off":
        machine_state = False
        break
    elif drink == "report":
        resource_in_machine = Resources(drink)
        resource_in_machine.report()
        print(f"Money: ${tmp_money.get_stored_money()}")

    elif drink in Menu.menu().keys():
        resource_in_machine = Resources(drink)
        if resource_in_machine.is_resources_available():
            user_money = MoneyMachine()
            user_money_collected = user_money.get_money()
            drink_cost = Menu.menu()[drink]["cost"]
            if user_money.is_enough_money(user_money_collected, drink_cost):
                new_drink.deliver(drink)
    else:
        print("Choose a choice from the given Menu")
