class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        # target - position / speed = time
        #12-10/2=1
        #4/4=1
        #12/1=12
        #7/1=7
        # 9/3=3
        stack = []
        for p,s in cars:
            time = (target - p)/s
            #print(time)
            if stack and stack[-1] > time:
                continue
            elif stack and stack[-1] == time:
                continue
            stack.append(time)
        #print(stack)
        return len(stack)