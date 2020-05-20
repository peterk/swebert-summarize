from summarizer import Summarizer
#from transformers import AutoModel,AutoTokenizer
import transformers
import os
import sys

filename = sys.argv[1]

print("Summrizing %s" % filename)

body = ""
with open(filename, 'r') as f:
    body = f.read()

bert_model = "KB/bert-base-swedish-cased"
custom_model = transformers.BertModel.from_pretrained(bert_model,  output_hidden_states=True)
custom_tokenizer = transformers.BertTokenizer.from_pretrained(bert_model)
model = Summarizer(model=bert_model, custom_model=custom_model, custom_tokenizer=custom_tokenizer)

#model = Summarizer(model='KB/bert-base-swedish-cased')
result = model(body, max_length=80, min_length=50)
full = ''.join(result)
print(full)

