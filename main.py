def twoSum(nums: list[int], target: int) -> list[int]:
    check = 0
    oa = 0
    ob = 0
    while check != 1:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target :
                    oa = i
                    ob = j
		    check = 1
    return [oa, ob]


















