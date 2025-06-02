from sqlalchemy.orm import Session
import app.crud as crud
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient
import json

load_dotenv()

client = InferenceClient(
    provider="novita",
    api_key=os.getenv("API_KEY"),
)


def perform_translation(task: int, text: str, languages: list, db: Session):
    translations = {}
    lans = ','.join(languages)
    try:
        response = client.chat.completions.create(model="deepseek-ai/DeepSeek-V3-0324",
        messages=[ 
            {"role":"system", "content": f"Just reply with the translated text into {lans} separated by '::' and nothing else!"},
            {"role": "user", "content": text}
        ],
        max_tokens=100)
        translations = response.choices[0].message.content.strip()
        translations = translations.split('::')
        translations = {languages[i]:translations[i] for i in range(len(languages))}
        print(f"-----------------------\n{translations}\n----------------------")
    except Exception as e:
        print(f"Error Translating!: {e}")
        translations = f"Error: {e}"
        
    crud.update_translation_task(db, task, translations)