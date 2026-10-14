class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Neha's unfiltered thought process-> first lowering all the characters, then checking if alphanumeric, then we will have the string-->we will have 2 pointers, one left, right right--> we should check if they are equal if yes l++ and r-- check until length of the string/2. If right not equal to left return False .


        #step 1: lowering the characters
        s=s.lower()

        #step 2: check if alphanum and store it in a string isAlpha
        isAlpha=""
        for c in s:
            #beginner mistake: isalnum check if you are calling the method or executing it :)
            if c.isalnum():
                isAlpha+=c
        l=0
        r=len(isAlpha)-1

        #dont forget to change the pointers :p
        while(l<r):
            if(isAlpha[l]!=isAlpha[r]):
                return False
            l+=1
            r-=1
            
        return True

       
        