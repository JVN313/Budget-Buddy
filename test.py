def loan_mode():
    mode_decision = ""
    loan_amount = int(input("Enter Loan Amount: "))
    monthly_payment = int(input("Desired Monthly Payment: "))
    time_needed = loan_amount / monthly_payment
    time_desired = int(input("How long would you like to pay off the loan?: "))

    print()

loan_mode()