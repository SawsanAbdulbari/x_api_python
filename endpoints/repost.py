from config.x_client import *
client = get_client()

repost_tweet_id_path = os.path.join(data_path, "repost_tweet_id.txt")

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
        
def post_repost(post_id):
    try:
        tweet = client.get_tweet(
            post_id,
            tweet_fields=["public_metrics"],  
            expansions=["author_id", "geo.place_id"]  
        )

        if tweet.data:
            tweet_data = tweet.data

            tweet_text = tweet_data['text']
            retweet_count = tweet_data['public_metrics']['retweet_count']
            like_count = tweet_data['public_metrics']['like_count']
            reply_count = tweet_data['public_metrics']['reply_count']
            quote_count = tweet_data['public_metrics']['quote_count']
            
            author_id = tweet.includes['users'][0]['id'] if 'users' in tweet.includes else "Unknown"
            
            location = None
            if 'places' in tweet.includes:
                location = tweet.includes['places'][0] 

            print(f"Tweet found: {tweet_text}")
            print(f"Retweets: {retweet_count}, Likes: {like_count}, Replies: {reply_count}, Quotes: {quote_count}")
            print(f"Author ID: {author_id}")
            if location:
                print(f"Location: {location['name']} (Place ID: {location['id']})")
            else:
                print("Location data not available.")

            response = client.retweet(post_id)
            print(f"Tweet retweeted successfully! Retweet ID: {response.data['id']}")
        else:
            print("Tweet not found.")
        
    except tweepy.TweepyException as e:
        print(f"Error while retweeting: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
repost_tweet_id = read_file(repost_tweet_id_path)
post_repost(repost_tweet_id)