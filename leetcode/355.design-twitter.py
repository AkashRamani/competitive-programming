#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:
    '''
        Time: 
        1. post tweet: O(1)
        2. Follow/ Unfollow: O(1)
        3. getNewsFeed..
            if user is following N users:
                To consturct intial heap using the max of each tweet_list [last element by design] --> O(N)
                After this -- we roughtly push-pop K (10 here) times      --> K * O(log N) = O(K log N)
            ---------------------------
            Total: O(N) when k=10.. but lets say its : O(N) + O(K log N) to be more accurate
            NOTE: K here is 10. But K can grow very large in real scenarios.. aand getNewsFeed is designed accordingly
    '''

    def __init__(self):
        self.users = defaultdict(dict)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.setdefault(userId, {} ).setdefault('tweets', list())
        self.users.get(userId)['tweets'].append((self.count, tweetId))
        self.count+=1
    def get_top_k_tweets(self, user_tweets, k):
        top_k_tweets = []
        indices = [len(tweets)-1 for tweets in user_tweets]

        max_heap = []
        while k>0:
            if max_heap:
                max_count = -1 * heapq.heappop(max_heap)
                tweet_id, array_index = tweet_map[max_count]
                top_k_tweets.append(tweet_id)
                k-=1

                index = indices[array_index]
                if index<0:
                    continue
                element = user_tweets[array_index][index]
                indices[array_index] = index - 1

                count, tweet_id = element
                tweet_map[count] = (tweet_id, array_index)
                heappush(max_heap, -count)


            else:
                max_heap = []
                tweet_map = {}
                for array_index, index in enumerate(indices):
                    if index<0:
                        continue
                    element = user_tweets[array_index][index]
                    indices[array_index] = index - 1

                    count, tweet_id = element
                    tweet_map[count] = (tweet_id, array_index)
                    max_heap.append(-count)
                    
                if not max_heap:
                    break           
                
                heapq.heapify(max_heap)
                
        return top_k_tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        # retrive top 10 tweets
        self.users.setdefault(userId, {} ).setdefault('followers', set())
        followers = self.users.get(userId)['followers']

        tweets_by_followers = []
        for follower_id in followers:
            self.users.setdefault(follower_id, {} ).setdefault('tweets', list())
            tweets = self.users.get(follower_id)['tweets']
            tweets_by_followers.append(tweets)
        
        self.users.setdefault(userId, {} ).setdefault('tweets', list())
        tweets_by_self = self.users.get(userId)['tweets']
        tweets_by_followers.append(tweets_by_self)

        news_feed = self.get_top_k_tweets(tweets_by_followers, 10)
        return news_feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, {} ).setdefault('followers', set())
        self.users.get(followerId)['followers'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users.setdefault(followerId, {} ).setdefault('followers', set())
        self.users.get(followerId)['followers'].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

