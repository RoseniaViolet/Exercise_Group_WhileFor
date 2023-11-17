x = float(input('Enter X:'))
guess = x/2
while abs(guess * guess -x) > 1e-12 :
    guess = (guess + x / guess) /2.0
print(f'The square root of {x} is {guess}')
