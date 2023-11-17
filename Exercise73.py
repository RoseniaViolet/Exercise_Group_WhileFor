string = input('Enter a string:')
special_characters =(' ',',','?',';','!','.')
reverse = ''
reverse_convert = ''
for i in string:
    if i in special_characters :
        reverse = i.replace(i,'') + reverse
    else :
        reverse += i
for n in reverse:
    reverse_convert =  n + reverse_convert
if reverse == reverse_convert:
    print(f'{string} is palindrome string')
else :
    print(f'{string} not is palindrome string')