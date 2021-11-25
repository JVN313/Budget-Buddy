def Number_Test(value):
    test_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    value = value.upper()
    testing = list(value)
    check = any(item in test_list for item in testing)

    while check == True:
        print("not a number")
        value = input("new num").upper()
        testing = list(value)
        check = any(item in test_list for item in testing)
        continue

    return value