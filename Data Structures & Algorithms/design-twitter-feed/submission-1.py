class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.users = {}

        self.tweetHeap = []
        self.tweetCount = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[tweetId] = userId
        heapq.heappush(self.tweetHeap,(-self.tweetCount,tweetId))
        self.tweetCount += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        retArr = []
        saver = []
        while len(retArr) < 10 and self.tweetHeap :
            currPost = heapq.heappop(self.tweetHeap)
            if (self.tweets[currPost[1]] == userId or
                (userId in self.follows and self.tweets[currPost[1]] in self.follows[userId])):
                retArr.append(currPost[1])
            saver.append(currPost)
        
        for s in saver:
            heapq.heappush(self.tweetHeap,s)
        
        return retArr


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = {followeeId}
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)