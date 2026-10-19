class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #stop trying to recall the solution try to build it!
        #step 1: lets lower and remove all the alphanumeric characters
        #we want to count the frequency of numbers: hashmap: key can be the letter and value can be the count.

        s=s.lower()
        t=t.lower()

        #length should be equal
        if (len(s)!=len(t)):
            return False

        countT={}
        countS={}

        for c in s:
            countS[c]=countS.get(c,0)+1

        for c in t:
            countT[c]= countT.get(c,0)+1

        return countS==countT



        
        