# 📝 Document Extractor Web App

This project is a web-based **Document Extractor** built using **Flask**, which uses **OCR (Optical Character Recognition)** via `pytesseract` to extract important information from images of:

- 🆔 Aadhaar Card  
- 🧾 PAN Card  
- 🏦 Bank Passbook  

It identifies key details such as name, gender, date of birth, account number, IFSC code, and more using **regular expressions**.

---

## 🚀 Features

- Upload document images (`.png`, `.jpg`, etc.)
- Choose document type (Aadhar / PAN / Bank Passbook)
- Extracts:
  - Aadhaar: Name, DOB, Gender, Aadhar Number
  - PAN: Name, DOB, PAN Number, Father's Name
  - Bank Passbook: Name, Account Number, IFSC Code, Bank Name
- Clean and responsive UI using Bootstrap
- Graceful error handling for invalid files

---

## 🛠️ Tech Stack

- 🔹 Python 3.x  
- 🔹 Flask  
- 🔹 pytesseract (OCR)  
- 🔹 BeautifulSoup (optional for parsing)  
- 🔹 Bootstrap (frontend)  
- 🔹 HTML / CSS  

---

## 📂 Folder Structure
```bash
document_extractor/
|
├── static/
│ └── uploads/ # Uploaded images
│
├── templates/
│ └── index.html # Main frontend
│
├── app.py # Flask backend logic, Contains extract_aadhar, extract_pan, extract_bank
├── README.md # Project documentation
```

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/document_extractor.git
cd document_extractor
```

### 2. Install dependencies
pip install flask pillow pytesseract

### 3. Set up Tesseract OCR
Download and install Tesseract from:
👉 https://github.com/tesseract-ocr/tesseract

Update the path in app.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this

### 4. Run the app
python app.py

Visit 👉 http://127.0.0.1:5000/ in your browser.

### 🧪 Sample Usage
1. Upload a scanned Aadhaar card image → Get Name, DOB, Gender, Aadhar Number
2. Upload a PAN card → Extract PAN number & details
3. Upload a bank passbook snapshot → Get IFSC, Account number & Bank name
