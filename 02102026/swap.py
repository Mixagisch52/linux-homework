#!/opt/homebrew/bin/python3

a = int(input())
b = int(input())


print(f"До перестановки: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")


a, b = b, a
print(f"После 1 способа: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")


a, b = b, a 

temp = a
a = b
b = temp
print(f"После 2 способа: a = {a} (id: {id(a)}), b = {b} (id: {id(b)})")

