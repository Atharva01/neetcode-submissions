class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_r = [i for i in range(len(nums)+1)]
        num_r = set(num_r)
        nums = set(nums)
        print(num_r)
        print(nums)
        missing =  num_r - nums
        return int(next(iter(missing)))