import datetime

def Shopping_Mode():
    global shopping_list,prices
    budget = float(input("What is your budget for this shopping trip?\n$"))

    shopping_list = []
    prices = []

    def tax(price):
        sales_tax= price * 0.06
        return sales_tax

    def repeat_ShopMode():
        repeat_SM_options = ["A","B","DONE","NO","N"]
        user_responseSM = input("If You Would Like To Create A New Budget & Shopping List PRESS 'A'.\nIf You Would Like To Go Into SALES TAX MODE PRESS 'B'.\nOr TYPE 'DONE' To End The Program\n").upper()
        
        while user_responseSM not in repeat_SM_options:
            print("INVALID RESPONSE")
            user_responseSM = input("If You Would Like To Create A New Budget & Shopping List PRESS 'A'.\nIf You Would Like To Go Into SALES TAX MODE PRESS 'B'.\nOr TYPE 'DONE' To End The Program: \n").upper()
        
        if user_responseSM == "A":
            Shopping_Mode()
        elif user_responseSM == "B":
            SalesTax_Mode()
        elif user_responseSM == "DONE" or user_responseSM == "NO" or user_responseSM == "N":
            print("Thanks For Using Budget Buddy!")
            List_Saver()
            quit()

    filling_list =  True
    while filling_list:
        shopping_list.append(input("What's on your shopping list? (Type 'Done' When Finished Adding Items): ").upper())
        if "DONE" in shopping_list:
            shopping_list.pop()
            filling_list = False
        
        if shopping_list[-1] == "":
            print("It Looks Like You Didn't Add An Item Correctly. Try Again")
            shopping_list.pop()
            continue

    for i in shopping_list:
        prices.append(float(input(f"What does {i} cost?: $")))

    prices_sum = sum(prices)
    shopping_total = round(prices_sum + tax(prices_sum), 2)

    if shopping_total >  budget:
        print(f"You're Over Budget! by ${round(shopping_total - budget, 2)}")
        most_expensiive = prices.index(max(prices))
        print(f"Expected Shopping Total With Tax Total of ${round(tax(prices_sum), 2)} Is: ${shopping_total} / Without Tax: ${prices_sum}")
        print(f"Recommended Item Removal: {shopping_list[most_expensiive]}")
        repeat_ShopMode()
    elif budget >= shopping_total:
        print(f"You're within your budget with ${round(budget - shopping_total, 2)} left over.")
        print(f"Expected Shopping Total With Tax Total of ${round(tax(prices_sum), 2)} Is: ${shopping_total} / Without Tax: ${round(prices_sum, 2)}")
        repeat_ShopMode()

def SalesTax_Mode():
    unit_price = float(input("Input Price: $"))
    def tax_adding(price):
        sales_tax = price * 0.06
        true_total = price +  sales_tax
        print(f"Total Price With Tax: ${round(true_total, 2)}")

    def repeat_SalesTaxMode():
        repeat_STM_options = ["A","B","DONE","NO","N"]
        user_responseSTM = input("If You Would Like Input Another Price PRESS 'A'.\nIf You Would Like To Go Into SHOPPING MODE PRESS 'B'.\nOr TYPE 'DONE' To End The Program\n").upper()
        
        while user_responseSTM not in repeat_STM_options:
            print("INVALID RESPONSE")
            user_responseSTM = input("If You Would Like To Create A New Budget & Shopping List PRESS 'A'.\nIf You Would Like To Go Into SALES TAX MODE PRESS 'B'.\nOr TYPE 'DONE' To End The Program: \n").upper()
        
        if user_responseSTM == "B":
            Shopping_Mode()
        elif user_responseSTM == "A":
            SalesTax_Mode()
        elif user_responseSTM == "DONE" or user_responseSTM == "NO" or user_responseSTM == "N":
            print("Thanks For Using Budget Buddy!")
            quit()

    tax_adding(unit_price)
    repeat_SalesTaxMode()


def List_Saver():
    x = datetime.datetime.now()
    date = f"{x.month}-{x.day}-{x.year}"
    saved_list = dict(zip(shopping_list,prices))
    saved_list_file = open(f"Lists/List-{date}.txt","w+")
    saved_list_file.write(str(saved_list))
    saved_list_file.close()

def Mode_Selector():
    print("WELCOME TO BUDGET BUDDY!")
    options = ["A","SHOPPING MODE","SHOPPING","B","SALES TAX MODE","SALES TAX","SALES"]
    shopping_mode_options = ["A","SHOPPING MODE","SHOPPING"]
    salestax_mode_options = ["SALES TAX MODE","SALES TAX","B","SALES"]

    user_input = input("Select Which Operating Mode You Would Like To Use:\nA) Shopping Mode\n In this mode, you tell Budget Buddy your budget and shopping list, including items and prices. Then it will get a total of your list plus tax and let you knoow if you're Over or Under Budget!\nB) Sales Tax Mode\n In this mode, you input an item price and Budget Buddy will give you the total plus tax\n").upper()

    while user_input not in options:
        print("NOT A VALID OPTION TRY AGAIN")
        user_input = input("Select Which Operating Mode You Would Like To Use:\nA) Shopping Mode\n In this mode, you tell Budget Buddy your budget and shopping list, including items and prices. Then it will get a total of your list plus tax and let you knoow if you're Over or Under Budget!\nB) Sales Tax Mode\nIn this mode, you input an item price and Budget Buddy will give you the total plus tax\n").upper()

    if user_input in shopping_mode_options:
        Shopping_Mode()
    elif user_input in salestax_mode_options:
        SalesTax_Mode()

Mode_Selector()