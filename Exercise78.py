result = ""
q = int(input("Enter a decimal number: "))
while q != 0:
    r = q % 2
    result = str(r) + result
    q //= 2
print("Binary representation:", result)
