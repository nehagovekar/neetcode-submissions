class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #height: 1,7,2,5,4,7,3,6
        #width: index of x - index of y
        #for eg. 7,5: width: 3-1=2
        #height: min(7,5)=5

        l,r=0, len(heights)-1
        max_area = 0

        while l<r:
            h = min(heights[l], heights[r])
            w= r-l
            area=h*w
            max_area=max(area, max_area)

            #tricky part is how do we move the l and r. When we reduce the width our hope is that we can maximize the height so that area is maximum
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return max_area



 
        