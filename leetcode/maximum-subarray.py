nums = [5,4,-1,7,8]

#Solution 1
max_sum = min(nums)
if len(nums)==1:
    print(nums[0])
elif len(nums)==0:
    print(0)
else:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i<j:
                temp_sum = sum(nums[i:j+1])
                #print("sum",sum(nums[i:j]),i,j)
            elif j>i:
                temp_sum = sum(nums[j:i-1])
            elif i==j:
                #print("sumsum",sum(nums[i:j]),i,j)
                temp_sum = nums[i]
            #print(max_sum, temp_sum,i,j)
            max_sum = temp_sum if max_sum<temp_sum else max_sum
    print(max_sum)


#Solution 2
import math

temp_max = -math.inf
max_sum = -math.inf
for i in nums:
    temp_max = max(temp_max+i, i)
    max_sum = max(temp_max, max_sum)
print(max_sum)