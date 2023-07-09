def twoSum_bruteforce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #Loop over each element and while on each element, loop over all the following elements in the list. If their sum matches the target, we return the index.
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
    return None

def twoSum_list_ops(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #Loop over each element and define a new variable as the difference between the target and the current variable. Search for this variable in the remaining list, if it is present, retrieve the index for it and return the appropriate indexes
    for i,j in enumerate(nums):
            new = target - j
            if new in nums[i+1:]:
                return i, nums[i+1:].index(new)+i+1
    return None