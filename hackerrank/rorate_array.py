def rotate(nums: list[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums==2:
            if k%2==1:
                rem_len=1
            else:
                rem_len=0
        else:
            rem_len = len_nums-k 
        nums1 = nums[rem_len:len_nums]
        nums2 = nums[0:rem_len]
        print(rem_len,nums1+nums2,nums[rem_len:len_nums],nums[0:rem_len])
        nums[:] = nums[rem_len:len_nums] + nums[0:rem_len]

nums = [1,2,3,4,5,6,7]
k=5
print(rotate(nums,k))
