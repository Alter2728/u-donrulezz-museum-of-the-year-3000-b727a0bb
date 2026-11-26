import os

TEXT = "Tiny Metal Password, c.2025. Carried in a pocket, this jagged copy persuaded a house to open; lose it, and the owner slept outside until a stranger was paid to break in legally."

assert 1 <= len(TEXT) <= 200, len(TEXT)
assert "\n" not in TEXT and "\r" not in TEXT

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)

with open(path, encoding="utf-8") as f:
    data = f.read()
assert data == TEXT
assert 1 <= len(data) <= 200
assert "\n" not in data and "\r" not in data
print(f"OK {len(data)} chars: {data}")
