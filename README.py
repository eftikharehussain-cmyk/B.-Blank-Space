# B.-Blank-Space
t  = int(input())
for _ in range(t):
	n = int(input())
	lst = list(map(int, input().split()))
	count = 0
	bigest = 0
	for i in lst:
		if i == 0:
			count += 1
			if count >= bigest:
				bigest = count
		if i != 0:
			count = 0
	print(bigest)
