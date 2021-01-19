class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        # print(nums)
        for i in range(0, len(nums)):
            # print(i, nums[i])
            if(i % 2 == 0):
                result += nums[i]
        return result
