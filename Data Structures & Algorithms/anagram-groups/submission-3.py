class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #when things are supposed to be put in buckets use defaultDict
        #If I access a key that doesn't exist, automatically create an empty list [].
        res = defaultdict(list)
        
        #first iterate through list, we dont need index here
        for s in strs:
            #26 letters so creating a empty list of 26 characters which will be key in the dictionary, so in case empty word, thats why defaultdict
            cnt= [0]*26
            #now iterate through each word for count
            for i in s:
                cnt[ord(i)-ord('a')]+=1
                #here ord converts letter to ascii value
                #by the end of this inner loop we understand the letter and its frequency which we will now store somewhere
            #now cnt has frequency which is going to be the key and s is the word which will be added to the list of values
            #here we use tuple because Python dictionaries require keys to be hashable. A list isn't hashable, but a tuple is.
            #dict values are added using append
            res[tuple(cnt)].append(s)

        return list(res.values())
            



        