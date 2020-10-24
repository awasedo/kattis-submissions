string = input()

combs = [
    "epe",
    "apa",
    "upu",
    "ipi",
    "opo"
]

for comb in combs:
    string = string.replace(comb, comb[:1])

print(string)
