from MenuList import MenuObj as Menu
from art import coffee_emoji


class CoffeeMachine:
    def __init__(self):
        self.count = 0

    def print_menu(self):
        print("MENU:")
        for i in Menu.menu():
            self.count += 1
            print(f"{self.count}:{i}")

    @staticmethod
    def get_user_choice():
        drink = input("What would you like? ").lower()
        return drink

    # def check_resources(self, drink):
    #     if drink != "espresso":
    #         water = MENU.menu()[drink]["ingredients"]["water"]
    #         milk = MENU.menu()[drink]["ingredients"]["milk"]
    #         coffee = MENU.menu()[drink]["ingredients"]["coffee"]
    #     else:
    #         water = MENU.menu()[drink]["ingredients"]["water"]
    #         milk = MENU.menu()[drink]["ingredients"]["milk"]
    #         coffee = 0

    @staticmethod
    def deliver(drink):
        print(f"Here is your {drink} {coffee_emoji}. Enjoy !")
