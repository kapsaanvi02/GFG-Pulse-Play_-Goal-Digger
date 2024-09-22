import re
import PyPDF2

# Dialysis thresholds
DIALYSIS_THRESHOLDS = {
    "creatinine": 2.0,  # mg/dL
    "BUN": 50,          # mg/dL
    "potassium": 5.5,   # mEq/L
    "sodium": 135,      # mEq/L
    "calcium": 8.5,     # mg/dL
    "pH": 7.0           # Blood pH
}

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""  # Handle cases where extract_text may return None
        return text

def parse_medical_values(text):
    """Parse medical values from extracted text."""
    data = {
        "creatinine": None,
        "BUN": None,
        "potassium": None,
        "sodium": None,
        "calcium": None,
        "pH": None
    }

    # Search for values in text
    match = re.search(r'creatinine\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['creatinine'] = float(match.group(1))

    match = re.search(r'BUN\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['BUN'] = float(match.group(1))

    match = re.search(r'potassium\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['potassium'] = float(match.group(1))

    match = re.search(r'sodium\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['sodium'] = float(match.group(1))

    match = re.search(r'calcium\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['calcium'] = float(match.group(1))

    match = re.search(r'pH\s*:\s*([\d\.]+)', text, re.IGNORECASE)
    if match:
        data['pH'] = float(match.group(1))

    return data

def check_dialysis_need(medical_data):
    """Check if dialysis is needed based on medical data."""
    dialysis_needed = False
    for key, value in medical_data.items():
        if value is not None:
            if value > DIALYSIS_THRESHOLDS[key]:
                dialysis_needed = True
                print(f"{key.capitalize()} is high: {value}, dialysis may be needed.")
            else:
                print(f"{key.capitalize()} is within normal range: {value}.")
    return dialysis_needed

def main(pdf_path):
    """Main function to scan a PDF and determine dialysis need."""
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    
    print("Parsing medical values...")
    medical_data = parse_medical_values(text)
    
    print("Analyzing results...")
    if check_dialysis_need(medical_data):
        print("ECG Required")
    else:
        print("No ECG Required.")

# Set the PDF path to the specified file
pdf_path = r"C:\Users\saanvi\Desktop\ECG-Sample-Report-1.pdf"
main(pdf_path)
