#Advent of Code 2023 Day 2: Cubes
from collections import defaultdict
import math

data = open("input_day2.txt")
lines = data.readlines()

max_cubes = {"red": 12, "green": 13, "blue": 14};

games_list = []
for line in lines:
    game,gameData = line.split(': ')
    game_id = int(game[5:])
    gameRounds = gameData.split(';')
    rounds_list = []
    game_Dict = defaultdict(int)
    for round in gameRounds:
        draws = round.split(',')
        draws_list = []
        for draw in draws:
            num,color = draw.strip().split(' ')
            game_Dict[color] =  max(game_Dict[color], int(num))
            draws_list.append(int(num) <= max_cubes[color])
        rounds_list.append(all(draws_list))
    games_list.append((game_id, all(rounds_list),game_Dict.values()))



##part 1
print(sum((id for id, result,minimum_cubes in games_list if result)))
#print(games_list)
##part 2
print(sum((math.prod(min_cubes) for id, result, min_cubes in games_list)))
