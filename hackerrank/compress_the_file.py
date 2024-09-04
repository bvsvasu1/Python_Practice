# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
#Sample Input
# 1222311
# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)



#SOLUTION 1

single_line = input()
output = []
temp =''
count=1
for i in range(len(single_line)):
    if not temp:
        temp=single_line[i]
        if i==(len(single_line)-1):
            output.append((count,int(temp)))
    else:
        if temp==single_line[i]:
            count+=1
            if i==(len(single_line)-1):
                output.append((count,int(temp)))
        elif temp!=single_line[i]:
            output.append((count,int(temp)))
            temp=single_line[i]
            count=1
            if i==(len(single_line)-1):
                output.append((count,int(temp)))
                
print(' '.join(str(x) for x in output))


# SOLUTION 2
from itertools import groupby

s = input()
for key, group in groupby(s):
    res = (len(list(group)),int(key))
    print(res,"",end="")