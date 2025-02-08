import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://api.deepseek.com/user/balance"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {os.getenv("DEEPSEEK_API_KEY")}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
