# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]

def solution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums


print(solution(array1))
print(solution(array2))


def solution_2(nums: list):
    zeros = nums.count(0)
    filtered = list(filter(bool, nums))
    # return filtered + [0 for _ in range(zeros)]
    return filtered + [0] * zeros


print(solution_2(array1))
print(solution_2(array2))
