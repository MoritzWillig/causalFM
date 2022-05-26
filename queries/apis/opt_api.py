from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from rtpt import RTPT

opt_model = "facebook/opt-30b" # "facebook/opt-30b"

def startup_opt(keys_dir):
    rtpt = RTPT(name_initials='MW', experiment_name='', max_iterations=100)
    rtpt.start()

    model = AutoModelForCausalLM.from_pretrained(opt_model, torch_dtype=torch.float16).cuda()

    # the fast tokenizer currently does not work correctly
    tokenizer = AutoTokenizer.from_pretrained(opt_model, use_fast=False)

    return model, tokenizer


def query_opt(context, query_text, dry_run=False):
    model, tokenizer = context

    print("[querying]", query_text)
    if dry_run:
        return None
    input_ids = tokenizer(query_text, return_tensors="pt").input_ids.cuda()
    generated_ids = model.generate(input_ids, num_return_sequences=1, max_length=70)

    results = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return results[0][len(query_text):]
