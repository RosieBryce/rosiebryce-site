# Splice the brand's embedded fonts into index.src.html -> index.html
import re, pathlib
here = pathlib.Path(__file__).parent
brand = (here / "../../Consultancy/brand/brand.html").read_text(encoding="utf-8")
faces = re.findall(r"@font-face\{[^}]*\}", brand)
assert len(faces) == 4, len(faces)
src = (here / "index.src.html").read_text(encoding="utf-8")
assert "/* FONTS */" in src
(here / "index.html").write_text(src.replace("/* FONTS */", "\n".join(faces)), encoding="utf-8")
print("index.html written")
