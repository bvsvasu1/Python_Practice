import math

def findOptimalResources(arr, k):
    #Solution 1
    # temp_sum = -math.inf
    # max_sum = -math.inf
    # for i in range(len(arr)-k+1):
    #     temp_list = []
    #     for j in range(i,i+k):
    #         if arr[j] not in temp_list:
    #             temp_list.append(arr[j])
    #     #print(temp_list)
    #     if len(temp_list)==k:
    #         temp_sum = max(temp_sum, sum(arr[i:i+k]))
    #         max_sum = max(temp_sum,max_sum)
    # return max_sum if max_sum>-math.inf else -1
    
    # Solution 2
    # temp_sum = -math.inf
    # max_sum = -math.inf
    # for i in range(len(arr)-k+1):
    #     len_check = len(set(arr[i:i+k]))
    #     if len_check!=k:
    #         temp_sum = -1
    #     else:
    #         temp_sum = max(temp_sum, sum(arr[i:i+k]))
    #         max_sum = max(temp_sum,max_sum)
    # return max_sum if max_sum>-math.inf else -1

    #solution 3
    
    import math
    def maximumSubarraySum(nums: list[int], k: int):
        temp_max = 0
        max_sum = 0
        l = 0
        r = 0
        k_list = []
        while r<len(nums):
            #print(l,r,nums[r],temp_max,max_sum,k_list,k)
            if r-l<k:
                if nums[r] not in k_list:
                    k_list.append(nums[r])
                    temp_max += nums[r]
                    r+=1
                else:
                    k_list = []
                    temp_max = 0
                    l+=1
                    r=l
                if r-l==k:
                    max_sum = max(temp_max, max_sum)
                    temp_max = 0
                    l+=1
                    r=l
                    k_list = []
            else:
                pass
        return max_sum