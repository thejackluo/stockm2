from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

api_key = os.getenv('QUICKFS_API_KEY')

if api_key:
    print("API Key:", api_key)
else:
    print("Environment variable not found.")