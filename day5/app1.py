input_file_name = 'input.txt'
file = open(input_file_name, 'r')
content = file.read()

categories = [[[int(num) for num in line.split()] for line in map_block.split('\n')] for map_block in [map_item.split(':')[1].strip() for map_item in content.split('\n\n')]]
seeds = categories[0][0]
categories_maps = categories[1:]

print('Seeds: ', seeds)
print('Maps:')
for category_maps in categories_maps:
    print(category_maps)
print('\n\n\n')

for i in range(len(seeds)):
    for category_maps in categories_maps:
        for map in category_maps:
            if seeds[i] in range(map[1], map[1] + map[2] + 1):
                print('Old value of seed: ', seeds[i])
                print(seeds[i], ' is in range (', map[1], ', ', map[1] + map[2], ')')
                print(map)
                seeds[i] = map[0] + seeds[i] - map[1]
                print('New value of seed: ', seeds[i])
                break
    print('\n')


print(seeds)
print(min(seeds))
file.close()
