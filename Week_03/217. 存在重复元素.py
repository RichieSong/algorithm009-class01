# -*- coding: utf-8 -*-
"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

1、统计
2、指针
"""
from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """统计"""
        if not nums: return False
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count.get(i, 0) > 1:
                return True
        return False

    def containsDuplicate1(self, nums: List[int]) -> bool:
        """指针"""
        if not nums: return False
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                return True
            i += 1
        return False
