data = open('input_day6.txt')
lines = data.readlines()

time = [int(a) for a in lines[0].split(':')[1].split()]
distance = [int(a) for a in lines[1].split(':')[1].split()]
time2 = ''.join([a for a in lines[0].split(':')[1].split()])
distance2 = ''.join([a for a in lines[1].split(':')[1].split()])

time.append(int(time2))
distance.append(int(distance2))

instances = []
prod = 1
for i in range(len(time)):
    count = 0
    for j in range(time[i]):
        dist = j*(time[i] - j)
        if dist > distance[i]:
            count = count + 1
    instances.append(count)
    prod = prod*count

print(instances)
print("The answer for part 1 is :", prod/instances[-1])
print("The answer for part 2 is ", instances[-1])


        