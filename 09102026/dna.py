#!/opt/homebrew/bin/python3
dna = input()
counter = [0, 0, 0, 0]
for i in range(len(dna)):
	if dna[i] == 'A':
		counter[0] += 1
	elif dna[i] == 'C':
		counter[1] += 1
	elif dna[i] == 'G':
		counter[2] += 1
	else:
		counter[3] += 1
print(counter[0], counter[1], counter[2], counter[3])

