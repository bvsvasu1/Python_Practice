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

# a = {'a':1}
# b = a.copy()
# b['a']+=1
# print(a,b)

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


# a =['a','b','c','d']
# # res = []
# # for i in range(len(a)-1,-1,-1):
# #     res.append(a[i])
# # print(res)

# print([a[i] for i in range(len(a)-1,-1,-1) ])

# test_cases = int(input())
# for i in range(2):
#     len_a = int(input())
#     str_a = input().split(' ')
#     str_b = input().split(' ')
#     dict_elem = {}
#     short = -1
#     long_l = -1
#     for i in range(len_a):
#         if str_a[i]!=str_b[i]:
#             if short ==-1:
#                 short = i+1
#             else:
#                 long_l = i+1
#         if i==len_a-1:
#             print(long_l-short+1)

# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2!=0:
#         print("Weird1")
#     elif (n%2==0 and 2<=n<=5):
#         print("Not Weird2")
#     elif (n%2==0 and (6<=n<=20)):
#         print("Weird3")
#     else:
#         print("Not Weird4")

# n=5
# x = [str(i) for i in range(1,n+1)]
# print(x)

# from itertools import groupby

# a = 'aaaabbbbbcccccc'
# print(a)
# for k,g in groupby(a):
#     print(k, len(list(g)))

# from itertools import combinations
# from functools import reduce

# _ = 9
# elts = "a b c a d b z e o".split()
# k = 4

# cs = combinations(elts, k)
# (hits, total) = reduce(lambda a,x: (a[0]+1, a[1]+1) if 'a' in x else (a[0],a[1]+1), cs, (0,0))
# print(hits/total)

# K,M = map(int, input().split())

# list_i = []
# list_max = []
# for i in range(K):
#     list_i.append([int(x) for x in input().split()])

# for i in list_i:
#     print(max(i))
#     list_max.append(pow(max(i),2))

# print(list_max)
# print(sum(list_max))
# res = sum(list_max)%M
# print(res)

# from itertools import product

# k, modulo = 7,867

# lst = [[val**2 for val in map(int,input().split()[1:]) ] for _ in range(int(k))]
# half = len(lst) // 2
# lists1 = lst[:half]
# lists2 = lst[half:]

# print(lists1)
# print(lists2)
# res = 0
# print(list(product(*lst)))
# for i in product(*lst):
#     x = sum(i)%int(modulo)
#     res = max(x,res)
# print(res)



from itertools import product

def maximize_it(k, M, sets):
    # Generate all possible combinations using the Cartesian product
    max_value = 0
    for combination in product(*sets):
        # Calculate the sum of squares of the selected numbers
        current_sum_of_squares = sum(x ** 2 for x in combination) % M
        if current_sum_of_squares > max_value:
            max_value = current_sum_of_squares
    return max_value
    
    
if __name__ == "__main__":    
    k, M = map(int, input().split())
    sets = []
    for _ in range(k):
        # Read the entire line and convert it into a list of integers
        sets.append(list(map(int, input().split())))
    
    result = maximize_it(k, M, sets)
    print(result)