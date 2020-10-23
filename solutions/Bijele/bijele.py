set = list(map(int, input().split()))
index = 0
original_set = [
    1, 1, 2,
    2, 2, 8
    ]

for card in set:
    do = original_set[index] - card
    print(do, end=" ")
    index += 1
