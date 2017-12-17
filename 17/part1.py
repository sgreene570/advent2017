#!/usr/bin/python
# Easy enough when dealing with a small # of values

skip_size = 345 # This is the number that AOC RNGs per user
spin = [0, 1]
mark = 1
for i in range(2, 2018):
    mark = ((mark + skip_size) % len(spin)) + 1
    spin.insert(mark, i)

print(spin[spin.index(2017) + 1])

