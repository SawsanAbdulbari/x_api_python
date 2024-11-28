import os
from config.x_client import *

client = get_client()
api = get_api()


def post_tweet_with_image(text, image_path):
    media_id = api.media_upload(filename=image_path).media_id_string
    print("Media ID:", media_id)

    response = client.create_tweet(text=text, media_ids=[media_id])
    tweet_id = response.data['id']
    print("Tweet posted successfully:", response)
    
    save_tweet_id(tweet_id)
   

def save_tweet_id(tweet_id):
    tweet_id_file = os.path.join(data_path, "like_tweet_id.txt")
        
        # Write tweet ID to file
    with open(tweet_id_file, 'w') as id_file:
        id_file.write(tweet_id)
        print(f"Tweet ID {tweet_id} saved to {tweet_id_file}")