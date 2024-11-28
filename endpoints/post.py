import os
from config.x_client import *
client = get_client()

def post_text_only_tweet(text):
    response = client.create_tweet(text=text)
    tweet_id = response.data['id']
    print("Text only tweet posted successfully:", response)

    save_tweet_id(tweet_id)

def save_tweet_id(tweet_id):
    tweet_id_file = os.path.join(data_path, "delete_tweet_id.txt")
        # Write tweet ID to file
    with open(tweet_id_file, 'w') as id_file:
        id_file.write(tweet_id)
        print(f"Tweet ID {tweet_id} saved to {tweet_id_file}")