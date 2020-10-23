dice = list(map(int, input().split()))
dice = sorted(dice)
for i in range(1+dice[0], 2+dice[1]):
    print(i)
