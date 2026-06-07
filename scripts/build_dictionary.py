import time
import os
import json
from models.translator import translate_batch
from utils.text_ops import replace_quotes,  match_case

OUTPUT_FILE = "dictionary.py"


def build_dictionary_from_file(words, batch_size=128):
    print(f"🚀 Translating {len(words)} words...")
    start = time.time()
    saved = 0
    first_line = None
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        if first_line != "data = [":
            f.write("data = [\n")
        for i in range(0, len(words), batch_size):
            batch = words[i:i + batch_size]
            try:
                translations = translate_batch(batch)
            except Exception as e:
                print("❌ batch error:", e)
                continue
            for idx in range(len(batch)):
                en = batch[idx]
                uk = translations[idx]
                if not uk:
                    continue
                uk = match_case(en, uk)
                en_safe = json.dumps(en, ensure_ascii=False)
                uk_safe = json.dumps(replace_quotes(uk), ensure_ascii=False)
                f.write(f"    ({en_safe}, {uk_safe}),\n")
                saved += 1
            if (i // batch_size) % 10 == 0:
                print(f"🧾 progress={i}/{len(words)} | saved={saved}")
        f.write("]\n")
    print(f"✅ DONE: {saved} pairs in {time.time() - start:.2f}s")
