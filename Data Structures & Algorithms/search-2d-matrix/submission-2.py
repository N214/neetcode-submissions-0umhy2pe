class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [1,2,4,8,10,11,12,13,14,20,30,40]
        l, r = 0, (len(matrix[0]) * len(matrix)) -1

        while l <= r:
            # (0+11)//2 = 5
            mid = (l+r)//2
            # 5//4 = 1
            row = mid // len(matrix[0])
            # 5%4 = 1
            # matrix[1][1] = 11
            col = mid % len(matrix[0])
            if target > matrix[row][col]:
                l = mid+1
            elif target < matrix[row][col]:
                r = mid-1
            else:
                return True
        return False