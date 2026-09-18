#!/opt/homebrew/bin/python3
a = input()
print('Sequence', a)
print('Length', len(a))
print('A', a.count('A'))
print('C', a.count('C'))
print('G', a.count('G'))
print('T', a.count('T'))
print('GC',((a.count('C')+a.count('G'))/len(a))*100)
