from preprocess import preprocessor
from naive_bayes import NaiveBayesClassifier
import json
import pickle

def training():
    with open('training\dataset.json', 'r') as f:
        dataset = json.load(f)

    for i in range(len(dataset)):
        dataset[i]['task'] = preprocessor(dataset[i]['task'])

    model = NaiveBayesClassifier()
    model.train(dataset)

    with open('model.pickle', 'wb') as file:
        pickle.dump(model, file)

if __name__ == '__main__':
    training()