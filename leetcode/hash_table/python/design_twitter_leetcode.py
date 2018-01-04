"""
https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

1. postTweet(userId, tweetId): Compose a new tweet.

2. getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.

3. follow(followerId, followeeId): Follower follows a followee.

4. unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

https://discuss.leetcode.com/topic/48205/use-python-heapq-merge
"""
import collections
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_store = collections.defaultdict(list)
        self.relationships = collections.defaultdict(set)
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1

        self.tweet_store[userId].append((tweetId, self.time))



    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        result = []

        # get user's tweets
        user_tweets = self.tweet_store[userId] if userId in self.tweet_store else []

        # add the result
        result.extend(user_tweets)

        # get all user's followers by id
        followed_user_ids = self.relationships[userId] if userId in self.relationships else []

        # get tweets of all followers
        for follower_id in followed_user_ids:
            result.extend(self.tweet_store[follower_id]) if follower_id in self.tweet_store else []

        # sort result by time posted; reverse list to keep most recent tweets first. Remember sorting in asc by default so we need to reverse to get desc order
        res =  list(reversed(sorted(result, key = lambda x: x[1])))

        # return 10 most recent tweets
        return [i for i, j in res][:10]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return

        self.relationships[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return

        self.relationships[followerId].discard(followeeId)
        # .discard Removes element elem from the set if it is present.
        # above is same as below
        # if followerId in self.relationships:
        #     if followeeId in self.relationships[followerId]:
        #         self.relationships[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# if __name__ == '__main__':
    # obj = Twitter()
    # obj.postTweet(1, 5)
    # print obj.tweet_store
    # print obj.getNewsFeed(1)
    # obj.follow(1, 2)
    # obj.postTweet(2, 6)
    # print obj.tweet_store
    # print obj.getNewsFeed(1)
    # print obj.relationships
    # obj.unfollow(1, 2)
    # print obj.relationships
    # print obj.getNewsFeed(1)

    # obj = Twitter()
    # obj.postTweet(1, 1)
    # print obj.getNewsFeed(1)
    # obj.follow(2, 1)
    # print obj.getNewsFeed(2)
    # obj.unfollow(2, 1)
    # print obj.getNewsFeed(2)

    # obj = Twitter()
    # obj.follow(1, 5)
    # print obj.getNewsFeed(1)
    # print '\n'
    # twitter = Twitter()
    # twitter.postTweet(1, 5)
    # twitter.postTweet(1, 3)
    # print twitter.tweet_store
    # print twitter.getNewsFeed(1)

    # t = Twitter()
    # t.postTweet(1, 5)
    # t.postTweet(1, 3)
    # t.postTweet(1, 101)
    # t.postTweet(1, 13)
    # t.postTweet(1, 10)
    # t.postTweet(1, 2)
    # t.postTweet(1, 94)
    # t.postTweet(1, 505)
    # t.postTweet(1, 333)
    # t.postTweet(1, 22)
    # t.postTweet(1, 11)
    # print t.tweet_store
    # print t.getNewsFeed(1)
