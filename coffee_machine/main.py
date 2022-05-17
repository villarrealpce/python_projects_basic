import os
# configuration of menu and resources

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

# **********  Funtions block  **********
def report (money):
    # TODO 3: Print report.
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")

def reposition_of_resources(money):
    water_r = int(input("reposition of resources --> Water: " ))
    coffee_r = int(input("reposition of resources --> Coffee: " ))
    milk_r = int(input("reposition of resources --> Milk: " ))

    resources['water'] += water_r
    resources['coffee'] += coffee_r
    resources['milk'] += milk_r

    print ("Updated inventory.......")
    report(money)

def check_resources(type_coffee):
    # TODO 4: Check resources sufficient
    if type_coffee == "espresso":
        if resources['water'] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            return True
    if type_coffee == "latte":
        if resources['water'] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        else:
            return True
    if type_coffee == "cappuccino":
        if resources['water'] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources['coffee'] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        elif resources['milk'] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        else:
            return True

def process_coins(cost_coffee):
    cant_quarter = int(input("Insert quarter coins: "))
    cant_dimes = int(input("Insert dimes coins: "))
    cant_nickel = int(input("Insert nickel coins: "))
    cant_pennies = int(input("Insert pennies coins: "))

    # TODO 6: Check transaction successful?
    total_coins = (cant_quarter * 0.25) + (cant_dimes * 0.1) + (cant_nickel * 0.05)+ (cant_pennies * 0.01)
    if total_coins < cost_coffee:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is {round(total_coins-cost_coffee, 2)} dollars in change.")
        return True
    
def make_coffee(type_coffee):
    # TODO 7: Make Coffee.
    if type_coffee == "espresso":
        resources['water'] -= MENU["espresso"]["ingredients"]["water"]
        resources['coffee'] -= MENU["espresso"]["ingredients"]["coffee"]
    elif type_coffee == "latte":
        resources['water'] -= MENU["latte"]["ingredients"]["water"]
        resources['coffee'] -= MENU["latte"]["ingredients"]["coffee"]
        resources['milk'] -= MENU["latte"]["ingredients"]["milk"]
    elif type_coffee == "cappuccino":
        resources['water'] -= MENU["cappuccino"]["ingredients"]["water"]
        resources['coffee'] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources['milk'] -= MENU["cappuccino"]["ingredients"]["milk"]
    print(f"Here is your {type_coffee}. Enjoy!")

# **********  End Funtions block  **********

# TODO 2: Turn off the Coffee Machine by entering “​ off​” to the prompt.
coffee="on"
money = 0
make_drink = False
coins_pro = False
make_coffees = False

while coffee != "off":
    print("*" * 100)
    print("Coffee Machine".center(100, "*"))
    print("*" * 100)
    # TODO 1 : Prompt user by asking
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "report":
        os.system('clear')
        report(money)

    elif coffee == "reposition":
        os.system('clear')
        reposition_of_resources(money)
    elif coffee == "off":
        os.system('clear')
        print("Machine in mantenamce.....")
        
    else:
        coins_pro = check_resources(coffee)

    if coins_pro:
        make_coffees = process_coins(MENU[coffee]["cost"])   
    if make_coffees:
        money += MENU[coffee]["cost"]
        make_coffee(coffee)
    input("Enter for continue: ")
    make_drink = False
    coins_pro = False
    make_coffees = False
    os.system('clear')
