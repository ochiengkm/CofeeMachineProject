from CoffeeService import money, order_choice
from Menu import MENU, resources

machine_on = True


def my_function():
    change = money - MENU[order_choice]["cost"]

    def order():
        coffee = True
        while coffee:
            for thing, amount in resources.items():
                if amount > 0:
                    if money < MENU[order_choice]["cost"]:
                        print("Insufficient funds, money refunded!")
                        return
                    else:
                        resources["money"] = 0
                        if order_choice == "espresso":
                            resources["water"] -= 50
                            resources["coffee"] -= 18
                            resources["money"] += 1.5
                            print(f"Here is your ${change} in change")
                            print("Here is your espresso. Enjoy!")

                        if order_choice == "latte":
                            resources["water"] -= 200
                            resources["coffee"] -= 24
                            resources["milk"] -= 150
                            resources["money"] += 2.5
                            print(f"Here is your ${change} in change")
                            print("Here is your latte. Enjoy!")

                        if order_choice == "cappuccino":
                            resources["water"] -= 250
                            resources["coffee"] -= 24
                            resources["milk"] -= 100
                            resources["money"] += 3
                            print(f"Here is your ${change} in change")
                            print("Here is your cappuccino. Enjoy!")

                else:
                    print(f"Sorry, there is not enough {thing}")
                return resources

    order()


while machine_on:
    my_function()
