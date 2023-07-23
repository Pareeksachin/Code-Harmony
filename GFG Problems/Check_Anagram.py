#User function Template for python3


class Solution:
    
    def isAnagram(self,a,b):
        if len(a) != len(b):
            return False
        freq1 ={}
        freq2 ={}
        for ch in a:
            freq1[ch] = freq1.get(ch,0)+1
        for ch in b:
            freq2[ch] = freq2.get(ch,0)+1
        return freq1 == freq2
            
            
                    
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
