class Solution:
    def generate(self, numRows):
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        arr = []
        for i in range(numRows):
            arr.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    arr[i].append(1)
                else:
                    arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
        return arr