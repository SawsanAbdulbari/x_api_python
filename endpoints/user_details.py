from config.x_client import get_client
client = get_client()

def get_user_details(user_id):
    try:
        user_details = client.get_user(id=user_id)
        return user_details
    except Exception as e:
        print(f"Error retrieving user details for {user_id}: {e}")
        return None
