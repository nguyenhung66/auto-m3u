from datetime import datetime

playlist = f"""#EXTM3U
# Playlist được tạo tự động
# Cập nhật: {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")}
"""

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(playlist)

print("Đã tạo playlist.m3u")
