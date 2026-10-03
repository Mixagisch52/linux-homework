#!/opt/homebrew/bin/python3

a = input()
summ = 0 
for i in a:
	summ += int(i)

reverse_num = a[::-1]

print(f'{summ}, {reverse_num}')
