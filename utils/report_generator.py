from fpdf import FPDF

def generate_report(file_data, output_path="reports/report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for data in file_data:
        for key, value in data.items():
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
        pdf.cell(200, 10, txt="------------------------", ln=True)

    pdf.output(output_path)
