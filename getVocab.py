import json
import unicodedata
data = {}


def normalize_word(word: str) -> str:
    word = word.lower().strip()
    word = unicodedata.normalize("NFD", word)
    word = "".join(ch for ch in word if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", word)


def is_affix(text: str) -> bool:
    words = text.split()
    return (
        len(words) == 1 and
        words[0].startswith("-")
    )


with open(
    r"E:\Git\game-ai-translator\game-ai-core\parser\enwiktionary.jsonl",
    "r",
    encoding="utf-8",
) as f:
    for line in f:
        item = json.loads(line)
        word = item.get("word")
        senses = item.get("senses", [])
        for sense in senses:
            translations = sense.get("translations", [])
            for t in translations:
                if t.get("lang") == "Ukrainian":
                    ua = t.get("word")
                    if word and ua:
                        word = word.lower().strip()
                        ua = ua.lower().strip()
                        if word not in data:
                            if not is_affix(ua):
                                data[word] = normalize_word(ua)
with open("dictionary.py", "w", encoding="utf-8") as f:
    f.write("data = [\n")
    for en, ua in sorted(data.items(), key=lambda x: x[0]):
        f.write(f'    ("{en}", "{ua}"),\n')
    f.write("]\n")
