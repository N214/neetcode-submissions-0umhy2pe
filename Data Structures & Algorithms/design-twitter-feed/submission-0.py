import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followmap = defaultdict(set)  # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Standard positive count increment. Higher numbers mean newer tweets.
        self.tweetmap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        maxHeap = []

        # Combine users followed + the user themselves
        connections = self.followmap[userId] | {userId}

        for followee in connections:
            if followee in self.tweetmap:
                # Start at the end of the array (newest tweet)
                index = len(self.tweetmap[followee]) - 1
                count, tweetId = self.tweetmap[followee][index]
                # Push the data. Max-heap sorts primarily by the first element (`count`)
                maxHeap.append([count, tweetId, followee, index - 1])
        
        # Python 3.14 native max heapify
        heapq.heapify_max(maxHeap)
        
        while maxHeap and len(res) < 10:
            # Python 3.14 native max heappop (pulls the largest `count`)
            count, tweetId, followee, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            
            # If there are older tweets remaining for this user, look at the previous index
            if index >= 0:
                count, tweetId = self.tweetmap[followee][index]
                # Python 3.14 native max heappush
                heapq.heappush_max(maxHeap, [count, tweetId, followee, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)