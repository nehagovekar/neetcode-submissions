class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeated= set()
        for n in nums:
            if n in repeated:
                return True
            repeated.add(n)
        return False

     
            


        
        