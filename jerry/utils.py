import re
import zipfile
from collections import Counter


def canonicalize_text(text):
    text = text.lower()
    # Normalize the empty space symbol
    text = re.sub('[\t\n]', ' ', text)
    # Eliminate non-alphanumeric characters
    text = re.sub('[^a-zA-z0-9\s]', '', text)
    # Replace all digits by symbol `DG`
    text = re.sub('\d+', 'DG', text)
    return text


def preprocess(data):
    data['text'] = data['text'].apply(canonicalize_text)


def read_zip_file(filepath, filename):
    zfile = zipfile.ZipFile(filepath)
    ifile = zfile.open(filename)
    for line in ifile.readlines():
        yield line


def get_corpus_vocabulary(df):
    vocabulary = Counter()
    for _, row in df.iterrows():
        words = row['text'].split()
        for word in words:
            vocabulary[word] += 1
    return vocabulary
