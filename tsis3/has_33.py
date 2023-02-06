def has_33(nums):
    for i in range(len(nums)):
        if nums[i] == 3:
            if nums[i+1] == 3 and i+1 <= len(nums)-1:
                return True

    return False
