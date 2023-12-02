available_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

input = open('input.txt', 'r')
total = 0
total2 = 0

for line in input.readlines():
    
    colon_split = line.split(':')

    id = colon_split[0].split()[1]

    semicolon_split = colon_split[1].split(';')
    
    max_cubes = {}

    for subgame in semicolon_split:
        subsubgame = subgame.split(',')
        for subsubsubgame in subsubgame:
            x = subsubsubgame.split()
            max_cubes[x[1]] = max(max_cubes.get(x[1], 0), int(x[0]))

    playable = True
    min_num = 1

    for color in max_cubes.keys():
        playable = playable and (max_cubes[color] <= available_cubes[color])
        min_num = min_num * max_cubes[color]

    if playable:
        total = total + int(id)

    total2 = total2 + min_num
    
print(total)
print(total2)
input.close()
