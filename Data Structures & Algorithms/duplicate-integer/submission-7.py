class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #traverse through the array to check for hasDuplicate
        #Use a set --> contains no duplicates

        isDuplicate= set()

        for i in range(len(nums)):
            #if the number is present in the set that means it contains duplicates
            if nums[i] in isDuplicate:
                return True
            #if not it needs to be added in the set for the remaining numbers
            isDuplicate.add(nums[i])

        return False
            
            
        

        