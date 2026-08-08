# 生成画像をWeb用に最適化する（JPEG変換・最大1920px・品質85）
import os
from PIL import Image

SRC = r"D:\たぶんごみ\ClaudeCODE\web\draft-b\assets\img\raw"
DST = r"D:\たぶんごみ\ClaudeCODE\web\draft-b\assets\img"
MAX_W = 1920

for name in os.listdir(SRC):
    if not name.endswith(".png"):
        continue
    path = os.path.join(SRC, name)
    img = Image.open(path).convert("RGB")
    # 横幅が大きすぎる場合は縮小
    if img.width > MAX_W:
        ratio = MAX_W / img.width
        img = img.resize((MAX_W, int(img.height * ratio)), Image.LANCZOS)
    out = os.path.join(DST, name.replace(".png", ".jpg"))
    img.save(out, "JPEG", quality=85, optimize=True)
    print(f"{name} -> {os.path.basename(out)} ({img.width}x{img.height}, {os.path.getsize(out)//1024}KB)")
