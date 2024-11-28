# import argparse
# import logging
import os
from endpoints import get_user_id,get_user_details
from time import sleep
import config as config

# from utils import configure_logging

# from tweepy import TooManyRequests
# from endpoints.pinned_lists import get_pinned_lists, pin_list, unpin_list
# from endpoints.lists import get_user_lists

# configure_logging()

# Data path
data_path = config.data_path

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    # else:
    #     logging.warning(f"File {file_path} does not exist.")
    #     return None

def main():
    # parser = argparse.ArgumentParser(description="X Bot Operations")
    # parser.add_argument('--post-text', action='store_true', help='Post a text-only tweet')
    # parser.add_argument('--post-image', action='store_true', help='Post a tweet with an image')
    # parser.add_argument('--like-tweet', action='store_true', help='Like a tweet')
    # parser.add_argument('--get-followers', action='store_true', help='Get followers list')
    # parser.add_argument('--get-following', action='store_true', help='Get following list')
    # parser.add_argument('--delete-tweet', action='store_true', help='Delete the last tweet')
    # parser.add_argument('--get-pinned-lists', action='store_true', help='Get pinned lists')
    # parser.add_argument('--pin-list', type=str, help='Pin a list by list ID')
    # parser.add_argument('--unpin-list', type=str, help='Unpin a list by list ID')
    # parser.add_argument('--get-lists', action='store_true', help='Get user lists')
    # parser.add_argument('--test', action='store_true', help='Run in test mode without making API calls')
    # args = parser.parse_args()

    # if args.test:
    #     logging.info("Running in test mode. No API calls will be made.")
    #     # Simulate operations here
    #     return

    # try:
        # Set the tweet_id_file path
    # tweet_id_file = os.path.join(data_path, "tweet_id.txt")
        
        # Check if the directory exists (if needed)
        # If you have a function to check directory existence, use it here
        # is_directory_exists(os.path.dirname(tweet_id_file))
        
        # tweet_id = None

        # Only read tweet_id if needed for like or delete operations

        # if post_text:
        # Post a text-only tweet
    # tweet_text_only_path = os.path.join(data_path, "tweet_text_only.txt")
    # tweet_text_only = read_file(tweet_text_only_path)
    # post_text_only_tweet(tweet_text_only)

        # if args.post_image:
        # Post a tweet with an image
    # image_path = os.path.join(data_path, "logo.jpeg")
    # tweet_with_image_path = os.path.join(data_path, "tweet_with_image.txt")
    # tweet_with_image = read_file(tweet_with_image_path)
    # post_tweet_with_image(tweet_with_image, image_path)

    # sleep_duration = int(os.getenv("SLEEP_DURATION", 10))
    # sleep(sleep_duration)
    
    # if  delete_tweet:
    #     tweet_id = read_file(tweet_id_file)
    #     delete_tweet(tweet_id)

        
        # if args.like_tweet and tweet_id:
        # like_tweet(tweet_id)
        # logging.info(f"Tweet {tweet_id} liked successfully.")


        # if args.delete_tweet and tweet_id:
        # Delete the tweet
        # delete_tweet(tweet_id)
        # logging.info(f"Tweet {tweet_id} deleted successfully.")
        
        
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

        # if args.get_followers and user_id:
        #     try:
        #         get_followers_list(user_id)
        #         get_following_list(user_id)
            
        #     except TooManyRequests as e:
        #         wait_time = int(e.response.headers.get("x-rate-limit-reset", 60))
        #         logging.warning(f"Rate limit exceeded. Sleeping for {wait_time} seconds.")
        #         time.sleep(wait_time)
            
        #         # Retry the API call
        #         get_followers_list(user_id)
        #         get_following_list(user_id)

        # if get_pinned_lists and user_id:
        #     get_pinned_lists(user_id)

        # if args.pin_list and user_id:
        # pin_list(user_id, pin_list)

        # if args.unpin_list and user_id:
        # unpin_list(user_id,unpin_list)

        # if args.get_lists and user_id:
        # get_user_lists(user_id)

    # except Exception as e:
    #     logging.error(f"An error occurred in main: {e}")

# if __name__ == "__main__":
#     main()
    
# API_KEY = "C5jdy4gzcBEnKrcuFznxtLNv4"
# API_SECRET_KEY = "baCtk0uG5P2GvhNRYucNrLH1JiXDfu2DxJ6VVfw2xIkCP9XT6i"
# ACCESS_TOKEN = "1854840313623257088-tY2M1epnMzyJNak1vzeMiqtG5QfeOy"
# ACCESS_TOKEN_SECRET = "XSBI4EDFq41Mu3d4wJl1DLIr0qs50gFdfpwVBFWqipSje"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHpswwEAAAAAow4QZ7pVY2tJGR8k8IUg4LE8dRo%3DrHw2CSqDAluS3iByYrzpoCYNaqs66c3GkIvmF36meMY435Dlqm"
# Sawsan
# API_KEY="zhpsGryOEpVye8crnbeoXJWLI"
# API_SECRET_KEY="MgyEUNvgHPlqoB0lIkOfraVAQ45Lcstgeg2CvdpMRRIq2JhNeF"
# ACCESS_TOKEN="3305585063-RO0LjQe2v302P1j0TqjRuMSrLoVJ4HWdjiw3HR9"
# ACCESS_TOKEN_SECRET="xubKeiun2kUrqgiNigq2CjiMSdrNw6Dp1ivpD72WsWuyl"
# BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAACRuwwEAAAAAriP6KdyO%2BcBuHbNUeWh3AGwsu8w%3DFRx1nnJB7SPggRnFpOVQsj2m0XsoYLjPQyVaQOlC8Rh8Ibrsf2"
# NEW