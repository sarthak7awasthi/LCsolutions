class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        
        newList=[]
        for i in intervals:
            if len(newList)>0:
                if newList[-1][1]<i[0] or newList[-1][1]==i[0]:
                    newList.append(i)
                    continue
                else:
                    return False
            else:
                newList.append(i)
        return True