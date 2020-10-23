c_per_m2 = input()
n_of_lawns = int(input())
m2s = 0

for i in range(n_of_lawns):
    dimensions = list(input().split())
    width = float(dimensions[0])
    length = float(dimensions[1])
    m2s += width * length

print("{:.7f}".format(float(c_per_m2)*m2s))
