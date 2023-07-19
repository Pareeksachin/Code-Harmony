from queue import Queue

class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        arr = []
        while not q.empty():
            arr.append(q.get())
        
        new_queue = Queue(maxsize=len(arr))
        while len(arr) > 0:
            new_queue.put(arr.pop())
        
        return new_queue


from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends
