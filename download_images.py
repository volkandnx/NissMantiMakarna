import os
import re
import urllib.request
import codecs
import string

img_dir = "d:\\niss\\images"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

with codecs.open("d:\\niss\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find all image paths currently in the HTML
pattern = re.compile(r'<img src="(https?://[^"]+)" alt="([^"]+)"')

matches = pattern.findall(html)

def safe_filename(name):
    # allow turkish chars and ascii
    valid_chars = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789çğıöşüÇĞİÖŞÜ"
    filename = ''.join(c for c in name if c in valid_chars)
    filename = filename.replace(' ', '_').lower()
    return filename

downloaded = {}

# We might see images outside menu too, let's keep track
for url, alt_text in matches:
    if url in downloaded:
        continue
    
    clean_name = safe_filename(alt_text)
    if not clean_name: clean_name = "image"
    
    ext = ".jpg" 
    if url.lower().endswith(".png"): ext = ".png"
    elif url.lower().endswith(".webp"): ext = ".webp"
    
    filename = f"{clean_name}{ext}"
    filepath = os.path.join(img_dir, filename)
    local_url = f"images/{filename}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            with open(filepath, 'wb') as out_file:
                out_file.write(data)
                
        downloaded[url] = local_url
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Replace URLs in HTML
new_html = html
for url, local_path in downloaded.items():
    new_html = new_html.replace(url, local_path)

with codecs.open("d:\\niss\\index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("HTML updated with local image paths.")
