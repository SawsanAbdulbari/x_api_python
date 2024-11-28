from config.x_client import *

client = get_client()

def delete_tweet(tweet_id):
    try:
        response = client.delete_tweet(id=tweet_id)
        if response.data:
            print(f"Tweet {tweet_id} deleted successfully.")
        else:
            print(f"Failed to delete tweet {tweet_id}. Response: {response}")
    except Exception as e:
        print(f"Error deleting tweet {tweet_id}: {e}")