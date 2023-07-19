#User function Template for python3

class Solution:
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        freq = {}
        for ele in s:
            if ele in freq:
                freq[ele]+=1
            else:
                freq[ele]=1
        
        for char in s:
            if freq[char]==1:
                return char
        return "$"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# } Driver Code Ends
