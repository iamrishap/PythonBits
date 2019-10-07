'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_dict = {}
        self.n = len(nums)
        for i in range(self.n):
            self.sum_dict[(i, i)] = nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            return
        if (i, j) not in self.sum_dict:
            if i + 1 < self.n and (i + 1, j) in self.sum_dict:
                self.sum_dict[(i, j)] = self.sum_dict[(i + 1, j)] + self.nums[i]
            elif j - 1 >= 0 and (i, j - 1) in self.sum_dict:
                self.sum_dict[(i, j)] = self.sum_dict[(i, j - 1)] + self.nums[j]
            elif i + 1 < self.n:
                self.sum_dict[(i, j)] = self.sumRange(i + 1, j) + self.nums[i]
            elif j - 1 >= 0:
                self.sum_dict[(i, j)] = self.sumRange(i, j - 1) + self.nums[j]
        return self.sum_dict[(i, j)]


# Your NumArray object will be instantiated and called as such:
nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
obj = NumArray(nums)
param_1 = obj.sumRange(2, 8)
param_2 = obj.sumRange(0, 3)
param_3 = obj.sumRange(5, 9)
param_4 = obj.sumRange(5, 5)
param_5 = obj.sumRange(-1, -1)
param_6 = obj.sumRange(0, 9)
print(param_1, param_2, param_3, param_4, param_5, param_6)
