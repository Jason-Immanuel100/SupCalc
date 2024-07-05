from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

# Define the file path for the PDF
file_path = "Treatment_Calculation_for_kV_Template.pdf"

# Create a SimpleDocTemplate object with A4 page size
doc = SimpleDocTemplate(file_path, pagesize=A4)

# Define styles
styles = getSampleStyleSheet()
style_normal = styles['Normal']
style_heading = styles['Heading1']
style_bold = ParagraphStyle(name='Bold', parent=style_normal, fontName='Helvetica-Bold')

# Content for the document
content = []

# Title
title = Paragraph("Treatment Calculation for kV", style_heading)
content.append(title)
content.append(Spacer(1, 12))

# Filler and Date Information
filler_date_info = [
    ["[FILLER]", "[FILLER]", "[Date]", "[DR NAME]"],
    ["[FILLER]"],
    ["[Location 1]"],
    ["[Town/ City]"],
    ["[Post code]"]
]
for line in filler_date_info:
    p = Paragraph(" ".join(line), style_normal)
    content.append(p)
    content.append(Spacer(1, 12))

# Fields information
fields_info = [
    ("Field ID:", "Field Name:"),
    ("Treatment Unit:", "Technique:"),
    ("Energy:", "Shielding:"),
    ("Build UP/Bolus:", "FSD:"),
    ("Applicator:", "Filter:", "Field Size (Width X Length):", "PB cut-out:"),
    ("Eq.Square/Circle Diameter:"),
    ("Applicator:"),
    ("Leaded Area Output:"),
    ("Inverse Square Law:"),
    ("Tumour Dose%/cGy:"),
    ("Monitor Units:")
]
for field in fields_info:
    p = Paragraph(" ".join(field), style_normal)
    content.append(p)
    content.append(Spacer(1, 12))

# Calculation checks
calc_checks = [
    "Calculation 1st Check initials",
    "Calculation 2nd Check initials",
    "2nd check Reverse Calculations please check document No: REF-49",
    "Calculation 3rd Check initials"
]
for check in calc_checks:
    p = Paragraph(check, style_normal)
    content.append(p)
    content.append(Spacer(1, 12))

# Build the PDF
doc.build(content)

print(f"PDF generated successfully and saved to {file_path}")
