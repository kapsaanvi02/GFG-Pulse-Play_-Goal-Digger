import qrcode

# Function to create QR code
def generate_qr(data, filename='dialysis_data_qr.png'):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls error correction
        box_size=10,  # Controls the size of each 'box' of the QR code
        border=4,  # Thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

# Example dialysis data
dialysis_data = """
Creatinine: 5.2 mg/dL
BUN: 50 mg/dL
Potassium: 6.0 mEq/L
Sodium: 132 mEq/L
Calcium: 8.0 mg/dL
Dialysis needed: Yes
Frequency: Every 3 days
"""

# Generate QR code for dialysis data
generate_qr(dialysis_data)