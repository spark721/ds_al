
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def _perm(start):
            if start == len(nums) - 1:
                res.append(nums[:])
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                _perm(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        _perm(0)

        return res
