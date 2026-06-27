"""
Given an array and we verify if this array satisfies the preorder traversal of BST
We use here the monotonic stack to similate this sequence 
1. return false if the curr num is smaller than the min limit
2. the stack has to be non empty and 
the stack's first number has to be smaller than the current number (with [5,2,1,3,6], 
num=3 is the first occurence so we pop 1 then we pop 2) 

"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = float('-inf')
        stack = []

        for num in preorder:
            #print(f"\n--- Processing {num} ---")
            #print(f"Stack before: {stack}, min_limit: {min_limit}")
            while stack and stack[-1] < num:
                min_limit = stack.pop()
                #print(f"  Popped {min_limit}, moving right")
            if num <= min_limit:
                #print(f"  INVALID: {num} <= {min_limit}")
                return False
            stack.append(num)
            #print(f"Stack after: {stack}")
        return True