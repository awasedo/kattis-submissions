inps = []
for i in range(int(input())):
	inp = list(map(str, input().split()))
	if inp[0] == ("Simon") and inp[1] == ("says"):
		inp.remove(inp[0])
		inp.remove(inp[0])
		inps.extend(inp)
		inps.append("\n")
print(" ".join(inps))
