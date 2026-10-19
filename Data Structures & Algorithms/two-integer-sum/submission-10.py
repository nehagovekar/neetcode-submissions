class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #lets think it out loud first: 

        #traverse through the array

        isAvail={}

        for i in range(len(nums)):
            diff= target-nums[i]
            if diff in isAvail:
                return [isAvail[diff],i]
                #return [nums[i],nums[diff]]
            
            isAvail[nums[i]]=i
   
      
        