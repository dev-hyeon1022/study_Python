# https://ocr.space/OCRAPI
import requests
import json

url = "https://api.ocr.space/parse/imageurl?apikey=K81659339888957&url=https://hanasia.com/_sys/_upload/image/201906/12/15603238171847.jpg&language=kor&isOverlayRequired=true"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data['ParsedResults'][0]['ParsedText'])

# print(json.dumps(data, ensure_ascii=False, indent=2))