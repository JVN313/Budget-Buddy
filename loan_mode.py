from string_test import String_Test

mode_decision = input("Select A Mode: ").upper()
mode_options = ["TIME MODE","PAYMENT MODE", "TIME", "PAYMENT"]
time_options = ["TIME MODE","TIME"]
payment_options = ["PAYMENT MODE","PAYMENT"]

while mode_decision not in mode_options:
    print("Invalid Input Please Try Again")
    mode_decision = input("Select A Mode: ").upper()

if mode_decision in payment_options:
    loan_amount = float(String_Test(input("Enter Loan Amount: ")))
    time_desired = float(String_Test(input("Within many months would you like to pay off the loan?: ")))
    monthly_payment = round(loan_amount / time_desired, 2)
    print(monthly_payment)
elif mode_decision in time_options:
    loan_amount = float(String_Test(input("Enter Loan Amount: ")))
    monthly_payment = float(String_Test(input("Desired Monthly Payment: ")))
    months_needed = round(loan_amount / monthly_payment, 2)
    print(months_needed)


