file_name = 'input.txt'
file = open(file_name, 'r')

total = 0
histories = []

for line in file.readlines():
    history = line.split()
    history = [int(x) for x in history]
    histories.append([history])


def is_constant_list(l1):
    for i in range(len(l1)-1):
        if l1[i] != l1[i+1]:
            return False
    return True


for history in histories:
    while not is_constant_list(history[-1]):
        new_difference = []
        for j in range(len(history[-1]) - 1):
            new_difference.append(history[-1][j+1] - history[-1][j])
        history.append(new_difference)


for history in histories:
    for i, difference in enumerate(history[::-1][1:]):
       value_to_add = difference[-1] + history[::-1][i][-1]
       difference.append(value_to_add)
    total = total + value_to_add


print(total)
file.close()
