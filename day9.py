#### day 8 advent of code: Mirage Management
### Part 1 by brute force and part2 using function def and zip 

data = open('input_day9.txt')
#data = open('day9_test.txt')
lines = data.readlines()
p1 = 0
p2 = 0

def extrapolate(seq):
    if all(x==0 for x in seq):
        return 0
    delta_seq = [y-x for x, y in zip(seq, seq[1:])]
    diff = extrapolate(delta_seq) 
    return seq[0]  - diff
    ### return seq[-1]+ diff for part 1



for line in lines:
    seq = [int(num) for num in line.split()]
    seq_list = [seq]
    p2 += extrapolate(seq)
    while not all(x==0 for x in seq):
        diff_seq = [seq[i+1] -  seq[i] for i in range(len(seq) - 1)]
        seq_list.append(diff_seq)
        seq = diff_seq
   
    for list in seq_list:
        p1 += list[-1]
        

print("Part 1 solution: ", p1)
print("Part 2 solution:  ", p2)