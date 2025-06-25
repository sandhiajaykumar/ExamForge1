from fpdf import FPDF

def generate_pdf_from_content(content, output_path, metadata=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set default font
    pdf.set_font("Arial", size=12)

    # Optional: Add metadata heading if feature is "question_paper"
    if metadata:
        pdf.set_font("Arial", "B", 14)
        if metadata.get("college_name"):
            pdf.cell(0, 10, metadata["college_name"], ln=True, align='C')
        if metadata.get("exam_title"):
            pdf.cell(0, 10, metadata["exam_title"], ln=True, align='C')
        if metadata.get("subject_name"):
            pdf.cell(0, 10, f"Subject: {metadata['subject_name']}", ln=True, align='L')
        if metadata.get("exam_date"):
            pdf.cell(0, 10, f"Date: {metadata['exam_date']}", ln=True, align='L')
        pdf.ln(10)  # Add spacing after header
        pdf.set_font("Arial", size=12)

    # Add content line by line
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, txt=line, align='L')

    pdf.output(output_path)
