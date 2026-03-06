import fitz

# step 1 load the pdf

def load_pdf(pdf_path : str) -> str:
    """Extract all text from pdf file"""

    doc = fitz.open(pdf_path)

    full_text = ""
    
    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += f"\n---Page {page_num+1} ---\n{text}"

    doc.close()
    print(f"Loaded pdf--{len(full_text)} characters extracted")

load_pdf(r"1475163596-1-21 (1)-pages.pdf")
