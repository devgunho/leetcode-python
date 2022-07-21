from typing import List


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        base = 1
        big = 0
        result = 0

        if a > b:
            base = b
            big = a
        else:
            base = a
            big = b

        for i in range(1, base + 1):
            if (big % i == 0) and (base % i == 0):
                result += 1

        return result


def run():
    obj = Solution()
    na = 12
    nb = 6

    print(obj.commonFactors(a=na, b=nb))


if __name__ == "__main__":
    run()
