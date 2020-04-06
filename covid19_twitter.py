import tweepy
import os
from dotenv import load_dotenv
load_dotenv()



class Covid19Tweets:
    """
    A class that retrieves and processes tweets about COVID-19
    using the Twitter API.
    """

    def __init__(self, consumer_key=os.getenv("CONSUMER_KEY"),
                 consumer_secret=os.getenv("CONSUMER_SECRET"),
                 access_token=os.getenv("ACCESS_TOKEN"),
                 access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")):
        """
        Initailizes an instance of Covid19Tweets.
        @consumer_key: The Twitter API's consumer key
        @consumer_secret: The Twitter API's consumer secret key
        @access_token: The Twitter API's access token
        @access_token_secret: The Twitter API's access token secret
        return: None
        rtype: None
        """
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Create API object
        self._api = tweepy.API(auth)


    def get_tweets(self, region, num_rpp):
        """
        Gets COVID-19 related tweets for the given region.
        @region: The region to retrieve COVID-19-related tweets about
        @num_rpp: The number of most recent public tweets to retrieve
        type region: str
        type num_rpp: int
        return: A list containing the <num_rpp> most recent tweets
        rtype: [str]
        """
        result = []
        # TODO: Allow q to be more flexible
        # TODO: Store the whole JSON responses instead of using
        #       just extracting values from them?
        for tweet in self._api.search(q=f"coronavirus {region}", lang="en", rpp=num_rpp):
            result.append(f"{tweet.user.name}:{tweet.text}")

        return result




if __name__ == "__main__":
    c_tweets = Covid19Tweets()
    tweets = c_tweets.get_tweets("japan", 10)
    print(tweets)
