from reportlab.pdfgen import canvas

# Output PDF file
output_pdf = "PhishingExample.pdf"

# Create the PDF
c = canvas.Canvas(output_pdf)

# Add text and a styled button-like area
c.drawString(100, 750, "DocuSign")
c.setFont("Helvetica-Bold", 14)
c.drawString(100, 730, "Secure Digital Document Platform")
c.setFont("Helvetica", 12)
c.drawString(100, 710, "ACH-Wire Authorization FOR VERY IMPORTANT ENT CUSTOMER.pdf")
c.setFont("Helvetica", 10)
c.drawString(100, 690, "You have received a document that requires your attention. Please review and sign it at your earliest convenience.")

# Draw a rectangle to simulate a button
c.setFillColorRGB(0.2, 0.6, 1)  # Light blue
c.rect(100, 650, 200, 30, fill=True, stroke=False)
c.setFillColorRGB(1, 1, 1)  # White text
c.setFont("Helvetica-Bold", 12)
c.drawString(120, 660, "Review Document")

# Add a clickable hyperlink to  previous driveby example the rectangle
c.linkURL("https://drivebyviaapi.webflow.io", (100, 650, 300, 680))

# Add disclaimer text
c.setFillColorRGB(0, 0, 0)  # Black text
c.setFont("Helvetica", 8)
c.drawString(100, 620, "Do Not Share This Email")
c.drawString(100, 600, "This email contains a secure link to DocuSign. Please do not share this email or link with others.")

# Save the PDF
c.save()

print(f"PDF created with a phishing-like link: {output_pdf}")
