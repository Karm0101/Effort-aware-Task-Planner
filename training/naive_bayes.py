class NaiveBayesClassifier():
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
        if json.label == 'very easy':
            veryEasyTasks.append(json.data)
        elif json.label == 'easy':
            easyTasks.append(json.data)
        elif json.label == 'moderate':
            moderateTasks.append(json.data)
        elif json.label == 'hard':
            hardTasks.append(json.data)

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

        allSentences = veryEasyTasks + easyTasks + moderateTasks + hardTasks

        for word in allSentences:
            if word not in veryEasyCount:
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

        for character in easyCount:
            self.easyCount[character] = (self.easyCount[character] + 1) / (len(easyTasks) + len(self.easyCount))

        for character in moderateCount:
            self.moderateCount[character] = (self.moderateCount[character] + 1) / (len(moderateTasks) + len(self.moderateCount))

        for character in hardCount:
            self.hardCount[character] = (self.hardCount[character] + 1) / (len(hardTasks) + len(self.hardCount))

        self.probVeryEasy = len(veryEasyTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probEasy = len(easyTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probModerate = len(moderateTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))
        self.probHard = len(hardTasks) / (len(veryEasyTasks) + len(easyTasks) + len(moderateTasks) + len(hardTasks))

    def predict(self, taskList):
        for i in range(len(taskList)):
            taskList[i] = taskList[i].split()

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