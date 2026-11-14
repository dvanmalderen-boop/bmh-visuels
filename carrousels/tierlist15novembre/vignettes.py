# -*- coding: utf-8 -*-
"""Mise au point des vignettes carrees : on regarde, on corrige, on ne devine pas."""
import os, sys
from PIL import Image

SCENES = "/home/claude/tierlist/scenes"

# cx, cy = ou vit le flacon dans la scene, en fraction. fen = part de la
# largeur de la scene que la fenetre carree prend.
CADRE = {
 "6290360590585": (0.68, 0.45, 0.70),  # Maison Alhambra Infini Elixir
 "6290361916896": (0.68, 0.45, 0.70),  # Arabiyat Sugar Mango Affogato
 "6298042000926": (0.68, 0.45, 0.70),  # French Avenue Vulcan Baie
 "5061042410214": (0.68, 0.45, 0.70),  # Ayat Jumrah Coffee
 "6294015163513": (0.68, 0.45, 0.70),  # Armaf CDN Urban Man Elixir
 "6291100130979": (0.63, 0.45, 0.70),  # Al Haramain Royal Musk
 "6290171072829": (0.60, 0.45, 0.70),  # Zimaya Treasure
 "6294879841183": (0.68, 0.45, 0.70),  # Paris Corner Khair Felicity
 "0614514204092": (0.68, 0.45, 0.70),  # Rasasi La Yuqawam Jasmine Wisp
 "6298141926707": (0.65, 0.45, 0.70),  # Emir Voux Violette
 "6290171075288": (0.65, 0.45, 0.70),  # Afnan 9pm Rebel
}

def vignette(ean, cote=320):
    im = Image.open(os.path.join(SCENES, ean + "c.jpg")).convert("RGB")
    cx, cy, fen = CADRE[ean]
    f = int(im.width * fen)
    x = int(cx * im.width - f / 2)
    y = int(cy * im.height - f / 2)
    x = max(0, min(x, im.width - f))
    y = max(0, min(y, im.height - f))
    return im.crop((x, y, x + f, y + f)).resize((cote, cote), Image.LANCZOS)

if __name__ == "__main__":
    eans = list(CADRE)
    c = 320
    pl = Image.new("RGB", (c * 6, c * 2), (240, 228, 206))
    for i, e in enumerate(eans):
        pl.paste(vignette(e, c), ((i % 6) * c, (i // 6) * c))
    pl.save("/tmp/claude-0/planche-vignettes.jpg", quality=88)
    print("ok", eans)
