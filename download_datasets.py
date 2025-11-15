import os
import requests

def download_file(url, dest_path):
    if not os.path.exists(dest_path):
        print(f"Downloading from {url}...")
        r = requests.get(url, stream=True)
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded to {dest_path}")
    else:
        print(f"File already exists: {dest_path}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # Sample dataset links (TextOCR and IAM samples or placeholders)
    sample_urls = {
        "TextOCR_sample": "https://github.com/google-research-datasets/textocr/raw/master/sample.jpg",
        "IAM_sample": "https://fki.tic.heia-fr.ch/static/img/a01-000u.png"
    }

    for name, url in sample_urls.items():
        download_file(url, f"data/{name}.jpg")