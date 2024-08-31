a = 'aabcccabbaaaacbbbbbba'

set_a = set(list(a))
dict_a =dict.fromkeys(set_a,0)
print(dict_a)
for x in a:
    dict_a[x]=dict_a[x]+1
print(dict_a)