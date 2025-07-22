from utils.pdf_utils import download_pdf, extract_chunks

def pdf_agent(paper):
    pdf_url = paper.pdf_url
    filename = pdf_url.split("/")[-1]
    download_pdf(pdf_url, f"/tmp/{filename}")
    chunks = extract_chunks(f"/tmp/{filename}")
    return chunks 