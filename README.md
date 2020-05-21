# swebert-summarize
A tiny demo on how to summarize swedish texts using the BERT model from the National Library of Sweden. It uses the [Bert Extractive Summarizer library](https://pypi.org/project/bert-extractive-summarizer/).

Install requirements:

```pip install -r requirements.txt```

Run it with 

```python summarize.py my_long_text.txt```

# Simple web gui
A simple web gui in Flask is provided for testing. To run it, install Docker and docker-compose. 

To run it:

```docker-compose up -d```

On the first run the BERT-model is downloaded (this may take several minutes). The ser ver will be available on 0.0.0.0:80.