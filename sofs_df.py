import pandas as pd
import re

labels = pd.read_csv("sofs_tagging.csv")
labels.head()

with open("sofs_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

pattern = r"\n([A-Z][a-z]+ \d{1,2}, 1847)\n"
parts = re.split(pattern, raw_text)

dates = parts[1::2]
texts = parts[2::2]

text_df = pd.DataFrame({
    "chapter_id": range(len(texts)),
    "date": dates,
    "text": texts
})

df = text_df.merge(labels, on="chapter_id")
df.head()