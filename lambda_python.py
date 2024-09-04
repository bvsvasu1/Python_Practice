n=5
x = lambda x: [x*x for x in range(1,n+1)]
print(*x(5),sep='\n')