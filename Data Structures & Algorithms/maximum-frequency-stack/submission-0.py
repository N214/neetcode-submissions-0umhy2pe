class FreqStack:

    def __init__(self):
        self.cnt = {} 
        self.maxCount = 0
        self.stacks = {} # map count to the frequency group 

    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt
        if valCnt > self.maxCount:
            self.maxCount +=1
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()