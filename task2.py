import pandas as pd
from fpdf import FPDF

# Load CSV data
df = pd.read_csv('student_data.csv')

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Student Marks Report", ln=1, align='C')

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, 'Name', border=1)
pdf.cell(60, 10, 'Subject', border=1)
pdf.cell(30, 10, 'Marks', border=1)
pdf.ln()

# Table Data
pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(60, 10, row['Name'], border=1)
    pdf.cell(60, 10, row['Subject'], border=1)
    pdf.cell(30, 10, str(row['Marks']), border=1)
    pdf.ln()

# Save PDF
pdf.output("student_report.pdf")
print("PDF report created successfully!")
