#In the below code why dict_name, dict_name_count have same values?

marks= [78, 51, 32,55,81,59]
name= ['ABC','ABC','XYZ','ABC','Jack','Jack']

set_name = set(list(name))
dict_name = dict.fromkeys(set_name,0)
print(dict_name)
dict_name_count = dict_name.copy()
print(dict_name)

for x in range(len(name)):
    dict_name[name[x]] = marks[x]+dict_name[name[x]]
    dict_name_count[name[x]] = dict_name_count[name[x]]+1

print(dict_name, dict_name_count)