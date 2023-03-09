
def twoSum(nums: list[int], target: int) -> list[int]:
    a = nums[0]
    check = 0
    i = 0
    j = 0
    oa = 0
    ob = 0
    while check != 1 :
        if i + 1 >= len(nums):
            break
        if nums[j] + nums[i + 1] == target:
            oa = j
            ob = i + 1
            check = 1
        else :
            j = j + 1
            i = i + 1
    return [oa, ob]
