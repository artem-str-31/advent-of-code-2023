file = open('input.txt', 'r')
total = 0
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

for line in file.readlines():    
    integers = []
    indexes = {}

    for number in numbers.keys():
        indexes[number] = list(find_all(line, number))
    
    indexes = {k: v for k, v in indexes.items() if v != []}
     
    for index in indexes:
        for value in indexes[index]:
            line_list = list(line)
            line_list[value] = str(numbers[index])
            line = "".join(line_list)

    for character in line:
        if character.isdigit():
            integers.append(int(character))
    
    total = total + (10 * integers[0] + integers[-1])

file.close()
print(total)
