# import logging
from config.x_client import get_client

client = get_client()

def get_pinned_lists(user_id):
    try:
        response = client.get_pinned_lists(user_id=user_id)
        if response.data:
            print(f"Pinned lists for user {user_id}: {response.data}")
            return response.data
        else:
            print(f"No pinned lists found for user {user_id}.")
    except Exception as e:
        print(f"Error retrieving pinned lists for user {user_id}: {e}")

# def pin_list(user_id, list_id):
#     try:
#         response = client.pin_list(user_id=user_id, list_id=list_id)
#         if response.data:
#             print(f"List {list_id} pinned successfully for user {user_id}.")
#         else:
#             print(f"Failed to pin list {list_id} for user {user_id}. Response: {response}")
#     except Exception as e:
#         print(f"Error pinning list {list_id} for user {user_id}: {e}")

# def unpin_list(user_id, list_id):
#     try:
#         response = client.unpin_list(user_id=user_id, list_id=list_id)
#         if response.data:
#             print(f"List {list_id} unpinned successfully for user {user_id}.")
#         else:
#             print(f"Failed to unpin list {list_id} for user {user_id}. Response: {response}")
#     except Exception as e:
#         print(f"Error unpinning list {list_id} for user {user_id}: {e}") 