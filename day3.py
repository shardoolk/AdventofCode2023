### Day 3 Advent of code: Gear Ratios
from functools import reduce


data = open("input_day3.txt")
data = [list(line) for line in data.read().strip().split('\n')]

nrows = len(data)
ncols = len(data[0])


nums = []


### find all numbers, the line it is on and the start and end of the number 
for i in range(nrows):
    j = 0
    while j < ncols:
        if data[i][j].isdecimal():
            start = j
            num = ""
            while j < ncols and data[i][j].isdecimal():
                num += data[i][j]
                j  += 1
            # Adjust j to the last digit of the number    
            j -= 1
            nums.append((int(num), (i, start, j)))
        j += 1

## Part 1
sum = 0

for num in nums:
    num_flag = False
    for i in range(num[1][0]-1, num[1][0]+2):
        if i >=0 and i < nrows:
            for j in range(num[1][1] - 1, num[1][2]+2):
                if j >=0 and j < ncols:
                    if not(data[i][j].isdecimal() or data[i][j] == '.'):
                        num_flag=True
                        sum += num[0]
                        break 
        if num_flag:
            break 


print("Part 1 :  ",sum)


#### part 2

gears = {}

for num in nums:
    for i in range(num[1][0]-1, num[1][0]+2):
        if i >=0 and i <nrows:
            for j in range(num[1][1] - 1, num[1][2]+2):
                if j >=0 and j < ncols:
                    if data[i][j] == '*':
                        if not gears.get((i,j)):
                            gears[(i,j)] = []
                        gears[(i,j)].append(num[0])

gear_ratio = 0

for gear in gears:
    if len(gears[gear]) ==2:
        gear_ratio += reduce(lambda a,b : a*b, gears[gear])

#print(gears)
print("Part 2 : " ,gear_ratio)                                    
                                       