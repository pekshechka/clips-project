import re

import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords


def only_word_and_cifr(text: str) -> str:
    stop = stopwords.words("russian")
    text_ = re.sub("[^\w\s]", " ", text)
    text_ = " ".join(t.lower() for t in text_.split() if t.lower() not in stop)
    return text_
