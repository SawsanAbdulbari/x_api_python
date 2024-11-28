import sys
import os
import time
# import logging
from config import config
from config.x_client import get_client


from utils.directory_exists import is_directory_exists

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Data path
data_path = config.data_path

def get_user_id(username, output_file):
    client = get_client()
    try:
        user = client.get_user(username=username)
        user_id = user.data.id
        
        # Ensure the directory exists
        is_directory_exists(os.path.dirname(output_file))
        
        # Write the user ID to a file
        with open(output_file, 'w') as file:
            file.write(str(user_id)) 
            print(f"User ID for {username} saved to {output_file}")
        
        return user_id
    except Exception as e:
        print(f"Error fetching user ID for {username}: {e}")


