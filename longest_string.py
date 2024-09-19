# find a the letter which comes maximum times in a consecutive sequence : 
# aabcccabbaaaacbbbbbba

input_string = "aabcccabbaaaacbbbbbba"
j=0
k=1
count = 0
temp_count = 0
max_string = []
temp_max_string = []
while k<len(input_string):
    if not temp_max_string:
        temp_max_string.append(input_string[j])
        temp_count+=1
    if input_string[j]==input_string[k]:
        temp_count+=1
        temp_max_string.append(input_string[k])
        k+=1
        if temp_count>count:
            count = temp_count
            max_string = temp_max_string
    else:
        j=k
        k=j+1
        temp_count = 0
        temp_max_string = []
print(max_string)
long_str = "".join(max_string)
print(long_str)