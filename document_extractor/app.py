import os
import pytesseract
import re
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image, UnidentifiedImageError

# Set tesseract path 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Extractor: Aadhar
def extract_aadhar(text):
    aadhar = re.findall(r'\d{4}\s\d{4}\s\d{4}', text)
    dob = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)
    gender = re.findall(r'\bMale\b|\bFemale\b', text, re.IGNORECASE)
    return {
        "Document": "Aadhar",
        "DOB": dob[0] if dob else "Not Found",
        "Gender": gender[0].capitalize() if gender else "Not Found",
        "Aadhar Number": aadhar[0] if aadhar else "Not Found"
    }

# Extractor: PAN
def extract_pan(text):
    pan = re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', text)
    dob = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)
    return {
        "Document": "PAN",
        "DOB": dob[0] if dob else "Not Found",
        "PAN Number": pan[0] if pan else "Not Found"
    }

# Extractor: Bank Passbook
def extract_bank(text):
    account = re.findall(r'\d{11}', text)
    cleaned_text = text.replace('\n', '').replace(' ', '')
    ifsc = re.findall(r'[A-Z]{5}[0-9]{6}', cleaned_text)
    bank = re.findall(r'(State Bank of India|HDFC Bank|ICICI Bank|Bank of Baroda)', text, re.IGNORECASE)
    return {
        "Document": "Bank Passbook",
        "Account Number": account[1] if account else "Not Found",
        "IFSC Code": ifsc[0] if ifsc else "Not Found",
        "Bank": bank[0].title() if bank else "Not Found"
    }

# Route
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None

    if request.method == 'POST':
        file = request.files['file']
        doc_type = request.form['doc_type']

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Try opening the image
                img = Image.open(filepath)
                text = pytesseract.image_to_string(img)

                # Document type based extraction
                if doc_type == 'aadhar':
                    result = extract_aadhar(text)
                elif doc_type == 'pan':
                    result = extract_pan(text)
                elif doc_type == 'bank':
                    result = extract_bank(text)

            except UnidentifiedImageError:
                error_message = "❌ Oops! This doesn't seem to be a valid image file (e.g., PDF uploaded instead of JPG/PNG)."
            except Exception as e:
                error_message = f"⚠️ Unexpected error: {str(e)}"

    return render_template('index.html', result=result, error=error_message)

# Run
if __name__ == '__main__':
    app.run(debug=True)
