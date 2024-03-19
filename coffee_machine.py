import math
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":200,
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
cost=0
working=True
check_re=True
def refill():
    resources["water"]=300
    resources["milk"]=200
    resources["coffee"]=100
def money(quator,dimes,nikles,pennies,coffee_type,meanue):
    total_money=quator*0.25+dimes*0.10+nikles*0.05+pennies*0.01
    if coffee_type == "espresso" and total_money>=MENU["espresso"]["cost"]:
        print("here"+ str(total_money-MENU["espresso"]["cost"]))
        cut_resouces(meanue)
        return True
    elif coffee_type == "latte" and total_money>=MENU["latte"]["cost"]:
        print("here"+ str(total_money-MENU["latte"]["cost"]))
        cut_resouces(meanue)
        return True
    elif coffee_type =="cappuccino" and total_money>=MENU["cappuccino"]["cost"]:
        print("here"+ str(total_money-MENU["cappuccino"]["cost"]))
        cut_resouces(meanue)
        return True
    else:
        print("Money is les here are your "+total_money)
        return False
def print_resources():
    print()
    print("Water left"+str(resources["water"]))
    print("milk left" + str(resources["milk"]))
    print("coffee left" + str(resources["coffee"]))
def cut_resouces(dictionary_send):
    #check if available
    if resources["water"]>=dictionary_send["ingredients"]["water"] and resources["milk"]>=dictionary_send["ingredients"]["milk"] \
            and resources["coffee"]>=dictionary_send["ingredients"]["coffee"]:
        print("resources avaiable")
        resources["water"]=resources["water"]-dictionary_send["ingredients"]["water"]
        resources["milk"] = resources["milk"] - dictionary_send["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - dictionary_send["ingredients"]["coffee"]

        return True
    else:
        print()
        print("not available")
        return False
def check_resouces(dictionary_send):
    if resources["water"]>=dictionary_send["ingredients"]["water"] and resources["milk"]>=dictionary_send["ingredients"]["milk"] \
            and resources["coffee"]>=dictionary_send["ingredients"]["coffee"]:
        print("resources avaiable")
        return True
    else:
        print()
        print("not available resouces")
        return False

while(working):
    checker=False
    store=input("1)espresso   \n2)latte/  \n3)cappuccino and \n4)'exit' for quiting and \n5)'report' for the generating report\n6)for refilling enter 'refill'").lower()
    print()
    if store=='refill':
        refill()
    if store=='exit':
        break
    if store=='report':
        print_resources()
        continue
    #check resources first
    checker=False
    cost=0
    if store=='espresso':
            checker=check_resouces(MENU["espresso"])
            cost=1.5
    elif store=='latte':
            checker=check_resouces(MENU["latte"])
            cost=2.5
    elif store=='cappuccino':
            checker=check_resouces(MENU["cappuccino"])
            cost=3.0
    if checker:
        #first take money from the clients
        print("Kindly do your payment first of:"+str(cost))
        quator=float(input("Quarters:"))
        dimes = float(input("Dimes:"))
        nikles = float(input("nikles:"))
        pennies = float(input("pennies:"))
        if store=="espresso":
            money_verify=money(quator,dimes,nikles,pennies,"espresso",MENU["cappuccino"])
        elif store=="latte":
            money_verify=money(quator,dimes,nikles,pennies,"latte",MENU["latte"])
        elif store=="cappuccino":
            money_verify=money(quator,dimes,nikles,pennies,"cappuccino",MENU["cappuccino"])
        #resources check
    else:
        print("Resouces not avaiable, please fill the resouces")





    
