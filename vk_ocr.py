
import requests, base64

VK_API_KEY = "2wYzyEjRyDExt8QfsSfrx25riWTdZBHtEqktT6ftfcYaDEh1z2ENTx9LfcFxtK"
VK_URL = "https://api.cloud.vk.com/vision/ocr"

def vk_ocr(image_path: str) -> dict:
    with open(image_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()

    payload = {
    "image": img_base64
}

    headers = {
        "Authorization": f"Bearer {VK_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(VK_URL, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()
