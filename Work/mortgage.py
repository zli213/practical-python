# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
totalMonth = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    if totalMonth <= extra_payment_end_month and totalMonth >= extra_payment_start_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    totalMonth = totalMonth + 1

print('Total paid:', round(total_paid, 2), ', month:', round(totalMonth))
