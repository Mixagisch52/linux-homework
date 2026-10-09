#! /opt/homebrew/bin/python3
dna = input()
gc = (dna.count('G') + dna.count('C')) / len(dna)
print(f'{gc:.2%}')
