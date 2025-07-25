import fitz  # PyMuPDF

def download_pdf(url, out_path):
    import requests
    resp = requests.get(url)
    with open(out_path, "wb") as f:
        f.write(resp.content)

def extract_chunks(pdf_path, chunk_size=1000):
    print(f"\nExtracting chunks from {pdf_path} \n")
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    return [text[i : i+chunk_size] for i in range(0, len(text), chunk_size)] 
