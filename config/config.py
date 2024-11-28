from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API keys and tokens
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

data_path = r"D:\hamk2ndyear\AnalytiikkaratkaisutLiiketoiminnanTukena\assignment4_x_api_python\data"
# Tweet IDs

# Sleep duration
# SLEEP_DURATION = 10

