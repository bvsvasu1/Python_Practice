from itertools import permutations

str_lst =[]
numbers =  [30,123,321,29,91]
numbers_str = list([str(i) for i in numbers])
combinations_str_lst = list(permutations(numbers_str,2))
print(combinations_str_lst)
for i in combinations_str_lst:
    if ((i[0][1] == i[1][0])):
        str_lst.append((int(i[0]), int(i[1])))
str_lst1 = str(str_lst)
print(len(str_lst),str_lst )