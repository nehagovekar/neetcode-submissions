class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #since we want to check if two strings are anagrams, their count of characters should be the same.
        #Lets create two hashmaps to create key, value pair where key is the character and value is the count

        countS={}
        countT={}

        #check if the length is same of both the strings if not, its not an anagram anyway
        if(len(s)!=len(t)):
            return False

        #Now, lets count by using a for loop to iterate through the array

        for i in range(len(s)):
            countS[s[i]]= countS.get(s[i],0)+1
            countT[t[i]]=countT.get(t[i],0)+1

        return countS==countT
        