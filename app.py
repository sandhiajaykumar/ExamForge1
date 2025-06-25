from flask import Flask, render_template, request, send_file
from utils.text_extractor import extract_text
from utils.prompts import get_prompt
from utils.pdf_generator import generate_pdf_from_content
import os
import uuid
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
UPLOAD_FOLDER = 'generated_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = genai.GenerativeModel('gemini-1.5-flash')

def call_ai_api(prompt):
    try:
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text
        else:
            print("Empty response from Gemini API.")
            return "Sorry, the AI did not return any content."
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Error generating content."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    file = request.files.get('file')
    feature = request.form.get('feature')
    num_items = request.form.get('num_items', None)

    if not file or file.filename == '':
        return render_template('result.html', content="Error: No file selected.", filename="")
    if not feature:
        return render_template('result.html', content="Error: No feature selected.", filename="")

    text = extract_text(file)
    if "Unsupported file format." in text:
        return render_template('result.html', content=text, filename="")

    prompt = get_prompt(text, feature, num_items=num_items)
    result = call_ai_api(prompt)

    # Metadata fields for Question Paper
    metadata = {
        "college_name": request.form.get("college_name", "").strip(),
        "exam_title": request.form.get("exam_title", "").strip(),
        "subject_name": request.form.get("subject_name", "").strip(),
        "exam_date": request.form.get("exam_date", "").strip()
    }

    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    try:
        generate_pdf_from_content(result, filepath, metadata=metadata if feature == "question_paper" else None)
    except Exception as e:
        print(f"PDF generation error: {e}")
        return render_template('result.html', content=result, filename="")

    return render_template('result.html', content=result, filename=filename)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
