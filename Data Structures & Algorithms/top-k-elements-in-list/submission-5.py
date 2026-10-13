class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #calculating the frequency
        cnt={}

        for i in range(len(nums)):
            cnt[nums[i]]= cnt.get(nums[i],0) + 1

        #{1: 1, 2: 2, 3: 3} k:v
        #now use bucket sort
        #create an array for bucket sort, create it of len+1
        freq= [[] for i in range(len(nums)+1)]

        for num, cn in cnt.items():
            freq[cn].append(num)

            #freq: [[],[1],[2],[3],[],[],[]]

            #now traverse the freq array in reverse until the length of k 
        res=[]
        for i in range(len(freq)-1, 0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res


     
       




        

        