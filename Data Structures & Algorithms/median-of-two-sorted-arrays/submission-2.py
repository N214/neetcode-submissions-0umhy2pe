class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # swap the array if len(A) > len(B) so A is always the shorter array
        if len(B) < len(A):
            A, B = B, A
        
        # run binary search on A
        l, r = 0, len(A) - 1

        while True:
            mid = (l + r) // 2
            midB = half - mid - 2 # index of mid in B, dont forget to do -2 because both A and B start at 0

            Aleft = A[mid] if mid >= 0 else float("-inf")
            Aright = A[mid+1] if (mid + 1) < len(A) else float("inf")
            Bleft = B[midB] if midB >= 0 else float("-inf")
            Bright = B[midB+1] if (midB + 1) < len(B) else float("inf")

            # partition correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd 
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # too many element from A
                r = mid - 1
            else:
                l = mid + 1