class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #lets calculate prefix first and store it in an array such that each index should have the product of all the values before it.
        #fixed length array syntax remember
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            #yes, first val will always be one because it stores value of something that is before that but in this case thats nothing
            res[i]=prefix
            prefix*=nums[i]

        postfix=1
        #the reverse loop should go to -1 not 0
        #saving space by directly multiplying postfix to already present prefix
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]

        return res

           

        
        