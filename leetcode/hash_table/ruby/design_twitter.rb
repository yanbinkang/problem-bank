require 'set'

class Twitter
  def initialize()
    @tweet_store = Hash.new { |h, k| h[k] = [] }
    @relationships = Hash.new { |h, k| h[k] = Set.new }
    @time = 0
  end

  def post_tweet(user_id, tweet_id)
    @time += 1

    @tweet_store[user_id] << [tweet_id, @time]
  end

  def get_news_feed(user_id)
    result = []

    user_tweets =
        @tweet_store.include?(user_id) ? @tweet_store[user_id] : []

    result += user_tweets

    followed_user_ids =
      @relationships.include?(user_id) ? @relationships[user_id] : []


  end
end
