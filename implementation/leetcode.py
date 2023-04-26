class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            i = 1
            while True:
                if i * i > x:
                    return i - 1
                i += 1


if __name__ == "__main__":
    print(Solution().mySqrt(8))
