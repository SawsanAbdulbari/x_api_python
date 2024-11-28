from config.x_client import *
import logging
logging.basicConfig(level=logging.INFO)

client = get_client()

def like_tweet(tweet_id):
    try:
        response = client.like(tweet_id=tweet_id)
        if response.data:
            logging.info(f"Tweet {tweet_id} liked successfully.")
        else:
            logging.error(f"Failed to like tweet {tweet_id}. Response: {response}")
    except Exception as e:
        logging.error(f"Error liking tweet {tweet_id}: {e}")