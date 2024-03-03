import os

path = r'C:\PYTHON\LAB 5'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)