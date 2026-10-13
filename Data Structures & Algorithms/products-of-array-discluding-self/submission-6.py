class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #lets calculate prefix first and store it in an array such that each index should have the product of all the values before it.
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]

        return res

           

        
        