from nltk.corpus import stopwords
import gensim.models.keyedvectors as word2vec
import pickle

from pathlib import Path
from os.path import join
model_path = join(Path(__file__).parent, 'pretrained_models/glove.6B.300d.pickle')
model = None

def _init_model():
    global model
    if not model:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

def calculate_document_distance(doc_1, doc_2):
    """
    Calculates the distance between two documents
        :param doc_1(str): Document 1
        :param doc_2(str): Document 2
    """
    _init_model()
    doc_1 = clean_doc(doc_1)
    doc_2 = clean_doc(doc_2)

    return model.wmdistance(doc_1, doc_2)


def clean_doc(doc: str):
    return [
        word.lower().strip()
        for word in doc.split()
        if word not in stopwords.words('english')
    ]
