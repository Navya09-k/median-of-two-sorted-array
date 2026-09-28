class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find(x):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r)//2
                if nums[m] < x: l = m+1
                else: r = m
            return l
        a, b = find(target), find(target+1)
        return [a, b-1] if a < len(nums) and nums[a] == target else [-1, -1]