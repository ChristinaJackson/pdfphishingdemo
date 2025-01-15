from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName
from reportlab.pdfgen import canvas

# Step 1: Create a base PDF with reportlab
base_pdf = "base.pdf"
output_pdf = "IamAPDFWithVisibleButton.pdf"

# Create a blank PDF with some content
c = canvas.Canvas(base_pdf)
c.drawString(200, 750, "This PDF contains a button.")  # Text on the PDF
c.save()

# Step 2: Add a visible button with JavaScript
# JavaScript code to trigger on button click
js_code = """
app.alert("Hello! This button works!");
"""

# Read the base PDF
pdf = PdfReader(base_pdf)

# Create a button annotation
button = PdfDict(
    FT=PdfName.Btn,  # Field type: Button
    T="TestButton",  # Button name
    Ff=0,  # Flags: Visible and interactive
    Rect=[150, 650, 250, 700],  # Position and size: [x1, y1, x2, y2]
    DA="/Helvetica 12 Tf 0 0 1 rg",  # Default appearance: Helvetica, size 12, blue text
    MK=PdfDict(BC=[0, 0, 1], BG=[0.8, 0.8, 0.8]),  # Border and background color
    AA=PdfDict(U=PdfDict(S=PdfName.JavaScript, JS=js_code))  # Add JavaScript to mouse-up action
)

# Ensure annotations exist and add the button to the first page
if not hasattr(pdf.pages[0], 'Annots') or pdf.pages[0].Annots is None:
    pdf.pages[0].Annots = []
pdf.pages[0].Annots.append(button)

# Step 3: Save the output PDF
PdfWriter(output_pdf, trailer=pdf).write()

print(f"PDF created with a visible button: {output_pdf}")
