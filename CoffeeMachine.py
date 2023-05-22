coffee = {"espresso":{"water":10,"milk":20,"coffee":10,"money":20},
          "latte":{"water":20,"milk":30,"coffee":20,"money":30},
          "cappuccino":{"water":30,"milk":40,"coffee":30,"money":40}}

resources = {"water":300,"milk":300,"coffee":300,"money":0}

def prompt():
    decision = input("\nWhat would you like? (espresso(₹20)/latte(₹30)/cappuccino(₹40)):  ").lower()
    return decision

def checkresources(coffeetype):
    global coffee
    global resources
    s=0
    for x in resources:
        if resources[x]>=coffee[coffeetype][x]:
            s=s+1
        elif x == "money":
            continue
        else:
            return False,x
    if s==3:
        for x in resources:
            if x=="money":
                continue
            resources[x] = resources[x] - coffee[coffeetype][x]
        return True,""
    
def generatereport():
    global resources
    for x in resources:
        print(f"{x}: {resources[x]}")
    #print(resources["money"])

def addresource(toadd,howmuchtoadd):
    global resources
    resources[toadd] = resources[toadd] + howmuchtoadd

def start():
    global coffee
    global resources

    userinput = prompt()
    if userinput == 'espresso' or userinput == 'latte' or userinput == 'cappuccino':
        resourcecheck, notsufficient = checkresources(userinput)
        if resourcecheck == True:

            print("Please enter coins.")
            onerupee = int(input("How many ₹1?: "))
            tworupee = int(input("How many ₹2?:  "))
            fiverupee = int(input("How many ₹5?:  "))
            tenrupee = int(input("How many ₹10?:  "))

            moneyinput = onerupee*1 + tworupee*2 + fiverupee*5 + tenrupee*10

            if moneyinput>coffee[userinput]["money"]:
                userchange = moneyinput - coffee[userinput]["money"]
                resources["money"] += coffee[userinput]["money"]
                print(f"\nHere is your ₹{userchange} in change.")
                print(f"\nHere is your {userinput}. Enjoy!") 

            elif moneyinput==coffee[userinput]["money"]:
                resources["money"] += coffee[userinput]["money"]
                print(f"\nHere is your {userinput}. Enjoy!")

            else:
                print(f"\nNot enough money. ")

            start()

        elif resourcecheck == False:
            print(f"Sorry there is not enough {notsufficient}.")

    elif userinput == "report":
        generatereport()

    elif userinput == "off":
        exit()

    elif userinput == "add":
        useradd = input("What do you want to add? Water, milk or coffee: ").lower()
        quantityadd = int(input(f"How much {useradd} do you want to add?:  "))
        if useradd == "water" or useradd == "milk" or useradd == "coffee":
            addresource(useradd,quantityadd)
    
    else:
        exit()
    start()
start()



    
                



            



