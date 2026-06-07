from utils.file_ops import load_words, remove_old
from scripts.build_dictionary import build_dictionary_from_file
from utils.logger import log


if __name__ == "__main__":
    remove_old(["dictionary.py"])
    words = load_words("data/en_words.txt") + load_words("data/en_phrases.txt")
    log("🚀 Starting translation...")
    log(len(words))
    build_dictionary_from_file(words)
