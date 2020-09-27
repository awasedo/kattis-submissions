str = input()
chars = []

for element in str:
    if element.isupper():
        chars.append(element)

print("".join(chars))
