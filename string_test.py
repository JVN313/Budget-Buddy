def String_Test(value):
    while isinstance(value, str) == True:
        
        try:
            value = float(value)
            return value
            
        except ValueError:
            value = input("Invalid Input: Please Write Price In Numeral Form.\nNew Value: ")
            continue
