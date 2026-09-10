class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}

        # for i, x in enumerate(nums):
        #     complement = target - x
        #     if complement in seen:
        #         return [seen[complement],i]
        #     seen[x] = i
        # return []

        hm = {}
        for index, num in enumerate(nums):
            num_we_need = target - num
            if num_we_need in hm:
                return [hm[num_we_need],index]
            hm[num] = index
            