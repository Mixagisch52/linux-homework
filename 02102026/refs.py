#!/opt/homebrew/bin/python3

import sys


a = sys.argv[1:]


b = a


c = a[:]


print(f"b является тем же объектом, что и a? {b is a} (id(a): {id(a)}, id(b): {id(b)})")
print(f"c является тем же объектом, что и a? {c is a} (id(a): {id(a)}, id(c): {id(c)})")


a[0] = "ИЗМЕНЕНО"


print(f"Список a: {a}")
print(f"Список b (изменился вместе с a): {b}")
print(f"Список c (остался независимым): {c}")


