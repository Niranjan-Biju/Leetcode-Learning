class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in newMap:
                return [newMap[diff],i]
                exit()
            else:
                newMap[n] = i
