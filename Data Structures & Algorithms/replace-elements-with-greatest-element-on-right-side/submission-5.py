class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currGreatest = -1
        res = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            res[i] = currGreatest
            currGreatest = max(arr[i], currGreatest)

        return res