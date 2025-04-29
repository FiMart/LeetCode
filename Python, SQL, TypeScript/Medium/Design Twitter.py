class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)  # userId -> list of tweets
        self.user_following = defaultdict(set)  # userId -> set of followeeIds
        self.tweets = defaultdict()  # tweetId -> (userId, timestamp)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.user_following[userId]
        users = set(following)
        users.add(userId)  # Include the userId itself
        tweets = [self.user_tweets[u][::-1][:10] for u in users]
        tweets = sum(tweets, [])
        return nlargest(10, tweets, key = lambda tweet: self.tweets[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.user_following[followerId]
        if followeeId in following:
            following.remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)