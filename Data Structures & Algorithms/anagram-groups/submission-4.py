class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #grouping hence defaultDict which returns a list (empty if needed)
        res= defaultdict(list)

        #traverse the list
        for s in strs:
            #initiate a list of 26 characters to save the frequency
            cnt= [0] * 26
            #traverse each word now
            for i in s:
                cnt[ord(i)-ord('a')]+=1
            #will give eat as [1,0,0,0,1,0,0,...1,0,0]
            #need to put this as key and words as values
            #need to use tuple since key cant be a list (unhashable)
            res[tuple(cnt)].append(s)
        return(list(res.values()))
              
     



        