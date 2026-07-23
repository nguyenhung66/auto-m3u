import json
import requests
from bs4 import BeautifulSoup

URL = "https://phaohoa1.live/"

r = requests.get(URL, timeout=20)
r.raise_for_status()

soup = BeautifulSoup(r.text, "lxml")

matches = []

# TODO:
# Tìm các phần tử HTML chứa danh sách trận đấu công khai
# rồi thêm vào matches dưới dạng:
# {
#   "home": "...",
#   "away": "...",
#   "time": "...",
#   "league": "..."
# }

with open("matches.json", "w", encoding="utf-8") as f:
    json.dump(matches, f, ensure_ascii=False, indent=2)

print(f"Saved {len(matches)} matches")
