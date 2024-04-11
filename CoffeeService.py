from Menu import resources, MENU

report = True
machine_on = True


def prompt(machine_on):
    # prompt the user to select coffee type or print resources left
    while report and machine_on:
        choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
        if choice == "power":
            return False
            break
        elif choice == "report":
            for resource, value in resources.items():
                print(f"{resource}: {value}")
        elif choice not in MENU:
            print("Invalid option, try again")
        else:
            return choice
    return None


def dollar_convert(quarters, dimes, nickels, pennies):
    # Convert different denominations to dollars
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    dollars = round(total, 2)
    return dollars


def order():
    global order_choice
    if order_choice == "espresso" or order_choice == "latte" or order_choice == "cappuccino":
        dollar_convert(quarters, dimes, nickels, pennies)
    else:
        print("Incorrect option, please try again")
        return prompt(True)


def coffee_order():
    global order_choice, money
    if order_choice in MENU:
        cost = MENU[order_choice]["cost"]
        if money < cost:
            print(f"Insufficient funds, moneys refunded ${money}!")
        else:
            for ingredient, amount in MENU[order_choice]["ingredients"].items():
                resources[ingredient] -= amount
            resources["money"] += cost
            print(f"Here is your {order_choice}, enjoy!")
            if money > cost:
                change = money - cost
                print(f"Here is your ${change} in change")
    else:
        print("Incorrect option, please try again")


def enough():
    global money, order_choice
    if money < MENU[order_choice]["cost"]:
        print(f"Insufficient funds, money refunded ${money}!")
    else:
        # resources["money"] += money
        coffee_order()
        order()


while machine_on:
    order_choice = prompt(machine_on)
    if order_choice is False:  # Check if the machine should be turned off
        machine_on = False
        break
    if machine_on:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        money = dollar_convert(quarters, dimes, nickels, pennies)
        enough()
