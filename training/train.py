from preprocess import preprocessor
from naive_bayes import NaiveBayesClassifier
import json

def training():
    with open('training\dataset.json', 'r') as f:
        dataset = json.load(f)

    for i in range(len(dataset)):
        dataset[i]['task'] = preprocessor(dataset[i]['task'])

    model = NaiveBayesClassifier()