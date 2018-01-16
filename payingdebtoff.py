def payingdebtoff (balance, annualInterestRate, monthlyPaymentRate):
    """
    Calculates the credit card balance after one year if only the monthly
    minimum required by the credit card company is paid
    :param balance: outstanding balance on the credit card
    :param annualInterestRate: annual interest rate as a decimal
    :param monthlyPaymentRate: minimum monthly payment rate as a decimal
    :return: remaining balance with two decimals of accuracy
    """

    i = 0
    while i < 12:
        minimum_payment = balance * monthlyPaymentRate
        unpaid_balance = balance - minimum_payment
        interest = annualInterestRate / 12.0 * unpaid_balance
        cc_balance = unpaid_balance + interest
        balance = cc_balance
        i += 1

    return round(cc_balance, 2)


print(payingdebtoff(42, 0.2, 0.04))
print(payingdebtoff(484, 0.2, 0.04))
