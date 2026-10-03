#!/opt/homebrew/bin/python3

import sys


num_str = sys.argv[1]
num = int(num_str)

b = bin(num)
o = oct(num)
h = hex(num)

print(f"{num} -> {b} {o} {h}")

back_from_bin = int(b, 2)
back_from_oct = int(o, 8)
back_from_hex = int(h, 16)

print(f"Обратно: {back_from_bin}, {back_from_oct}, {back_from_hex}")

