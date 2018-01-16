def payingdebtoff (balance, annualInterestRate):
    """
    Calculates the minimum payment needed to pay off credit card balance in twelve months.
    Minimum payment must be a multiple of 10.
    :param balance: outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :return:
    """

    payment = 0
    estimated_balance = balance

    while estimated_balance >= 0:

        # following three declarations reset variables used within internal while loop
        i = 1
        estimated_balance = balance
        payment += 10

        while i <= 12:
            estimated_balance = estimated_balance - payment
            monthly_interest = annualInterestRate / 12.0 * estimated_balance
            cc_balance = estimated_balance + monthly_interest
            estimated_balance = cc_balance
            i += 1

    print("Lowest payment: ", payment)


print(payingdebtoff(3329, 0.2))
print(payingdebtoff(4773, 0.2))
print(payingdebtoff(3926, 0.2))
