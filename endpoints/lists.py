# import logging
from config.x_client import get_client

client = get_client()

def get_user_lists(user_id):
    try:
        response = client.get_lists(user_id=user_id)
        if response.data:
            for lst in response.data:
                print(f"List ID: {lst.id}, Name: {lst.name}")
            return response.data
        else:
            print(f"No lists found for user {user_id}.")
    except Exception as e:
        print(f"Error retrieving lists for user {user_id}: {e}") 