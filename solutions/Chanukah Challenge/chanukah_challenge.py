for r in range(int(input())):
    inputs = list(map(int, input().split()))
    n = inputs[1]
    for i in range(int(n)):
        n += 1+i
    print(r+1, n)
