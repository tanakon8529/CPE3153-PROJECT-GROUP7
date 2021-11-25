from dotenv import load_dotenv
from pathlib import Path
import os

# command build and run docker
"""
docker build -t cpe3153 .

# option 1
docker run -d --name g7 -p 8080:8080 cpe3153
# option 2 (ngrok-domain)
docker run --rm -it --link 0.0.0.0 --net ngrok shkoliar/ngrok ngrok http 0.0.0.0:80
"""

load_dotenv(verbose=True)
#cp .env.example .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
LOCAL_REDIS_URL = os.getenv('LOCAL_REDIS_URL')