with open('input.txt', 'r') as file:
    n = len(file.readlines())
    powers = [0 for _ in range(n)]
    copies = [1 for _ in range(n)]

with open('input.txt', 'r') as file:
    for line in file.readlines():
        id = int(line.split(':')[0].split()[1])
        game = line.split(':')[1].split('|')
        winning = game[0].split()
        given = game[1].split()
    
        power = 0
        index = id - 1

        for element in given:
            if element in winning:
                power = power + 1

        if power > 0:
            powers[index] = 2 ** (power-1)
    
        for i in range(index+1, min(index+power+1, len(copies))):
            copies[i] = copies[i] + 1 * copies[index] 

print(sum(powers))
print(sum(copies))
