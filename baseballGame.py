class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stakc = []
        for i in ops:
            if i == 'C':
                stakc.pop()
            elif i == 'D':
                stakc.append(stakc[-1] * 2)
            elif i == '+':
                stakc.append(stakc[-1] + stakc[-2])
            else:
                stakc.append(int(i))
        return sum(stakc)
