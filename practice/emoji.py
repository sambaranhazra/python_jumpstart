#!/usr/bin/python
for i in range(1, 11):
    s = ""
    s += " " * (10 - i)
    s += '\U0001f600' * i
    print(s)
