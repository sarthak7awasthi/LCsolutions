class Solution:
    def firstUniqChar(self, s: str) -> int:
        Arr = list(s)
        Arr.sort()
        repArr = []
        
        if s == "":
            return -1
        
        if len(s) < 2:
            return 0
        
        if Arr[0] != Arr[1]:
            repArr.append(Arr[0])
            
        if Arr[len(Arr)-1] != Arr[len(Arr)-2]:
            repArr.append(Arr[len(Arr)-1])
        
        for i in range(1, len(Arr) - 1):
            if Arr[i] != Arr[i+1] and Arr[i] != Arr[i - 1]:
                repArr.append(Arr[i])
                
        for i in range(len(s)):
            if s[i] in repArr:
                return i
            
            
        return -1
