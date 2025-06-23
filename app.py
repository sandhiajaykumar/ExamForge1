from flask import Flask, render_template, request, send_file
from utils.text_extractor import extract_text
from utils.prompts import get_prompt
from utils.pdf_generator import generate_pdf_from_content  # ✅ Import PDF generator
import os
import uuid
from dotenv import load_dotenv

# Import the Google Generative AI library
import google.generativeai as genai

# Load the Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

# Folder to save generated files
UPLOAD_FOLDER = 'generated_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to talk to Gemini API
def call_ai_api(prompt):
    try:
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text
        else:
            print(f"Gemini API returned an empty response for prompt: {prompt}")
            return "Sorry, the AI did not return any content for that request."
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return "Oops! EduGenie ran into a problem generating content. Please try again with different input or feature."


# Homepage
@app.route('/')
def index():
    return render_template('index.html')


# Generate Content
@app.route('/generate', methods=['POST'])
def generate():
    file = request.files.get('file')
    feature = request.form.get('feature')
    num_items = request.form.get('num_items')

    if not file or file.filename == '':
        return render_template('result.html', content="Error: No file selected.", filename="")
    if not feature:
        return render_template('result.html', content="Error: No feature selected.", filename="")

    text = extract_text(file)

    if "Unsupported file format." in text:
        return render_template('result.html', content=text, filename="")

    prompt = get_prompt(text, feature, num_items=num_items)
    result = call_ai_api(prompt)

    # ✅ Generate and save PDF file instead of .txt
    pdf_filename = f"{uuid.uuid4()}.pdf"
    pdf_filepath = os.path.join(UPLOAD_FOLDER, pdf_filename)

    try:
        generate_pdf_from_content(result, pdf_filepath)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return render_template('result.html', content=result, filename="")

    return render_template('result.html', content=result, filename=pdf_filename)


# Download PDF
@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)


# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)
