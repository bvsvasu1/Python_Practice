# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     print(total_value,value)
#     print(f"That is {(value/total_value)*100}")
# except Exception as e:
#     print(e,ValueError)
#     raise e

# except ValueError as e:
#     if e==ValueError:
#         print("You need to enter a number. Run the program again.")

# total_value = float(input("Enter total value: "))
# value = float(input("Enter value: "))
# print(total_value,value)
# print(f"That is {(value/total_value)*100}")

# a = [1,2,3]
# b = a
# a.insert(0,5)
# print(a,b)



# a = {'b':[1,2,3]}
# b = a.copy()
# print("post copy")
# print(a,b)
# b['b'][0]=2
# print(b['b'][0])
# print(a,b)
# # {'b': [2, 2, 3]} {'b': [2, 2, 3]}

a = {'a':1}
b = a.copy()
b['a']+=1
print(a,b)

# print("only b was changed")
# print(a,b)
# print("only a was changed")
# a = {'b':[1,2,3]}
# b = a.copy()
# a['b']=5
# print(a,b)
# a = {'b':[1,2,3]}
# b = a.copy()
# a['c']=55
# print("only a was changed with a new key")
# print(a,b)