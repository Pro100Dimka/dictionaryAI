import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

device = "cuda" if torch.cuda.is_available() else "cpu"
print("🔥 Using device:", device)

model_name = "facebook/nllb-200-distilled-600M"
SRC_LANG = "eng_Latn"
TGT_LANG = "ukr_Cyrl"


torch.backends.cudnn.benchmark = True
torch.set_float32_matmul_precision("high")


model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device)

model.eval()

tokenizer = AutoTokenizer.from_pretrained(model_name)


@torch.inference_mode()
def translate_batch(batch):
    tokenizer.src_lang = SRC_LANG
    inputs = tokenizer(
        batch,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=64
    ).to(device)
    outputs = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(TGT_LANG),
        max_length=64,
        num_beams=1,
        do_sample=False
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)
