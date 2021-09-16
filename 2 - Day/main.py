'''
Problem:
N meetings in one room
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.
'''

#User function Template for python3

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        final_meetings = []
        total_meetings = []
 
        for i in range(n):
            total_meetings.append(meeting(start[i], end[i], i))
            
        sorted(total_meetings,key = lambda x: x.end)
        final_meetings.append(total_meetings[0].pos)
    
        time_limit = total_meetings[0].end
        
        for i in range(1, n):
            if total_meetings[i].start > time_limit:
                final_meetings.append(total_meetings[i].pos)
                time_limit = total_meetings[i].end
             
        return len(final_meetings)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
