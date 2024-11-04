# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    sum = 0
    for line in f:
        row = line.split(',')
        sum += int(row[1]) * float(row[2])
print(f'Total cost {sum}')
