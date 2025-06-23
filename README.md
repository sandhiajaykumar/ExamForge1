
# 📘 EduGenie – Your Smart Educational Content Generator 🧙‍♂️

EduGenie is an intelligent web application designed to empower students and educators by transforming raw educational content (from PDF, DOCX, or TXT files) into a variety of valuable study materials. Leveraging the power of Google's Gemini AI, EduGenie streamlines the process of creating multiple-choice questions, assignment prompts, project ideas, concise summaries, and flashcards.

---

## ✨ Features

- **File Uploads:** Upload PDF, DOCX, and TXT documents.
- **Intelligent Content Generation:**
  - **MCQ Generator** – Create multiple-choice questions with options and correct answers.
  - **Assignment Generator** – Long-answer academic questions.
  - **Project Ideas Generator** – Innovative project ideas.
  - **Summarizer & Flashcards/Quiz** – Condensed notes and revision material.
  - **Question Paper Creator** – Auto-generates a mixed-format question paper.
  - **Simple Summarizer** – Quick summary tool.
- **Dynamic Quantity Control:** Choose how many questions or ideas to generate.
- **Downloadable Output:** Download generated content as a `.txt` file.
- **Responsive UI:** Clean and mobile-friendly interface using Flask + Bootstrap + CSS.

---

## 🚀 Technologies Used

### 🔹 Backend
- Python 3.8+
- Flask (Web framework)
- Google Generative AI SDK (Gemini Pro API)
- `pdfplumber` (PDF text extraction)
- `python-docx` (DOCX text extraction)
- `python-dotenv` (Environment management)
- `gunicorn` (Production WSGI server)

### 🔹 Frontend
- HTML5, CSS3 (with animated background)
- Bootstrap 5
- JavaScript
- Font Awesome (icons)

---

## 💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/EduGenie.git
cd EduGenie
````

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you haven’t generated `requirements.txt` yet, use:
>
> ```bash
> pip install flask python-docx pdfplumber google-generativeai python-dotenv gunicorn
> pip freeze > requirements.txt
> ```

### 5. Get Your Google Gemini API Key

* Go to [Google AI Studio](https://makersuite.google.com/)
* Log in → Create API key → Copy it

### 6. Configure Environment Variables

Create a `.env` file in your project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ Make sure `.env` is added to `.gitignore`.

### 7. Run the Application

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Live Demo on Render

🟢 Live App: [https://edugenie-w29b.onrender.com](https://edugenie-w29b.onrender.com)

---

## ☁️ Deployment on Render

### 1. Ensure `.gitignore` Includes:

```
venv/
__pycache__/
*.pyc
.env
generated_files/
.vscode/
.DS_Store
Thumbs.db
```

### 2. Add Required Files

**Procfile**

```
web: gunicorn app:app
```

Ensure `gunicorn` is added in `requirements.txt`.

### 3. Push to GitHub

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 4. Deploy via Render

* Go to [Render.com](https://render.com)
* Click **"New Web Service"**
* Connect your GitHub repo
* Fill out:

  * **Name:** edugenie
  * **Branch:** main
  * **Build Command:** `pip install -r requirements.txt`
  * **Start Command:** `gunicorn app:app`
  * **Environment Variable:**

    * Key: `GEMINI_API_KEY`
    * Value: `your-api-key`
* Click **"Create Web Service"**

Render will deploy and give you a public URL. Done! ✅

---

## 💡 Usage

1. **Upload File:** Choose a `.pdf`, `.docx`, or `.txt` file.
2. **Select Feature:** Click on the content type to generate.
3. **Set Quantity (if needed):** Input number of questions/ideas.
4. **Generate:** Click “Generate Content”.
5. **View & Download:** See results and download as `.txt`.
6. **Repeat or Home:** Click to generate more or go back.

---

## ❤️ Contributing

Contributions are welcome! Fork the repo, make improvements, and submit a pull request.

---
