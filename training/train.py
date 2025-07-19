from preprocess import preprocessor
from naive_bayes import EffortClassifier, ImportanceClassifier
import json
import pickle

def training():
    with open('training\dataset.json', 'r') as f:
        dataset = json.load(f)

    for i in range(len(dataset)):
        dataset[i]['task'] = preprocessor(dataset[i]['task'])

    effortModel = EffortClassifier()
    effortModel.train(dataset)

    importanceModel = ImportanceClassifier()
    importanceModel.train(dataset)

    with open('effortModel.pickle', 'wb') as file:
        pickle.dump(effortModel, file)
    
    with open('importanceModel', 'wb') as file:
        pickle.dump(importanceModel, file)

if __name__ == '__main__':
    training()