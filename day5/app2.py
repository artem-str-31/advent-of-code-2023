input_file_name = 'input.txt'
file = open(input_file_name, 'r')
content = file.read()

categories = [[[int(num) for num in line.split()] for line in map_block.split('\n')] for map_block in [map_item.split(':')[1].strip() for map_item in content.split('\n\n')]]
seeds_ranges = [[categories[0][0][2*n], categories[0][0][2*n] + categories[0][0][2*n+1] - 1] for n in range(len(categories[0][0])//2)]
categories_maps = categories[1:]


print(seeds_ranges)
for category_maps in categories_maps:
    print(category_maps)


for category_maps in categories_maps:
    for map in category_maps:
        i = 0
        while i < len(seeds_ranges):
            print(i)

            seed_start, seed_end = seeds_ranges[i]
            map_start, map_end, map_length = map[0], map[1], map[2]
            updated = False

            if map_end <= seed_start < map_end + map_length and not updated:
                print('start: ', seeds_ranges[i])
                
                updated = True
                seeds_ranges[i][0] = map_start + seed_start - map_end
                if seed_end < map_end + map_length:
                    seeds_ranges[i][1] = map_start + seed_end - map_end
                else:
                    seeds_ranges[i][1] = map_start + map_length - 1
                    seeds_ranges.append([map_end + map_length, seed_end])
           
                print('end: ', seeds_ranges[i])
            
            elif map_end <= seed_end < map_end + map_length and not updated:
                print('start: ', seeds_ranges[i])
                
                updated = True
                seeds_ranges[i][1] = map_start + seed_end - map_end
                if seed_start > map_end:
                    seeds_ranges[i][0] = map_start + seed_start - map_end
                else:
                    seeds_ranges[i][0] = map_start
                    seeds_ranges.append([seed_start, map_end - 1])
                
                print('end: ', seeds_ranges[i])

            i = i + 1
            print('\n')
                


print(min([min(seed) for seed in seeds_ranges]))

file.close()
