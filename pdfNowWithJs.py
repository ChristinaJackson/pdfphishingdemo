from pdfrw import PdfReader, PdfWriter, PdfName

# Input and output PDF paths
input_pdf = "IamAPDFWithNoJS.pdf"
output_pdf = "IamAPDFWithJS.pdf"

# JavaScript code
js_code = """
app.alert("Hello! This is a test of JavaScript in a PDF.");
"""

# Read the input PDF
pdf = PdfReader(input_pdf)

# Add JavaScript action
pdf.Root.AA = {PdfName.OpenAction: {PdfName.S: PdfName.JavaScript, PdfName.JS: js_code}}

# Write the output PDF
PdfWriter(output_pdf, trailer=pdf).write()

print(f"PDF created with JavaScript: {output_pdf}")
