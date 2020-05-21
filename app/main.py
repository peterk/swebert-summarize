from flask import Response, Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup
from summarizer import Summarizer
import transformers
import os
import sys

app = Flask(__name__)
app.secret_key = os.environ["FLASK_KEY"]
DEBUG = os.environ["FLASK_DEBUG"]

bert_model = "KB/bert-base-swedish-cased"
model = None
custom_model = transformers.BertModel.from_pretrained(bert_model,  output_hidden_states=True)
custom_tokenizer = transformers.BertTokenizer.from_pretrained(bert_model)
model = Summarizer(model=bert_model, custom_model=custom_model, custom_tokenizer=custom_tokenizer)
MAXLEN = 500
MINLEN = 100

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', maxlen=MAXLEN, minlen=MINLEN)


@app.route("/process/", methods=['POST'])
def process():
    text = request.form.get("text", None)
    result = model(text, max_length=MAXLEN, min_length=MINLEN)
    summary = ''.join(result)
    return render_template('index.html', text=text, summary=summary, maxlen=MAXLEN, minlen=MINLEN)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=DEBUG, port=80)