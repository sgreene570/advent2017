#!/usr/bin/python
# Why store values you don't need to check!
skip_size = 345 # This will change per use

spin = [0, 1]
mark = 1
length = len(spin)
for i in range(2, 50000000):
    mark = ((mark + skip_size) % length) + 1
    if mark == (spin.index(0) + 1):
        spin[spin.index(0) + 1] = i
    length += 1

print(spin)
