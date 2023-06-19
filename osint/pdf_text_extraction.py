import PyPDF2

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

def save_results(file_path, text):
    with open(file_path.replace('.pdf', '.txt'), 'w') as f:
        f.write(text)

def main():
    file_path = input("Enter the path of the PDF file: ")
    text = extract_text_from_pdf(file_path)
    save_results(file_path, text)

if __name__ == "__main__":
    main()
