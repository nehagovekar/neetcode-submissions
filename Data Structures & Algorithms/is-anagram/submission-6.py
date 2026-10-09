class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the idea is to find out that frequency of each letter is same or not
        #lets filter with if the length is same or not
        if (len(s)!= len(t)):
            return False
        countS, countT={},{}
        #since I am using 2 words, using zip! I get so confused with counting in dictionaries. Just get used to the syntax-->
        for i,j in zip(s,t):
            countS[i]= countS.get(i,0)+1
            #What it does: It adds 1 to the count for x. If x isn't in the dict yet, its count starts from 0.
            countT[j]= countT.get(j,0)+1
        return countS == countT

            
      

        