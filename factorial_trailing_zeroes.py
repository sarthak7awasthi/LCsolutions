class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=1
        fact=1
        while i<=n:
            fact=fact*i
            i+=1
        fact=str(fact)
        c=0
        for j in fact[::-1]:
            if j=="0":
                c+=1
            else:
                return c
