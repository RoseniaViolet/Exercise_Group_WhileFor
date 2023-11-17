message = input("Enter the message: ")
shift = int(input("Enter the shift amount: "))
encrypted_message = ""

for char in message:
    if 'A' <= char <= 'Z':
        encrypted_char = chr((ord(char) - ord('A') + shift) + ord('A'))
    elif 'a' <= char <= 'z':
        encrypted_char = chr((ord(char) - ord('a') + shift) + ord('a'))
    else:
        encrypted_char = char
    encrypted_message += encrypted_char

print("Encrypted message:", encrypted_message)