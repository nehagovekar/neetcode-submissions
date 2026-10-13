class Solution:

    def encode(self, strs: List[str]) -> str:
        #note that it has to be stateless
        #converting the list into encoded string so initialize a string
        encoded_string=""
        #note that you have to chooose if iterating the length etc. v imp-->iterate over elements or indices
        #Default to for s in strs whenever you only need the actual values. Use range(len(strs)) when you need to access or manipulate elements by their positions.
        for s in strs:
            #neet
            encoded_string+=  str(len(s))+"#"+s
        return encoded_string
        #5#Hello5#World


    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        #decoded string initialization
        p=''
        #i will have string j will capture the hash
        while i < len(s):
            j=i 
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            p=s[j+1:j+1+length]
            res.append(p)
            i=j+length+1
        return res


        
