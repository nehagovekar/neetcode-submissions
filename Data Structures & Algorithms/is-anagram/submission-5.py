class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #step 1: checking the length
        if(len(s)!=len(t)):
            return False
        #creating 2 dictionaries first to then check if count is equal for all the keys which are letters here
        sdict, tdict = {},{}
        #here, since the length now will be same we can iterate for that length
        for i in range(len(s)):
            #three things we need to check now, first if the s[i] is already present in the keys, else add it with counter of 0
            sdict[s[i]]= 1+ sdict.get(s[i],0)
            tdict[t[i]]= 1+ tdict.get(t[i],0)

        return sdict==tdict
       

        
  
        