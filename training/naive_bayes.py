from preprocess import preprocessor

class EffortClassifier():
    def __init__(self):
        self.probVeryEasy = 0
        self.probEasy = 0
        self.probModerate = 0
        self.probHard = 0
        self.veryEasyCount = {}
        self.easyCount = {}
        self.moderateCount = {}
        self.hardCount = {}

    def train(self, dataset):
        veryEasyTasks = []
        easyTasks = []
        moderateTasks = []
        hardTasks = []
        for task in dataset:
            if task['effort'] == 'very easy':
                veryEasyTasks.append(task['task'])
            elif task['effort'] == 'easy':
                easyTasks.append(task['task'])
            elif task['effort'] == 'moderate':
                moderateTasks.append(task['task'])
            elif task['effort'] == 'hard':
                hardTasks.append(task['task'])

        numOfVeryEasyTasks = len(veryEasyTasks)
        veryEasyTasks = ' '.join(veryEasyTasks)
        veryEasyTasks = veryEasyTasks.split()

        numOfEasyTasks = len(easyTasks)
        easyTasks = ' '.join(easyTasks)
        easyTasks = easyTasks.split()

        numOfModerateTasks = len(moderateTasks)
        moderateTasks = ' '.join(moderateTasks)
        moderateTasks = moderateTasks.split()

        numOfHardTasks = len(hardTasks)
        hardTasks = ' '.join(hardTasks)
        hardTasks = hardTasks.split()

        allTasks = veryEasyTasks + easyTasks + moderateTasks + hardTasks

        for word in allTasks:
            if word not in self.veryEasyCount:
                countInVeryEasy = veryEasyTasks.count(word)
                countInEasy = easyTasks.count(word)
                countInModerate = moderateTasks.count(word)
                countInHard = hardTasks.count(word)

                self.veryEasyCount.update({word: countInVeryEasy})
                self.easyCount.update({word: countInEasy})
                self.moderateCount.update({word: countInModerate})
                self.hardCount.update({word: countInHard})

        for character in self.veryEasyCount:
            self.veryEasyCount[character] = (self.veryEasyCount[character] + 1) / (len(veryEasyTasks) + len(self.veryEasyCount))

        for character in self.easyCount:
            self.easyCount[character] = (self.easyCount[character] + 1) / (len(easyTasks) + len(self.easyCount))

        for character in self.moderateCount:
            self.moderateCount[character] = (self.moderateCount[character] + 1) / (len(moderateTasks) + len(self.moderateCount))

        for character in self.hardCount:
            self.hardCount[character] = (self.hardCount[character] + 1) / (len(hardTasks) + len(self.hardCount))

        self.probVeryEasy = len(veryEasyTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probEasy = len(easyTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probModerate = len(moderateTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probHard = len(hardTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))

    def predict(self, taskList):
        for i in range(len(taskList)):
            taskList[i] = preprocessor(taskList[i]).split()

        taskPredictions = []
        for task in taskList:
            probIfVeryEasy = self.probVeryEasy
            probIfEasy = self.probEasy
            probIfModerate = self.probModerate
            probIfHard = self.probHard
            for word in task:
                if word in self.veryEasyCount or word in self.easyCount or word in self.moderateCount or word in self.hardCount:
                    probIfVeryEasy *= self.veryEasyCount[word]
                    probIfEasy *= self.easyCount[word]
                    probIfModerate *= self.moderateCount[word]
                    probIfHard *= self.hardCount[word]

            probDict = {probIfVeryEasy: "very easy", probIfEasy: "easy", probIfModerate: "moderate", probIfHard: "hard"}
            taskPredictions.append(probDict.get(max(probDict)))
    
        return taskPredictions

class ImportanceClassifier():
    def __init__(self):
        self.probNoImportance = 0
        self.probLowImportance = 0
        self.probMediumImportance = 0
        self.probHighImportance = 0
        self.noImportanceCount = {}
        self.lowImportanceCount = {}
        self.mediumImportanceCount = {}
        self.highImportanceCount = {}

    def train(self, dataset):
        noImportanceTasks = []
        lowImportanceTasks = []
        mediumImportanceTasks = []
        highImportanceTasks = []
        for task in dataset:
            if task['importance'] == 'no importance':
                noImportanceTasks.append(task['task'])
            elif task['importance'] == 'low importance':
                lowImportanceTasks.append(task['task'])
            elif task['importance'] == 'medium importance':
                mediumImportanceTasks.append(task['task'])
            elif task['importance'] == 'high importance':
                highImportanceTasks.append(task['task'])

        numOfNoImportanceTasks = len(noImportanceTasks)
        noImportanceTasks = ' '.join(noImportanceTasks)
        noImportanceTasks = noImportanceTasks.split()

        numOfLowImportanceTasks = len(lowImportanceTasks)
        lowImportanceTasks = ' '.join(lowImportanceTasks)
        lowImportanceTasks = lowImportanceTasks.split()

        numOfMediumImportanceTasks = len(mediumImportanceTasks)
        mediumImportanceTasks = ' '.join(mediumImportanceTasks)
        mediumImportanceTasks = mediumImportanceTasks.split()

        numOfHighImportanceTasks = len(highImportanceTasks)
        highImportanceTasks = ' '.join(highImportanceTasks)
        highImportanceTasks = highImportanceTasks.split()

        allTasks = noImportanceTasks + lowImportanceTasks + mediumImportanceTasks + highImportanceTasks

        for word in allTasks:
            if word not in self.noImportanceCount:
                countInNoImportance = noImportanceTasks.count(word)
                countInLowImportance = lowImportanceTasks.count(word)
                countInMediumImportance = mediumImportanceTasks.count(word)
                countInHighImportance = highImportanceTasks.count(word)

                self.noImportanceCount.update({word: countInNoImportance})
                self.lowImportanceCount.update({word: countInLowImportance})
                self.mediumImportanceCount.update({word: countInMediumImportance})
                self.highImportanceCount.update({word: countInHighImportance})

        for character in self.noImportanceCount:
            self.noImportanceCount[character] = (self.noImportanceCount[character] + 1) / (len(noImportanceTasks) + len(self.noImportanceCount))

        for character in self.lowImportanceCount:
            self.lowImportanceCount[character] = (self.lowImportanceCount[character] + 1) / (len(lowImportanceTasks) + len(self.lowImportanceCount))

        for character in self.mediumImportanceCount:
            self.mediumImportanceCount[character] = (self.mediumImportanceCount[character] + 1) / (len(mediumImportanceTasks) + len(self.mediumImportanceCount))

        for character in self.highImportanceCount:
            self.highImportanceCount[character] = (self.highImportanceCount[character] + 1) / (len(highImportanceTasks) + len(self.highImportanceCount))

        self.probNoImportance = len(noImportanceTasks) / (len(noImportanceTasks) + len(lowImportanceTasks) + len(mediumImportanceTasks) + len(highImportanceTasks))
        self.probLowImportance = len(lowImportanceTasks) / (len(noImportanceTasks) + len(lowImportanceTasks) + len(mediumImportanceTasks) + len(highImportanceTasks))
        self.probMediumImportance = len(mediumImportanceTasks) / (len(noImportanceTasks) + len(lowImportanceTasks) + len(mediumImportanceTasks) + len(highImportanceTasks))
        self.probHighImportance = len(highImportanceTasks) / (len(noImportanceTasks) + len(lowImportanceTasks) + len(mediumImportanceTasks) + len(highImportanceTasks))

    def predict(self, taskList):
        for i in range(len(taskList)):
            taskList[i] = preprocessor(taskList[i]).split()

        taskPredictions = []
        for task in taskList:
            probIfNoImportance = self.probNoImportance
            probIfLowImportance = self.probLowImportance
            probIfMediumImportnace = self.probMediumImportance
            probIfHighImportance = self.probHighImportance
            for word in task:
                if word in self.noImportanceCount or word in self.lowImportanceCount or word in self.mediumImportanceCount or word in self.highImportanceCount:
                    probIfNoImportance *= self.noImportanceCount[word]
                    probIfLowImportance *= self.lowImportanceCount[word]
                    probIfMediumImportnace *= self.mediumImportanceCount[word]
                    probIfHighImportance *= self.highImportanceCount[word]

            probDict = {probIfNoImportance: "no importance", probIfLowImportance: "low importance", probIfMediumImportnace: "medium importance", probIfHighImportance: "high importance"}
            taskPredictions.append(probDict.get(max(probDict)))
    
        return taskPredictions