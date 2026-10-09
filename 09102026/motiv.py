#! /opt/homebrew/bin/python3
s = input()
t = input()
positions = []
for i in range(len(s)):
	if s[i:i+len(t)] == t:
		positions.append(str(i+1))
print(' '.join(positions))
