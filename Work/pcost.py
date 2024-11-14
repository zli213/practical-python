# pcost.py
#
# Exercise 1.27
# with open('Data/portfolio.csv', 'rt') as f:
#     next(f)
#     sum = 0
#     for line in f:
#         row = line.split(',')
#         sum += int(row[1]) * float(row[2])
# print(f'Total cost {sum}')
######
import gzip
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
#     next(f)
#     sum = 0
#     for line in f:
#         row = line.split(',')
#         sum += int(row[1]) * float(row[2])
# print(f'Total cost {sum}')


def portfolio_cost(filename):
    if filename.endswith('.gz'):
        opener = gzip.open
    else:
        opener = open
    with opener(filename, 'rt') as f:
        next(f)
        sum = 0
        for line in f:
            try:
                row = line.split(',')
                sum += int(row[1]) * float(row[2])
            except ValueError as e:
                print(f'{e}')
    return sum


# cost = portfolio_cost('Data/portfolio.csv')
cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
