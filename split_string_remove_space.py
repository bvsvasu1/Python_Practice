one="john,lisa, teresa"
two = one.split(',')
print(two)
for i in range(len(two)):
    print(i)
    two[i]=two[i].strip()
print(two)

three = [x.strip() for x in one.split(',')]
print(three)