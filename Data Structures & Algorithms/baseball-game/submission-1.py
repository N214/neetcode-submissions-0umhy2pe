class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            print(f"{score=}")
            try:
                integer = int(i)
                score.append(integer)
            except:
                if i == "+":
                    summ = score[-1] + score[-2]
                    score.append(summ)
                if i == "C":
                    score.pop()
                if i == "D":
                    double = score[-1] * 2
                    score.append(double)
        return sum(score)

