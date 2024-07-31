student_list = [5,3,2,2,3,5,4,6,9,6,4,12,8,9,12]
list1 = student_list
remainder = []
dict1 = {}
for n in list1:
    dict1[n] = len([i for i,val in enumerate(list1) if val==n])
print(dict1)
for k,v in dict1.items():
    if v==1:
        remainder.append(k)
print(remainder[0])