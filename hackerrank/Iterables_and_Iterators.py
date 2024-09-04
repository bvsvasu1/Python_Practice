#solution 1
import itertools

input_length = 9
input_str = "a b c a d b z e o"
input_lst = input_str.split(' ')
indices = 4

combination = list(itertools.combinations(input_lst,indices))
count = 0
for i in combination:
    if 'a' in i:
        count+=1
#print(len(combination))
print(f"{count/len(combination):.3f}")


#solution 2
from itertools import combinations
from functools import reduce

_ = 9
elts = "a b c a d b z e o".split()
k = 4

cs = combinations(elts, k)
(hits, total) = reduce(lambda a,x: (a[0]+1, a[1]+1) if 'a' in x else (a[0],a[1]+1), cs, (0,0))
print(hits/total)