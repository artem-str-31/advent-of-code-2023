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

current = 'AAA'
count = 0

while current != 'ZZZ':
    if instructions[count % len(instructions)] == 'L':
        current = nodes[current][0]
    else:
        current = nodes[current][1]
    count += 1

print(count)
