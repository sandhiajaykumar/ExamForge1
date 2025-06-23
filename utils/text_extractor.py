# utils/text_extractor.py
import pdfplumber
import docx
import io

def extract_text(file):
    file.seek(0)
    file_content = io.BytesIO(file.read())

    if file.filename.endswith('.pdf'):
        try:
            with pdfplumber.open(file_content) as pdf:
                return "\n".join([page.extract_text() or "" for page in pdf.pages])
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return "Error: Could not read PDF file. It might be corrupted or an unsupported PDF type."
    elif file.filename.endswith('.docx'):
        try:
            doc = docx.Document(file_content)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            print(f"Error reading DOCX: {e}")
            return "Error: Could not read DOCX file. It might be corrupted or an unsupported DOCX type."
    elif file.filename.endswith('.txt'): # NEW: Handle plain text files
        try:
            # For text files, we just need to read the content directly
            # Decode with utf-8, which is common for text files.
            return file_content.read().decode('utf-8')
        except Exception as e:
            print(f"Error reading TXT: {e}")
            return "Error: Could not read TXT file. It might be corrupted or an unsupported encoding."
    else:
        return "Unsupported file format. Please upload a .pdf, .docx, or .txt file."