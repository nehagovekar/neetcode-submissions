class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #step 1: sort the array since we want to use the logic of 2 pointers pattern
        nums.sort()
        res=[]
        #for three sum, keep one fixed pointer and two moving
        #we want the range to -2 since we want i+2 to be a possibility
        for i in range(len(nums)-2):
            #the current fixed number should not be the same as its previous number
            if i>0 and nums[i]==nums[i-1]:
                continue
            #now we know that we are not using the same number twice
            l=i+1
            r=len(nums)-1

            #here it gets confusing the idea is that sum of all three numbers should be 0, so lets see the sum of the numbers if it is greater then 0 then we need a smaller number so r--, if it is smaller than 0 we need a bigger number hence l++. Now, if after this we find the sum is 0 then we return those numbers 
            while(l<r):
                #The sum calculation and pointer movements must ALL happen inside this while loop.
                total_sum= nums[i]+nums[l]+nums[r]
                #print(total_sum)
                if total_sum<0:
                    l+=1
                elif total_sum>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l],nums[r]])
                    l+=1
                    r-=1
                    #this while loop should have been in else block to remove duplicates while running in the loop
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
            
            #now we dont want the l to be the same as l-1 otherwise it will be the same triplets again
            
                

        return res

        
                    




    
      
           

    






        