#! /opt/homebrew/bin/python3

dna1 = list(input())
dna2 = []
for i in dna1:
	if i == 'A':
		dna2.append('T')
	elif i == 'T':
		dna2.append('A')
	elif i == 'C':
		dna2.append('G')
	else:
		dna2.append('C')
print(''.join((dna2[::-1])))
