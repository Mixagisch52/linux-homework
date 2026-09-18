#!/opt/homebrew/bin/python3

import sys 

if len(sys.argv) < 3:
	print('error, give 2 numbers')
a = float(sys.argv[1])
b = float(sys.argv[2])

summ = a + b 
razn = a - b 
proizv = a * b 
print('Сумма', summ)
print('Разность', razn)
print('Произведение', proizv)



