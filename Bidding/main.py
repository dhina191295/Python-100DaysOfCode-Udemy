import os
from art import logo

print(logo)

bid_data = {}
exit_flag = False

while not exit_flag:
    name = input("What is your name?: ")
    bid_amount = int(input("what's your bid?: $"))
    bid_data[name] = bid_amount
    restart_value = input("If there are other bidders, please type yes else type no: ").lower()
    os.system('cls')
    if restart_value == "no":
        exit_flag = True
        max_amount = 0
        max_name = ""
        for name in bid_data:
            if max_amount < bid_data[name]:
                max_amount = bid_data[name]
                max_name = name
        print(f"The highest bidder is {max_name} and the bid amount is {max_amount}")
        print("Thank you")
