print("WELCOME TO BUDGET BUDDY!")
def Shopping_Mode():
    budget =int(input("What is your budget for this shopping trip?\n"))

    shopping_list = []
    prices = []

    def tax(price):
        sales_tax= price * 0.06
        return sales_tax

    filling_list =  True
    while filling_list:
        shopping_list.append(input("What's on your shopping list? (Type 'Done' When Finished Adding Items): ").upper())
        if "DONE" in shopping_list:
            shopping_list.pop()
            filling_list = False

    for i in shopping_list:
        prices.append(float(input(f"What does {i} cost? ")))

    prices_sum = sum(prices)
    shopping_total = round(prices_sum + tax(prices_sum), 2)

    if shopping_total >  budget:
        print(f"You're Over Budget! by {round(shopping_total - budget, 2)}")
        most_expensiive = prices.index(max(prices))
        print(f"Expected Shopping Total {shopping_total}")
        print(f"Recommended Item Removal: {shopping_list[most_expensiive]}")
        print("Thanks For Using Budget Buddy!")
    elif budget >= shopping_total:
        print(f"You're within your budget with {round(budget - shopping_total, 2)} left over.")
        print(f"Expected Shopping Total {shopping_total}")
        print("Thanks For Using Budget Buddy!")

def SalesTax_Mode():
    unit_price = float(input("Input  Price: "))
    def tax_adding(price):
        sales_tax = price * 0.06
        true_total = price +  sales_tax
        print(round(true_total, 2))

    tax_adding(unit_price)
    while True:
        replay = input("Would You Like To Input Another Price? ").upper()
        if replay == "YES":
          unit_price = float(input("Input  Price: "))
          tax_adding(unit_price)
        else:
            return False
    
    print("Thanks For Using Budget Buddy!")

def Mode_Selector():
    options = ["A","SHOPPING MODE","SHOPPING","B","SALES TAX MODE","SALES TAX"]
    shopping_mode_options = ["A","SHOPPING MODE","SHOPPING"]
    salestax_mode_options = ["SALES TAX MODE","SALES TAX","B"]

    user_input = input("Select Which Operating Mode You Would Like To Use:\nA) Shopping Mode\n In this mode, you tell Budget Buddy your budget and shopping list, including items and prices. Then it will get a total of your list plus tax and let you knoow if you're Over or Under Budget!\nB) Sales Tax Mode\n In this mode, you input an item price and Budget Buddy will give you the total plus tax\n").upper()

    while user_input not in options:
        print("NOT A VALID OPTION TRY AGAIN")
        user_input = input("Select Which Operating Mode You Would Like To Use:\nA) Shopping Mode\n In this mode, you tell Budget Buddy your budget and shopping list, including items and prices. Then it will get a total of your list plus tax and let you knoow if you're Over or Under Budget!\nB) Sales Tax Mode\nIn this mode, you input an item price and Budget Buddy will give you the total plus tax\n").upper()

    if user_input in shopping_mode_options:
        Shopping_Mode()
    elif user_input in salestax_mode_options:
        SalesTax_Mode()

Mode_Selector()