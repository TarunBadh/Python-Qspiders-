import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def generate_summary(text):
    prompt = "Summarize the following notes in simple language:\n" + text
    response = model.generate_content(prompt)
    return response.text


def generate_flashcards(text):
    prompt = "Create 5 flashcards from this text:\n" + text
    response = model.generate_content(prompt)
    return response.text


def generate_quiz(text):
    prompt = "Generate 5 quiz questions with answers:\n" + text
    response = model.generate_content(prompt)
    return response.text