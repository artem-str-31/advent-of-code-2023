file_name = 'input.txt'
file = open(file_name, 'r')

lines = file.readlines()

time_line = lines[0]
distance_line = lines[1]

times = int(time_line.split(':')[1].replace(' ', ''))
distances = int(distance_line.split(':')[1].replace(' ', ''))
start = 0
end = 0

for i in range(times):
    speed = i
    time = times - i
    distance = speed * time
    if distance > distances:
        start = i
        break

for i in range(times, -1, -1):
    speed = i
    time = times - i
    distance = speed * time
    if distance > distances:
        end = i
        break

print(end - start + 1)
file.close()
