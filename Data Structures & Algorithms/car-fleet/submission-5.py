class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p,s in cars:
            time = (target - p)/s
            # Skip cars with the same speed or faster
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)