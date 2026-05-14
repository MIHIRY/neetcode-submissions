class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # intitial max = -1
        # reverse iteration 
        # new max = max(oldmax, arr[i])

        rightmax = -1

        for i in range(len(arr)-1 , -1 , -1):
            newmax = max(arr[i], rightmax)
            arr[i] = rightmax

            rightmax = newmax
        return arr

