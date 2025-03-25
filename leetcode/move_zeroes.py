nums = [4,2,4,0,0,3,0,5,1,0]
nums1 = [4,2,4,0,0,3,0,5,1,0]
#solution 1
for i in nums1:
    #print(i,nums)
    if i==0:
        nums1.remove(i)
        nums1.append(0)
print(nums1)

#solution 2

def moveZeroes(nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=1
        while r<len(nums):
            print(l,r,nums, nums[r])
            if (nums[l]==0 and nums[r]!=0):
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l+=1
                r+=1
            elif (nums[l]!=0 and nums[r]==0):
                l+=1
                r+=1
            elif (nums[l]!=0 and nums[r]!=0):
                 l+=1
                 r+=1
            else:
                r+=1
        return nums
print(moveZeroes(nums))
print([4,2,4,3,5,1,0,0,0,0])


#solution 3:

def moveZeroes(self, nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums)==2:
        if nums[0]==0 and nums[1]!=0:
            nums[0]=nums[1]
            nums[1]=0
    elif len(nums)>2:
        indices = [i for i,x in enumerate(nums) if x==0]
        count = 0
        for i in indices:
            nums.pop(i-count)
            nums.append(0)
            count +=1