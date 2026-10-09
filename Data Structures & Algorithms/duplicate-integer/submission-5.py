class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create an empty hashSet
        repeated = set()

        for i in range(len(nums)):
            if nums[i] in repeated:
                return True
            repeated.add(nums[i])
        return False
        
        #revised mistake 1: forgot how to create a set
        #revised mistake 2: understand when to return true and when to return false -_-