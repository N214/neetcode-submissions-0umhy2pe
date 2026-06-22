"""
approach:
since the rows are sorted and each row starts after the previous row ends, 
can treat the matrix as a flattened sorted array, 
binary search over indices from 0 to rows * cols - 1

S.C. O(1)
T.C. O(log(m*n))
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1

        while left <= right:
            mid = (left + right)//2
            # to locate the element in the matrix, we have to convert the flattened object back to an matrix
            row = mid // cols
            col = mid % cols
            if matrix[row][col] < target:
                left = mid+1
            elif matrix[row][col] > target:
                right = mid-1
            else:
                return True
        return False