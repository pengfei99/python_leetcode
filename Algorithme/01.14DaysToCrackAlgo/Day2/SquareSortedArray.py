"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
import math
from typing import List


# the simplest solution is square the array, then sort it

def square_sort1(nums: List[int]) -> List[int]:
    res = []
    for item in nums:
        res.append(int(math.pow(item, 2)))
        res.sort()
    return res


# solution 2. We use two pointer to make it o(n)
def square_sort2(nums: List[int]) -> List[int]:
    mid = nums.index(0)
    res = [nums[mid]]
    left, right = mid - 1, mid + 1
    left_val = int(math.pow(nums[left], 2))
    right_val = int(math.pow(nums[right], 2))
    while (left >= 0) | (right < len(nums)):
        if left < 0:
            res.append(right_val)
            right = right + 1
        elif right >= len(nums):
            res.append(left_val)
            left = left - 1
        elif left_val >= right_val:
            res.append(left_val)
            left = left - 1
        else:
            res.append(right_val)
            right = right + 1
    return res


def square_sort3(nums):
    size = len(nums)
    left, right = 0, size - 1
    # in python we can't inert a element at position 4, if the list does not exist, or only has 2 element.
    # so we will create a list full of None that has the size of the origin
    res = [None] * size
    # note range include the beginning, not the end. e.g. rang(1,5)=1,2,3,4.
    # below range to include 0, we have to use -1 as the end.
    for i in range(size-1, -1, -1):
        print(i)
        left_val = int(math.pow(nums[left], 2))
        right_val = int(math.pow(nums[right], 2))
        if left_val >= right_val:
            res[i] = left_val
            left = left + 1
        else:
            res[i] = right_val
            right = right - 1
    return res


def main():
    nums = [-4, -1, 0, 3, 10]
    res1 = square_sort1(nums)
    print(f"result 1: {res1}")

    res2 = square_sort2(nums)
    print(f"result 2: {res2}")

    res3 = square_sort3(nums)
    print(f"result 3: {res3}")


if __name__ == "__main__":
    main()
