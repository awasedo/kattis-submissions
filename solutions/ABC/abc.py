num = sorted(list(map(int, input().split())))
abc = list(input())

min_ordbok = {
    "A": num[0],
    "B": num[1],
    "C": num[2]
}

for letter in abc: 
    print(min_ordbok[letter], end=" ")
