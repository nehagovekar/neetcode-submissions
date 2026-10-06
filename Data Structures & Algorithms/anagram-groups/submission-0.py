class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a hashmap
        result= defaultdict(list)

        #iterate every string in the list
        for s in strs:
            #creating an array of 26 initialize with 0
            count=[0]*26
            #now you have one word at a time and you need to traverse that word
            for i in s:
                #you need to count letters in that word
                count[ord(i)-ord("a")] +=1
                #ord() tells about ascii value
                #a -> 80 therefore it will be 80-80=0th place
                #b -> 81 therefore it will be 81-80=1st place and so on
            result[tuple(count)].append(s)
            #list can't be key in a dictionary, hence tuple.
        return result.values()


        