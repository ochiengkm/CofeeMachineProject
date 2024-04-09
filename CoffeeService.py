from Menu import resources

report = True


def prompt():
    # prompt the user to select coffee type
    while report:
        choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
        if choice == "report":
            for resource, value in resources.items():
                print(f"{resource}: {value}")
        else:
            return choice


order_choice = prompt()


def dollar_convert():
    # Convert different denominations to dollars
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    dollars = round(total, 2)
    return dollars


quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))
money = dollar_convert()
