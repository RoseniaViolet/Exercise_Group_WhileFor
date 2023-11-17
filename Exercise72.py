string= input('Enter a string:')
reverse = string
reverse_convert =''
for i in string:
    reverse_convert = i + reverse_convert
if reverse == reverse_convert:
    print(f'{string} is palindrome string')
else :
    print(f'{string} not is palindrome string')
