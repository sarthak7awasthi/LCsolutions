class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        MergedList=[]
        for i in intervals:
            if not MergedList or MergedList[-1][1] < i[0]:
                MergedList.append(i)
            else:
                MergedList[-1][1]= max(MergedList[-1][1],i[1])
        return MergedList