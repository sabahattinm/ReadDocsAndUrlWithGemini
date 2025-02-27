import requests
from bs4 import BeautifulSoup
import fitz
import os


def read_from_url(url):
    """URL'den içeriği okur (HTML, PDF, TXT destekler)."""
    if not url:
        return ""

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "").lower()

        if "text/html" in content_type:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text(separator="\n", strip=True)

        elif "application/pdf" in content_type:
            with open("temp.pdf", "wb") as f:
                f.write(response.content)
            doc = fitz.open("temp.pdf")
            text = "\n".join([page.get_text() for page in doc])
            os.remove("temp.pdf")
            return text

        elif "text/plain" in content_type:
            return response.text

        else:
            return "Bu URL’deki dosya formatı desteklenmiyor!"

    except requests.RequestException as e:
        return f"URL’den içerik alınamadı: {str(e)}"