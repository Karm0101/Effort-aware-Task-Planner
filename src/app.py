from flask import Flask, render_template, request
import pickle

def effortPredictions(tasks):
    with open('model\effortModel.pickle', 'rb') as file:
        effortModel = pickle.load(file)
        
    tasksArray = []
    for task in tasks:
        tasksArray.append(task.get('task'))

    effortPreds = effortModel.predict(tasksArray)
    return effortPreds

def importancePredictions(tasks):
    with open('model\importanceModel.pickle', 'rb') as file:
        importanceModel = pickle.load(file)
    
    tasksArray = []
    for task in tasks:
        tasksArray.append(task.get('task'))
        
    importancePreds = importanceModel.predict(tasksArray)
    return importancePreds

def easinessScore(effortPrediction):
    if effortPrediction == 'very easy':
        easiness = 4
    elif effortPrediction == 'easy':
        easiness = 3
    elif effortPrediction == 'moderate':
        easiness = 2
    else:
        easiness = 1
    
    return easiness

def importanceScore(importancePrediction):
    if importancePrediction == 'high importance':
        importance = 4
    elif importancePrediction == 'medium importance':
        importance = 3
    elif importancePrediction == 'low importance':
        importance = 2
    else:
        importance = 1
    
    return importance

def sortTasks(tasks):
    effortPreds = effortPredictions(tasks)
    importancePreds = importancePredictions(tasks)
    tasksPriority = {}
    
    for i in range(len(tasks)):
        easiness = easinessScore(effortPreds[i])
        importance = importanceScore(importancePreds[i])
        deadline = tasks[i].get('deadline')

        if deadline:
            urgency = 1/(deadline + 1)
        else:
            urgency = 0.01

        priority = easiness * importance * urgency

        print(easiness, importance, deadline)
        tasksPriority.update({tasks[i].get('task'): priority})
    
    tasksPriority = sorted(tasksPriority, key=tasksPriority.get, reverse=True)
    return tasksPriority

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    return render_template('index.html')

@app.route("/process_tasks", methods=['POST', 'GET'])
def processTasks():
    if request.method == 'POST':
        tasks = request.get_json()
        tasksPriority = sortTasks(tasks)
        return tasksPriority
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)