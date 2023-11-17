from random import randrange
num = 100
max_num = randrange(1, num + 1)
print(max_num)
updates = 0
count = 1
while count < num:
    current = randrange(1, num + 1)
    if current > max_num:
        max_num = current
        updates += 1
        print(f'{current}   <= Update')
    else:
        print(f'{current}')
    count += 1
print(f'The maximum number found was {max_num}')
print(f'The maximum number was updated {updates} times')
