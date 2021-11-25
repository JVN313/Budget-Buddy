price = float(input("Input Regular Price: $"))
discount = input("Input Discount: %")
discount = float("0." + discount)
discount_num = price * discount
sale_price = round(price - discount_num, 2)
new = list(str(sale_price))

if len(new) == 4:
    new = "".join(new)
    new = new + "0"
    print(new)
