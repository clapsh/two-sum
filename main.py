def twoSum (nums, target):
    res = list()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            sum = nums[i]+nums[j]
            if sum == target:
                res = [i,j]
    return res
