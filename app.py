from flask import Flask, request, jsonify, render_template
import requests
import pdfplumber
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tempfile
import os

app = Flask(__name__)

def is_valid_pdf_link(url):
    return url.lower().endswith('.pdf')

def extract_pdf_links(page_url):
    try:
        resp = requests.get(page_url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(page_url, href)
            if is_valid_pdf_link(full_url):
                links.append(full_url)
        return links
    except Exception as e:
        return []

def extract_text_from_pdf(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resp.content)
            tmp.flush()
            text = ""
            with pdfplumber.open(tmp.name) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        os.unlink(tmp.name)
        return text.strip()
    except Exception as e:
        return f"[Error extracting PDF: {str(e)}]"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_pdfs():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "No URL provided."}), 400

    # Validate URL schema
    try:
        parsed = urlparse(url)
        if not parsed.scheme.startswith('http'):
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid URL format."}), 400

    pdf_links = extract_pdf_links(url)
    if not pdf_links:
        return jsonify({"error": "No PDFs found on the page."}), 404

    results = []
    for link in pdf_links:
        text = extract_text_from_pdf(link)
        results.append({"pdf_url": link, "text": text[:1500] + ("..." if len(text) > 1500 else "")})

    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
