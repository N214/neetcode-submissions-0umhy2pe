class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) -1
        boat = 0
        # here they can be equal to each other
        while l <= r:
            remain = limit - people[r]
            r -=1
            boat += 1
            if l <= r and remain >= people[l]:
                l +=1
            
        return boat