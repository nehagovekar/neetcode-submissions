class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #even if the list is empty it will return an empty list
        res = {}
        
        for i, n in enumerate(nums):#say 0 is index and 2 is the number
            diff= target-n
            if diff in res:
                return [res[diff],i]
            
            res[n]=i
