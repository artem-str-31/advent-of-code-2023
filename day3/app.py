def left(l1):
    if l1[2].isdigit():
        if l1[1].isdigit():
            if l1[0].isdigit():
                return 100 * int(l1[0]) + 10 * int(l1[1]) + int(l1[2])
            else:
                return 10 * int(l1[1]) + int(l1[2])
        else:
            return int(l1[2])
    else:
        return 0


def right(l1):
    if l1[0].isdigit():
        if l1[1].isdigit():
            if l1[2].isdigit():
                return 100 * int(l1[0]) + 10 * int(l1[1]) + int(l1[2])
            else:
                return 10 * int(l1[0]) + int(l1[1])
        else:
            return int(l1[0])
    else:
        return 0


def center(l1):
    if l1[2].isdigit() and l1[4].isdigit():
        return 100 * int(l1[2]) + 10 * int(l1[3]) + int(l1[4])
    elif l1[2].isdigit():
        if l1[1].isdigit():
            return 100 * int(l1[1]) + 10 * int(l1[2]) + int(l1[3])
        else:
            return 10 * int(l1[2]) + int(l1[3])
    elif l1[4].isdigit():
        if l1[5].isdigit():
            return 100 * int(l1[3]) + 10 * int(l1[4]) + int(l1[5])
        else:
            return 10 * int(l1[3]) + int(l1[4])
    else:
        return int(l1[3])


file = open('input.txt', 'r')
symbols = []

for line in file.readlines():
    for char in line:
        if not char.isdigit() and char != '.' and char != '\n':
            symbols.append(char)

symbols_set = set(symbols)
file.close()


file = open('input.txt', 'r')
lines = file.readlines()
total = 0
total2 = 0


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in symbols_set:
            neighbours = [
                lines[i][j-3:j],
                lines[i][j+1:j+4],
                lines[i-1][j-3:j+4],
                lines[i+1][j-3:j+4]    
            ]
            
            neighbours[0] = left(neighbours[0])
            neighbours[1] = right(neighbours[1])

            if neighbours[2][3].isdigit():
                neighbours[2] = center(neighbours[2])
            else:
                temp1 = left(neighbours[2][0:3])
                temp2 = right(neighbours[2][4:7])
                neighbours[2] = 0
                neighbours.append(temp1)
                neighbours.append(temp2)

            if neighbours[3][3].isdigit():
                neighbours[3] = center(neighbours[3])
            else:
                temp1 = left(neighbours[3][0:3])
                temp2 = right(neighbours[3][4:7])
                neighbours[3] = 0
                neighbours.append(temp1)
                neighbours.append(temp2)
            
            neighbours = [neighbour for neighbour in neighbours if neighbour != 0]

            for neighbour in neighbours:
                total = total + neighbour

            if lines[i][j] == '*' and len(neighbours) == 2:
                total2 = total2 + neighbours[0] * neighbours[1]


print(total)
print(total2)

file.close()
