def twoSum(nums: list[int], target: int):
    indexed_nums = list(enumerate(nums))
    indexed_nums.sort(key=lambda x: x[1])
    
    left = 0
    right = len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][1] + indexed_nums[right][1]
        
        if current_sum == target:
            return [indexed_nums[left][0], indexed_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    # If no solution is found, which should not h        
nums = [2,7,11,15]
print(twoSum(nums,9))

nums = [3,2,4]
print(twoSum(nums,6))