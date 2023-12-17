file_name = 'input.txt'
file = open(file_name, 'r')


for line in file.readlines():
    hash = line.split()[0].split('.')
    hash = [x for x in hash if x != ""]
    numbers = line.split()[1].split(',')
    numbers = [int(x) for x in numbers]
    hash = [x for x in hash if len(x) >= min(numbers)]
    print(hash, numbers)



if len(hash) < len(numbers):
    pass
elif len(hash) > len(numbers):
    pass
else:
    pass





file.close()
