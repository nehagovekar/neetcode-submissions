class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap seen
        #iterate through the list and check the difference between target and the number then check if that number is present in the hashmap if yes, return the indices if not put that number in the hashmap
        seen={}
        for i,n in enumerate(nums):
            diff= target - n
            if diff in seen:
                return [seen[diff],i]

            seen[n]=i
'''
The one thing I want you to remember from Two Sum:

seen[number] = index

The number is your key. Its position is your value.

This distinction is fundamental to HashMap problems like Group Anagrams and Top K Frequent Elements.
'''

#mistake 1: dont try to memorize it, you used hashmap to get the index of the number just in case you find the difference you want to retrieve the index it was at!
#mistake 2: its simple while iterating if you find a number not visited you want to store it's key(the number) and value (the value)
    


    
      


     

     
        