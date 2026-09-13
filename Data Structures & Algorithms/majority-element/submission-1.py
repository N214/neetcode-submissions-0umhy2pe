class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Voting Algorithm
        # Key insight: If we "cancel out" each majority element with a non-majority element,
        # the majority element will always remain since it appears > n/2 times
        
        res = 0      # Candidate for majority element
        count = 0    # Balance counter: tracks (candidate count - others count)
        
        for num in nums:
            # When count reaches 0, reset candidate to current number
            # This works because the majority element will survive all cancellations
            if count == 0:
                res = num
            
            # Increment count if current number matches candidate
            # Decrement count if it doesn't (simulating cancellation)
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res