from pdfrw import PdfReader, PdfWriter, PdfDict, PdfName, PdfObject

# Input and output PDF paths
input_pdf = "IamAPDFWithNoJS.pdf"  # Make sure this file exists and has enough space
output_pdf = "IamAPDFWithVisibleButton.pdf"

# JavaScript code to trigger on button click
js_code = """
app.alert("This is a test of JavaScript triggered by a visible button!");
"""

# Read the input PDF
pdf = PdfReader(input_pdf)

# Create a visible button
button = PdfDict(
    FT=PdfName.Btn,  # Field type: Button
    T="VisibleButton",  # Button name
    Ff=0,  # Flags (visible, interactive)
    Rect=[150, 600, 300, 650],  # Position and size: [x1, y1, x2, y2]
    DA="/Helvetica 16 Tf 1 0 0 rg",  # Default appearance: Helvetica, size 16, red text
    MK=PdfDict(BC=[1, 0, 0], BG=[0.9, 0.9, 0.9]),  # Border (red) and background (light gray)
    AA=PdfDict(U=PdfDict(S=PdfName.JavaScript, JS=js_code))  # Add JavaScript to mouse-up action
)

# Ensure annotations exist and add the button to the first page
if not hasattr(pdf.pages[0], 'Annots') or pdf.pages[0].Annots is None:
    pdf.pages[0].Annots = []
pdf.pages[0].Annots.append(button)

# Write the output PDF
PdfWriter(output_pdf, trailer=pdf).write()

print(f"PDF created with a visible button: {output_pdf}")
