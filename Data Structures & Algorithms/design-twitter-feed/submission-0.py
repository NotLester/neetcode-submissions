from collections import defaultdict, deque
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        # deque(maxlen=10) automatically drops oldest tweets when > 10
        self.posts: defaultdict[int, deque] = defaultdict(lambda: deque(maxlen=10))
        self.i = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.i, tweetId))
        self.i += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        # 1. Get all relevant users (the user themselves + people they follow)
        users = self.follows[userId].copy()
        users.add(userId)
        
        heap = []
        # 2. Populate the heap with the *most recent* tweet from each user
        for u in users:
            if self.posts[u]:
                time, tweetId = self.posts[u][0]
                # Python's heapq is a min-heap. We want the largest timestamp first, 
                # so we push negative time. We also store the user ID and the current index.
                heapq.heappush(heap, (-time, tweetId, u, 0))
                
        # 3. Pull the newest tweet 10 times (or until heap is empty)
        while heap and len(res) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            res.append(tweetId)
            
            # If this user has an older tweet in their deque, push it to the heap
            if idx + 1 < len(self.posts[u]):
                next_time, next_tweetId = self.posts[u][idx + 1]
                heapq.heappush(heap, (-next_time, next_tweetId, u, idx + 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)