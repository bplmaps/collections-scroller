import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Paths
json_path = os.path.join("..", "src", "assets", "collections.json")
output_dir = os.path.join("..", "public", "thumbnails")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load JSON data
with open(json_path, 'r', encoding='utf-8') as f:
    collections = json.load(f)

# Helper function to download one image
def download_image(item):
    img_id = item.get("exemplary_image_ssi")
    if not img_id:
        return "Skipped item with no 'exemplary_image_ssi'"

    url = f"https://bpldcassets.blob.core.windows.net/derivatives/images/{img_id}/image_thumbnail_300.jpg"
    safe_filename = img_id.replace(":", "__") + ".jpg"
    output_path = os.path.join(output_dir, safe_filename)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(output_path, 'wb') as img_file:
            img_file.write(response.content)
        return f"Downloaded and saved: {safe_filename}"
    except requests.RequestException as e:
        return f"Failed to download {url}: {e}"

# Use ThreadPoolExecutor to download in parallel
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_image, item) for item in collections]
    for future in as_completed(futures):
        print(future.result())
