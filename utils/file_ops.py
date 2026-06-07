import os


def remove_last_bracket(path: str):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if lines and lines[-1].strip() == "]":
        # убираем последнюю строку
        lines = lines[:-1]
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)


def load_words(path="en_words.txt"):
    words = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip()
            if w:
                words.append(w)
    return words


def remove_old(files_to_remove):
    open("train.log", "w").close()
    for f in files_to_remove:
        if os.path.exists(f):
            os.remove(f)
            print(f"🗑 Deleted: {f}")
