import csv
from config.x_client import get_client
import logging
# from tabulate import tabulate
from utils.directory_exists import is_directory_exists

client = get_client()

def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username"])  # Header
        for item in data:
            writer.writerow([item])

def display_table(data, title):
    print(f"\n{title}\n")
    # print(tabulate(data, headers=["Username"], tablefmt="grid"))

def get_followers_list(user_id):
    try:
        followers = client.get_users_followers(id=user_id)
        if followers.data:
            usernames = [[f.username] for f in followers.data]
            logging.info(f"Followers of user {user_id}: {usernames}")
            
            # Write to CSV
            is_directory_exists("result")
            write_to_csv(f"result/followers_{user_id}.csv", usernames)
            
            # Display table
            display_table(usernames, "Followers List")
        else:
            logging.info(f"No followers found for user {user_id}.")
    except Exception as e:
        logging.error(f"Error fetching followers for user {user_id}: {e}")

def get_following_list(user_id):
    try:
        following = client.get_users_following(id=user_id)
        if following.data:
            usernames = [[f.username] for f in following.data]
            logging.info(f"Users followed by {user_id}: {usernames}")
            
            # Write to CSV
            is_directory_exists("result")
            write_to_csv(f"result/following_{user_id}.csv", usernames)
            
            # Display table
            display_table(usernames, "Following List")
        else:
            logging.info(f"No following users found for user {user_id}.")
    except Exception as e:
        logging.error(f"Error fetching following users for user {user_id}: {e}") 