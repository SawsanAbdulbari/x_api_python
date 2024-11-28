# import logging
import argparse
import os
from endpoints import post_text_only_tweet,post_tweet_with_image,delete_tweet,like_tweet,get_user_id,get_user_details,post_repost
from time import sleep
import config as config

# Data path
data_path = config.data_path

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()

def main():
    parser = argparse.ArgumentParser(description="X Bot Operations")
    parser.add_argument('--post-text', action='store_true', help='Post a text-only tweet')
    parser.add_argument('--post-image', action='store_true', help='Post a tweet with an image')
    parser.add_argument('--like-tweet', action='store_true', help='Like a tweet')
    parser.add_argument('--get-followers', action='store_true', help='Get followers list')
    parser.add_argument('--get-following', action='store_true', help='Get following list')
    parser.add_argument('--delete-tweet', action='store_true', help='Delete the last tweet')
    parser.add_argument('--get-pinned-lists', action='store_true', help='Get pinned lists')
    parser.add_argument('--pin-list', type=str, help='Pin a list by list ID')
    parser.add_argument('--unpin-list', type=str, help='Unpin a list by list ID')
    parser.add_argument('--get-lists', action='store_true', help='Get user lists')
    parser.add_argument('--repost-tweet', type=str, help='Repost a tweet by tweet ID')
    parser.add_argument('--test', action='store_true', help='Run in test mode without making API calls')
    args = parser.parse_args()

    if args.test:
        print("Running in test mode. No API calls will be made.")

        return

    # Post a text-only tweet
    tweet_text_only_path = os.path.join(data_path, "tweet_text_only.txt")
    tweet_text_only = read_file(tweet_text_only_path)
    post_text_only_tweet(tweet_text_only)

    # Post a tweet with an image
    image_path = os.path.join(data_path, "logo.jpeg")
    tweet_with_image_path = os.path.join(data_path, "tweet_with_image.txt")
    tweet_with_image = read_file(tweet_with_image_path)
    post_tweet_with_image(tweet_with_image, image_path)

    sleep_duration = int(os.getenv("SLEEP_DURATION", 10))
    sleep(sleep_duration)
    
    # if  delete_tweet:
    delete_tweet_id_path = os.path.join(data_path, "delete_tweet_id.txt")
    delete_tweet_id = read_file(delete_tweet_id_path)
    delete_tweet(delete_tweet_id)

    # if args.like_tweet and tweet_id:
    like_tweet_id_path = os.path.join(data_path, "like_tweet_id.txt")
    like_tweet_id = read_file(like_tweet_id_path)
    like_tweet(like_tweet_id)
    # logging.info(f"Tweet {tweet_id} liked successfully.")

    # Fetch user ID
    username = "laureauas"
    user_id_file = os.path.join(data_path, "user_id.txt")
    user_id = get_user_id(username, user_id_file)

    # Fetch user details
    if user_id:
            # Fetch and print user details
        user_details = get_user_details(user_id)
        if user_details:
            print(f"User Details: {user_details}")
    
                # Save user details to a file
            user_details_file = os.path.join(data_path, "user_details.txt")
            try:
                with open(user_details_file, 'w') as file:
                    file.write(str(user_details))  # Convert user details to string
                print(f"User details saved to {user_details_file}")
            except Exception as e:
                print(f"Error saving user details to file: {e}")
    
    repost_tweet_id_path = os.path.join(data_path, "repost_tweet_id.txt")
    repost_tweet_id = read_file(repost_tweet_id_path)
    post_repost(repost_tweet_id)

if __name__ == "__main__":
    main()