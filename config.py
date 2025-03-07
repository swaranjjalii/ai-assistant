from dotenv import load_dotenv
import os

load_dotenv()
HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
