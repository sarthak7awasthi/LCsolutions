class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for i in digits:
            number+=str(i)
        number=int(number)+1
        number=str(number)
        l=[]
        for i in number:
            l.append(i)
            
        return l
