#### Day4 advent of code --- Day 4: Scratchcards ---

from collections import defaultdict
import math

data = open("input_day4.txt")
lines = data.readlines()

totalPoints = 0

for line in lines:
    gameNum, gameData = line.split(':')
    card_id = int(gameNum[5:])
    winnningCards, yourCards = gameData.split('|')
    winnningCards_list = list(map(int, winnningCards.split()))
    yourCards_list = list(map(int, yourCards.split()))
    common_elements = [i for i in yourCards_list if i in winnningCards_list]
    if len(common_elements) > 0:
        points = len(common_elements)-1
        totalPoints = totalPoints + 2**(points)
print("Part1 : ", totalPoints)

total_points = 0
scratchcard_points = {}
for idx, line in enumerate(lines):
    gameNum, gameData = line.split(':')
    card_id = int(gameNum[5:])
    winnningCards, yourCards = gameData.split('|')
    winnningCards_list = list(map(int, winnningCards.split()))
    yourCards_list = list(map(int, yourCards.split()))
    common_elements = [i for i in yourCards_list if i in winnningCards_list]
    points =  len(common_elements)
    scratchcard_points[idx+1] = [points,1]

for i in range(1,len(lines)+1):
    points,num = scratchcard_points[i]
    total_points += num
    for j in range(i+1, i+1+points):
        scratchcard_points[j][1] += num

print("Part2 : " ,total_points)