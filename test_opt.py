from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from rtpt import RTPT

opt_model = "facebook/opt-13b" # "facebook/opt-30b"

rtpt = RTPT(name_initials='MW', experiment_name='', max_iterations=10)
rtpt.start()

model = AutoModelForCausalLM.from_pretrained(opt_model, torch_dtype=torch.float16).cuda()

# the fast tokenizer currently does not work correctly
tokenizer = AutoTokenizer.from_pretrained(opt_model, use_fast=False)

prompt = "Hello, I'm am conscious and"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

generated_ids = model.generate(input_ids, num_return_sequences=1, max_length=50)

result = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

print(f"\"{prompt}\"")
print(result[0][len(prompt):])
#["Hello, I'm am conscious and I'm not a robot.\nI'm a robot and"]
