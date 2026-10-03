#!/opt/homebrew/bin/python3

import sys

dna = sys.argv[1].upper()

rna = dna.replace('T', 'U')

pairs = str.maketrans('ATGC', 'TACG')
complementary = dna.translate(pairs)

reverse_complementary = complementary[::-1]


start_codon_pos = dna.find('ATG')

print(f"РНК: {rna}")
print(f"Обратно-комплиментарная: {reverse_complementary}")
print(f"Позиция старт-кодона ATG: {start_codon_pos}")

