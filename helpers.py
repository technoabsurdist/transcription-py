from langchain.document_loaders import YoutubeLoader
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('OPENAI_API_KEY')

client = OpenAI()

def transcription(url: str):
    loader = YoutubeLoader.from_youtube_url(
        url, add_video_info=True
    )
    documents = loader.load()
    print(documents)
    text = [doc.page_content for doc in documents][0]
    metadata = [doc.metadata for doc in documents][0]
    return text, metadata

def generate_summary(text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a short one-paragraph summary of the following text: '{text}'."}
        ]
    )
    return response.choices[0].message.content