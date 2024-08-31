a='srinivas'
#solution 1
a_list = list(a)
set_a = set(a_list)
print(set_a)

#solution 2
set_b = set()
for x in a:
    set_b.add(x)
print(set_b)