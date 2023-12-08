import math

file_name = 'input.txt'
file = open(file_name, 'r')
content = file.read()

instructions, network = content.strip().split('\n\n')
network = network.split('\n')
nodes = {}

for i, node in enumerate(network):
    for j in node:
        if j in ['=', ',', '(', ')']:
            network[i] = network[i].replace(j, ' ')
    network[i] = tuple(network[i].split())
    nodes[network[i][0]] = (network[i][1], network[i][2])


current_nodes = []
count = 0

for key in nodes.keys():
    if key[2] == 'A':
        current_nodes.append(key)

n = len(current_nodes)
numbers = [0 for i in range(n)]


for i, current_node in enumerate(current_nodes):
    count = 0

    while current_nodes[i][2] != 'Z':
        if instructions[count % len(instructions)] == 'L':
            current_nodes[i] = nodes[current_nodes[i]][0]
        else:
            current_nodes[i] = nodes[current_nodes[i]][1]
        count += 1

    numbers[i] = count


lcm = 1
for number in numbers:
    lcm = lcm * number // math.gcd(lcm, number)

print(lcm)
