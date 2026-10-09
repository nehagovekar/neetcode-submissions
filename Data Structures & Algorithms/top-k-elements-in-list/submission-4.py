class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket sort, where the index is the frequency, so placing something is the sorting.
        #step 1: lets have a dictionary with key values where key is the number value is the count
        cnt={}
        for n in nums:
            cnt[n]= cnt.get(n,0)+1

        #bucket sort is basically index being the frequency that is value in the case of cnt and the number will be saved as value
        freq=[[] for i in range(len(nums)+1)]
        for num, ct in cnt.items():
            freq[ct].append(num)

        res= []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
            