#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22182189"))
API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "5680454765"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTYxNTc0Nzk5LCJvcmdJZCI6NzI1MDI2LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTkzOTMxMDc4MzEiLCJuYW1lIjoiSXJhIiwiZW1haWwiOiI2aXV3aHFsNzByQHBvd2Vyc2NyZXdzLmNvbSIsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpc0RpeSI6dHJ1ZSwibG9naW5WaWEiOiJPdHAiLCJmaW5nZXJwcmludElkIjoiZTc1ODQ4NmZiMWYzNDRmZGFkZDdhNDNmNmRmMzkzNzMiLCJpYXQiOjE3NTY5MjA1MjUsImV4cCI6MTc1NzUyNTMyNX0.AcFmTaPbUY4TPk_hmd3cVl5XadvYIoLIpHcjMWykXZXqRSeGovzm_n8ljTmUgik2"
token_cp ='eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'
adda_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkcGthNTQ3MEBnbWFpbC5jb20iLCJhdWQiOiIxNzg2OTYwNSIsImlhdCI6MTc0NDk0NDQ2NCwiaXNzIjoiYWRkYTI0Ny5jb20iLCJuYW1lIjoiZHBrYSIsImVtYWlsIjoiZHBrYTU0NzBAZ21haWwuY29tIiwicGhvbmUiOiI3MzUyNDA0MTc2IiwidXNlcklkIjoiYWRkYS52MS41NzMyNmRmODVkZDkxZDRiNDkxN2FiZDExN2IwN2ZjOCIsImxvZ2luQXBpVmVyc2lvbiI6MX0.0QOuYFMkCEdVmwMVIPeETa6Kxr70zEslWOIAfC_ylhbku76nDcaBoNVvqN4HivWNwlyT0jkUKjWxZ8AbdorMLg"
photologo = 'https://tinypic.host/images/2025/02/07/DeWatermark.ai_1738952933236-1.png' #https://envs.sh/GV0.jpg
photoyt = 'https://tinypic.host/images/2025/03/18/YouTube-Logo.wine.png' #https://envs.sh/GVi.jpg
photocp = 'https://tinypic.host/images/2025/03/28/IMG_20250328_133126.jpg'
photozip = 'https://envs.sh/cD_.jpg'
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.

