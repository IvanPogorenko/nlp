import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
np.random.seed(42)
torch.manual_seed(42)

def generate(model, tok, text, do_sample=True, max_length=400, repetition_penalty=0.8, top_k = 5, top_p=0.95, temperature = 0.95, num_beams=None, no_repeat_ngram_size=3):
    input_ids = tok.encode(text, return_tensors="pt")
    print(model.generate.__globals__['__file__'])
    out = model.generate(input_ids, max_length = max_length, repetition_penalty = repetition_penalty, do_sample = do_sample, top_k = top_k, top_p = top_p, temperature = temperature, num_beams = num_beams, no_repeat_ngram_size = no_repeat_ngram_size)
    return list(map(tok.decode, out))

bb = 'Расскажу Вам про день. С самого утра только и делаю что придумываю смешные шутки, у меня в голове только шутки и шутки, поэтому я только и делаю, что хохочу и ш'

def load_tokenizer_and_model(model_name_or_path):
    return GPT2Tokenizer.from_pretrained(model_name_or_path), GPT2LMHeadModel.from_pretrained(model_name_or_path)

tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3large_based_on_gpt2")
generated = generate(model, tok, bb, num_beams=10)
print(generated[0])