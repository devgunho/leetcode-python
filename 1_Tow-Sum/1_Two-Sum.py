from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
        return result


def run():
    obj = Solution()
    nums = [3, 3]
    print(obj.twoSum(nums))


if __name__ == "__main__":
    run()
