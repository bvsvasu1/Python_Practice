# Implement in python:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


def two_sum(nums, target):
    # Dictionary to store the indices of elements
    index_map = {}
    
    # Traverse the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in index_map:
            # Return the indices of the two numbers that add up to the target
            return [index_map[complement], i]
        
        # Add the current number and its index to the dictionary
        index_map[num] = i

    # If no solution is found, which should not happen according to the problem statement
    raise ValueError("No two sum solution")

nums = [1,2,3,4,6,90,150,1000]
target = 240
print(two_sum(nums, target))



def two_sum_two_pointers(nums, target):
    # Pair each number with its index and sort the list based on the number
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
    
    # If no solution is found, which should not happen according to the problem statement
    raise ValueError("No two sum solution")

# Example usage
print(two_sum_two_pointers([2, 7, 11, 15], 18))  # Output: [0, 1]
# print(two_sum_two_pointers([3, 2, 4], 6))       # Output: [1, 2]
# print(two_sum_two_pointers([3, 3], 6))          # Output: [0, 1]
