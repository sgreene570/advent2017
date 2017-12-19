# AOC day 18 challenge

import ast

def main():
    last = 0
    registers = {}
    for i in range(ord('a'), ord('z') + 1):
        registers[chr(i)] = 0
    f = open("input.txt", "r")
    lines = f.read().split("\n")
    i = 0
    while( i >= 0 and i < len(lines)):
        command = lines[i].split(" ")
        if command[0] == "snd":
            last = registers[command[1]]
        elif command[0] == "set":
            try:
                registers[command[1]] = int(command[2])
            except ValueError:
                registers[command[1]] = registers[command[2]]
        elif command[0] == "add":
            try:
                registers[command[1]] += int(command[2])
            except ValueError:
                registers[command[1]] += registers[command[2]]
        elif command[0] == "mul":
            try:
                registers[command[1]] *= int(command[2])
            except ValueError:
                registers[command[1]] *= registers[command[2]]
        elif command[0] == "mod":
            try:
                registers[command[1]] %= int(command[2])
            except ValueError:
                registers[command[1]] %= registers[command[2]]
        elif command[0] == "rcv" and registers[command[1]] != 0:
            print("Recovering, last played")
            print(last)
        elif command[0] == "jgz":
            try:
                t = int(command[1])
                if t > 0:
                    i += (int(command[2]))
                    continue
                else:
                    break
            except ValueError:
                if registers[command[1]] > 0:
                    i += (int(command[2]))
                    continue

        i += 1


if __name__ == "__main__":
    main()
