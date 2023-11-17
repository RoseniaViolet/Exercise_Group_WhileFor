from random import randrange
total_flips = 0
for _ in range(10):
    count = 0
    consecutive = 0
    again_result = None
    while consecutive < 3:
        result = randrange(2)
        count += 1
        if count > 1:
            if result == again_result:
                consecutive += 1
            else:
                consecutive = 1
        print('H ' if result == 0 else 'T ', end='')
        again_result = result
    total_flips += count
    print(f'({count} flips)')
average_flips = total_flips / 10
print(f'On average, {average_flips} flips were needed')
