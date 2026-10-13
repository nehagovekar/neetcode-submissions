class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so the logic is to put all the numbers in a set and deduplicate first
        #then traverse the set and check if the number minus 1 exists in the set if not that can be the first of the sequence so initialize length as 1
        numSet= set(nums)
        longest=0

        #traverse we want numbers not indices therefore
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while(num+length) in numSet:
                    length+=1
                longest=max(length, longest)
        return longest
       


        