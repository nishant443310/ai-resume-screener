import fitz  

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
    return text.strip()


if __name__ == "__main__":
    text = extract_text_from_pdf("Sample_resume.pdf")  # Make sure this file exists
    print(text[:500])
