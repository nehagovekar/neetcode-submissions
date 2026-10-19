class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #traverse through the array and create a set of the numbers if number present in that set return True else false

        isDuplicate= set()
        for num in nums:
            if(num in isDuplicate):
                return True
            else:
                isDuplicate.add(num)
            
        return False

        