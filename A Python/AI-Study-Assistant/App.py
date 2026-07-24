from flask import Flask, request, jsonify
import PyPDF2
from ai_engine import generate_summary, generate_flashcards, generate_quiz

app = Flask(__name__)

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']

    text = extract_text_from_pdf(file)

    summary = generate_summary(text)
    flashcards = generate_flashcards(text)
    quiz = generate_quiz(text)

    return jsonify({
        "summary": summary,
        "flashcards": flashcards,
        "quiz": quiz
    })


if __name__ == "__main__":
    app.run(debug=True)