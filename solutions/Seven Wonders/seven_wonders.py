Ts = 0
Gs = 0
Cs = 0

for char in input():
    if char=="T":
        Ts += 1
    elif char=="G":
        Gs += 1
    else:
        Cs += 1

points = (Ts**2)+(Gs**2)+(Cs**2)+(7*min(Ts, Gs, Cs))

print(points)
