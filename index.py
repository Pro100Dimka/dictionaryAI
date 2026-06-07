# from getVocab import data


# with open("dictionary.py", "w", encoding="utf-8") as f:
#     f.write("data = [\n")
#     for en, uk in sorted(data.items(), key=lambda x: x[0]):
#         uk = unicodedata.normalize("NFC", uk)
#         f.write(f'    ("{en}", "{uk}"),\n')
#     for en, uk in train_pairs:
#         en = clean_sentence(en, "en").replace('"', '\\"')
#         uk = clean_sentence(uk, "uk").replace('"', '\\"')
#         if (
#             en == uk
#             or not is_good_ukrainian(uk)
#             or looks_broken(uk)
#             or not length_ratio_ok(en, uk)
#             or text_quality(en) < 0.5
#             or text_quality(uk) < 0.5
#         ):
#             continue
#         f.write(f'    ("{en}", "{uk}"),\n')
#     f.write("]\n")
#     f.write("val_data = [\n")
#     for en, uk in test_pairs:
#         en = clean_sentence(en, "en").replace('"', '\\"')
#         uk = clean_sentence(uk, "uk").replace('"', '\\"')
#         if (
#             en == uk
#             or not is_good_ukrainian(uk)
#             or looks_broken(uk)
#             or not length_ratio_ok(en, uk)
#             or text_quality(en) < 0.5
#             or text_quality(uk) < 0.5
#         ):
#             continue
#         f.write(f'    ("{en}", "{uk}"),\n')
#     f.write("]\n")
# with open("data_clean.txt", "w", encoding="utf-8") as f:
#     for en, uk in sorted(data.items(), key=lambda x: x[0]):
#         f.write(f"{en}\t{uk}\n")
#     for en, uk in train_pairs:
#         f.write(f"{en}\t{uk}\n")
# print("готово:", len(data)+len(train_pairs)+len(test_pairs))
