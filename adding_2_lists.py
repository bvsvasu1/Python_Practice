a =[0,3,4,30]
b =[4,6,31]

final_list = []
i = 0
j = 0
total_length = len(a)+len(b)

a_temp = a[0]
b_temp = b[0]

while True:
    print("i,j",i,j)
    if i<len(a):
        a_temp = a[i]
    else:
        pass

    if j<len(b):
        b_temp = b[j]
    else:
        pass
    
    print("temp",a_temp,b_temp)

    if (a_temp<b_temp and (i<len(a))):
        final_list.append(a_temp)
        i+=1
    elif a_temp==b_temp:
        final_list.append(a_temp)
        final_list.append(b_temp)
        i+=1
        j+=1
    elif (a_temp>b_temp and j<len(b)):
        final_list.append(b_temp)
        j+=1
    elif(a_temp<b_temp and (i>=len(a))):
        final_list.append(b_temp)
        j+=1
    elif (a_temp>b_temp and j<len(b)):
        final_list.append(b_temp)
        i+=1
    else:
        pass

    if i>=len(a) and j>=len(b):
        break
    
    print(i,j,final_list)

print(final_list)