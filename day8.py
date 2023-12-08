#### Day 8 Advent of Code   Haunted Wasteland ---
import re
from math import lcm

steps, data = open("input_day8.txt").read().split('\n\n')
data = data.split('\n')
num_steps = 0

current_point = 'AAA'
end_point = 'ZZZ'


data_network = {}
pattern = r'\b[A-Z]+\b'
for line in data:
    pos, instA, instB = re.findall(pattern, line)
    data_network[pos] = [instA,instB]

#print(data_network)

while current_point != end_point:
    num_steps = num_steps+1
    current_point = data_network[current_point][0 if steps[0] =='L' else 1]
    steps = steps[1:] + steps[0]
    
print(num_steps)    
        
        
#part2

posEndsA = [key for key in data_network if key.endswith('A')]

cycles = []

for current in posEndsA:
    cycle = []
    current_steps = steps
    step_count=0
    
    first_z = None
    
    while True:
        while step_count==0 or not current.endswith('Z'):
            step_count += 1
            current = data_network[current][0 if current_steps[0] == 'L' else 1]
            current_steps = current_steps[1:] + current_steps[0]
        
        cycle.append(step_count)
        
        if first_z is None:
            first_z = current
            step_count = 0
        elif current == first_z:
            break
        
        cycles.append(cycle)
        
print(cycles)
num = [cycle[0] for cycle in cycles]

lcm_result = num[0]
for n in num:
    lcm_result = lcm(lcm_result,n)
print(lcm_result)