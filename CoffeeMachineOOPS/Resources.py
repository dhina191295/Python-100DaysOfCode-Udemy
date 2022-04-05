from MenuList import MenuObj as Menu


class Resources:
    global RESOURCES
    RESOURCES = {
        'water': 300,
        'milk': 200,
        'coffee': 100
    }

    def __init__(self, drink):
        if drink != "report":
            self.b_water = Menu.menu()[drink]["ingredients"]["water"]
            self.b_coffee = Menu.menu()[drink]["ingredients"]["coffee"]
            if drink == "espresso":
                self.b_milk = 0
            else:
                self.b_milk = Menu.menu()[drink]["ingredients"]["milk"]
        else:
            pass

    @staticmethod
    def report():
        global RESOURCES
        print(f"water: {RESOURCES['water']}ml")
        print(f"Milk: {RESOURCES['milk']}ml")
        print(f"Coffee: {RESOURCES['coffee']}ml")

    def is_resources_available(self):
        global RESOURCES
        if self.b_water <= RESOURCES["water"] and self.b_milk <= RESOURCES["milk"] and self.b_coffee <= RESOURCES[
            "coffee"]:
            RESOURCES["water"] -= self.b_water
            RESOURCES["milk"] -= self.b_milk
            RESOURCES["coffee"] -= self.b_coffee
            return True
        else:
            if self.b_water > RESOURCES["water"]:
                print("Sorry There is no enough water.")
            elif self.b_milk > RESOURCES["milk"]:
                print("Sorry There is no enough milk.")
            else:
                print("Sorry There is no enough coffee.")
            return False
