class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#brute force: check combination to sum up to the target.
#we are looking for a difference, hashmap of every value, mapping value to the index
#always remember first visit the element then add it to hashmap if not present

        #create an empty hashmap
        prevM= {}
        #traverse through the array, since you want both value and index use enumerate
        for i, n in enumerate(nums):
            difference = target - n
            #mistake 1: since this checks for the second time the difference will be present in the prevM not nums
            if difference in prevM:
                return[prevM[difference],i]
            #syntax to remember to add value to hashmap, in this case, value is the key and index is the value iykyk
            prevM[n]=i

     
    
       
        

        