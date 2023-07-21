from dotenv import load_dotenv
import os

load_dotenv()

print("This is the API key from env: "+os.getenv('MY_API_KEY'))