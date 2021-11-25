from string_test import String_Test
from number_test import Number_Test

price = float(String_Test(input("Input Regular Price: $")))
discount = Number_Test(input("Input Discount: %"))
discount = float("0." + discount)
discount_num = price * discount
sale_price = round(price - discount_num, 2)
new = list(str(sale_price))

if len(new) == 4:
    new = "".join(new)
    new = new + "0"
    print(f"${new}")
else:
    print(sale_price)
