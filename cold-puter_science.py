n = int(input())
Temperatures = list(map(int, input().split()))
print(len([t for t in Temperatures if t < 0]))
