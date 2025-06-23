from fpdf import FPDF

def generate_pdf_from_content(content, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    lines = content.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)
    
    pdf.output(output_path)
