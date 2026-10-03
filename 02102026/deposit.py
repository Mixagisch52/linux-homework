#!/opt/homebrew/bin/python3

import sys

amount = float(sys.argv[1])
rate = float(sys.argv[2])
years = int(sys.argv[3])

total = amount * (1 + rate / 100) ** years

print(f"{amount:.0f} {rate:.0f} {years} -> {total:.2f}")
