class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        Dict={"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if Dict.get(i)==0 or Dict.get(i):
                Dict[i]=Dict[i]+1
        Dict["l"]=Dict["l"]//2
        Dict["o"]=Dict["o"]//2
        return min(Dict.values())