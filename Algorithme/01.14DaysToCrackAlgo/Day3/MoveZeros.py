"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""


def move_zeros(nums):
    last_non_zero_position = 0
    size = len(nums)
    for i in range(0, size):
        if nums[i] != 0:
            nums[last_non_zero_position] = nums[i]
            last_non_zero_position = last_non_zero_position + 1
    for j in range(last_non_zero_position, size):
        nums[j] = 0
    print(nums)


def main():
    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)


if __name__ == "__main__":
    main()
