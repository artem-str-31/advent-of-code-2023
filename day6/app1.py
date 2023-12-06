file_name = 'input.txt'
file = open(file_name, 'r')

lines = file.readlines()

time_line = lines[0]
distance_line = lines[1]

times = [int(x) for x in time_line.split(':')[1].split()]
distances = [int(x) for x in distance_line.split(':')[1].split()]
answers = []

for i in range(len(times)):
    answer = []
    for j in range(times[i]):
        speed = j
        time = times[i] - j
        distance = speed * time
        answer.append(distance)
    answers.append(len([x for x in answer if x > distances[i]]))

total = 1

for a in answers:
    total = total * a

print(total)
