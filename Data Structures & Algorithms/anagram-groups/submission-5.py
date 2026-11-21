class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. RULE 1: IF BUCKETS USE DEFAULTDICT
        res= defaultdict(list) #specify it is a dict of list

        #Let us iterate the string one word at a time first
        for s in strs:
            #here we create an array to understand the frequency of each letter in a word so the index is letters for our understanding and the value on that index will be the count of frequency of letters
            cnt=[0]*26  #remember the initialization syntax

            #Now, each character to be traversed in the string
            for c in s:
                #now ord converts characters to ascii
                cnt[ord(c)-ord('a')]+=1
                #this arr is basically [0,1,0,1,0...,1,0] for 26 characters
                #Now, we need to check how many words have the same frequency so this arr should be the key and strings should be appended to the list of values
                #Here is the catch: the key for hashmaps should be immutable but list/array is mutable tuple is not so lets convert it first

            res[tuple(cnt)].append(s)

        return list(res.values())




        