class MoneyMachine:
    global MONEY
    MONEY = 0

    def __init__(self):
        self.quarters = 0.25
        self.dimes = 0.10
        self.nickels = 0.05
        self.pennies = 0.01

    # @staticmethod
    # def report():
    #     print(f"Money: ${MONEY}")

    def get_money(self):
        print("Please insert coins:")
        total_money = 0
        total_money += (self.quarters * float(input("How many quarters?: ")))
        total_money += (self.dimes * float(input("How many dimes?: ")))
        total_money += (self.nickels * float(input("How many nickels?: ")))
        total_money += (self.pennies * float(input("How many pennies?: ")))
        return total_money

    @staticmethod
    def is_enough_money(total_money, drink_cost):
        if drink_cost <= total_money:
            print("Here is your change " + "{:.2f}".format(total_money-drink_cost))
            global MONEY
            MONEY += drink_cost
            return True
        else:
            print(f"Sorry There is not enough money. Money refunded: ${total_money}")
            return False

    @staticmethod
    def get_stored_money():
        return MONEY
