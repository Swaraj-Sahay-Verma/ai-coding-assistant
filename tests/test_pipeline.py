from extractor.pipeline import extract

with open("datasets/raw/quotes_dataset/page_000001.html", encoding="utf-8") as f:
    html = f.read()

best = extract(html)

print(best)