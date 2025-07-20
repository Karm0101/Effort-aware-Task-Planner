from flask import Flask, render_template
import pickle

def effortPredictions(tasks):
    with open('effortModel.pickle', 'rb') as file:
        effortModel = pickle.load(file)
    
    effortPreds = effortModel.prediction(tasks)
    return effortPreds

def importancePredictions(tasks):
    with open('importanceModel.pickle', 'rb') as file:
        importanceModel = pickle.load(file)
    
    importancePreds = importanceModel.prediction(tasks)
    return importancePreds

def easinessScore(effortPrediction):
    if effortPrediction == 'very easy':
        easiness = 4
    if effortPrediction == 'easy':
        easiness = 3
    if effortPrediction == 'moderate':
        easiness = 2
    else:
        easiness = 1
    
    return easiness

def importanceScore(importancePrediction):
    if importancePrediction == 'high importance':
        importance = 4
    if importancePrediction == 'medium importance':
        importance = 3
    if importancePrediction == 'low importance':
        importance = 2
    else:
        importance = 1
    
    return importance

def sortTasks(tasks, deadlines):
    effortPreds = effortPredictions(tasks)
    importancePreds = importancePredictions(tasks)
    tasksPriority = {}
    
    for i in range(len(tasks)):
        easiness = easinessScore(effortPreds[i])
        importance = importanceScore(importancePreds[i])
        urgency = 1/(deadlines[i] + 1)

        priority = easiness * importance * urgency

        tasksPriority.update({tasks[i]: priority})
    
    tasksPriority = sorted(dict.tasksPriority(), key = lambda item: item[1])
    return tasksPriority

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)