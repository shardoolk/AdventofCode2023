#Advent of Code Day1

import re
from collections import defaultdict
data = open("input_day1.txt")

lines = data.readlines()

counter = 0

for line in lines:
    regex = '\d'
    match = re.findall(regex,line)
    calibration_value = int(match[0])*10 + int(match[-1])
    match = []
    counter = counter + calibration_value
    calibration_value = 0
#    #print(match)

print(counter)

number_map = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

counter_real = 0
for line in lines:
    for key, value in number_map.items():
        line = line.replace(key,key+str(value)+key)
    regex = '\d'
    match = re.findall(regex,line)
    calibration_value1 = int(match[0])*10 + int(match[-1])
    #print(match)
    match = []
    counter_real = counter_real + calibration_value1
    calibration_value1 = 0
print(counter_real)