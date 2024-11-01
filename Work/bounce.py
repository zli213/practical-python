# bounce.py
#
# Exercise 1.5
original_height = 100
count = 1
while count < 11:
    jump_back_height = 3/5 * original_height
    original_height = jump_back_height
    print(round(original_height, 1))
    count = count + 1
