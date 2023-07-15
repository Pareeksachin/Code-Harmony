
import math
class Solution:
    def deleteMid(self, s, sizeOfStack):
        if sizeOfStack%2 != 0:
            s.pop(sizeOfStack//2)
        else:
            s.pop((sizeOfStack//2)-1)
import sys
sys.setrecursionlimit(10**8)

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
