class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        def binary(mid):
            l, r = 0 , len(matrix[0]) - 1

            while l <= r:
                m = l + (r - l) // 2
                if target == matrix[mid][m]:
                    return True
                elif target > matrix[mid][m]:
                    l = m + 1
                else:
                    r = m - 1
            return False

        while top <= bottom:
            mid = top + (bottom - top)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return binary(mid)
        return False

