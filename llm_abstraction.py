import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import HUGGING_FACE_API_KEY
from transformers import pipeline

class LLMHandler:
    def __init__(self, api_key=HUGGING_FACE_API_KEY):
        self.api_key = api_key

    def load_model(self, model_name="gpt2"):
        self.model = pipeline("text-generation", model=model_name)

    def generate_text(self, prompt, max_length=50):
        return self.model(prompt, max_length=max_length)[0]['generated_text']


