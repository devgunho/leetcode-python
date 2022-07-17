from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        for i in range(0, len(nums)):
            if i % 2 == 0:
                result += nums[i]
        return result


def run():
    obj = Solution()
    nums = [1, 4, 3, 2]
    print(obj.arrayPairSum(nums))


if __name__ == "__main__":
    run()
