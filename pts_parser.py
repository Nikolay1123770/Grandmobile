
import re
from vk_ocr import vk_ocr

def num(text):
    return ''.join(re.findall(r'\d', text))

def level(text):
    for i in ['3','2','1']:
        if i in text:
            return f"{i} ур."
    return "0 ур."

def parse_pts(path):
    data = vk_ocr(path)
    blocks = data.get("result", {}).get("text_detection", [])
    text = " ".join(b.get("text", "") for b in blocks)

    return {
        "pts": num(text),
        "auto": "—",
        "price": num(text),
        "mileage": num(text),
        "owners": num(text),
        "plate": "—",
        "engine": level(text),
        "turbo": level(text),
        "hydro": "Есть" if "ГИДРО" in text.upper() else "Нет",
        "chip": level(text),
        "brakes": level(text),
        "nitro": level(text),
        "trans": level(text),
        "tires": level(text),
        "susp": level(text),
    }
