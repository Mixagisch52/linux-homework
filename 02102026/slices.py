#!/opt/homebrew/bin/python3

s = input()

length = len(s)

first_char = s[0]
last_char = s[-1]


middle_char = s[len(s) // 2]


every_second = s[::2]


reversed_s = s[::-1]


is_palindrome = (s == reversed_s)


print(f"Длина: {length}")
print(f"Первый: {first_char}, Последний: {last_char}, Средний: {middle_char}")
print(f"Каждый второй: {every_second}")
print(f"Наоборот: {reversed_s}")
print(f"Палиндром ли: {is_palindrome}")

