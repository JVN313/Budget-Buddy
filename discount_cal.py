from string_test import String_Test
from number_test import Number_Test

def Discount_Cal():
    price = float(String_Test(input("Enter Regular Price: $")))
    discount = Number_Test(input("Input Discount Amount: %"))
    discount = float("0." + discount)
    discount_num = price * discount
    sale_price = round(price - discount_num, 2)
    new = list(str(sale_price))

    if len(new) <= 4:
        new = "".join(new)
        new = new + "0"
        print(f"The discounted price is ${new}")
    else:
        print(f"The discounted price is ${sale_price}")

    rerun = input("Would you like to find a new price?: ").upper()
    rerun_options = ["YES","Y"]

    if rerun in rerun_options:
        Discount_Cal()
   