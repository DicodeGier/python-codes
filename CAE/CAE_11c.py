class Student:
    def __init__(self, _name, _quizscore):
        self.name = _name
        self.quizscore = _quizscore
        self.number_of_quizzes = 1

    def getName(self):
        return self.name

    def addQuiz(self, score):
        self.quizscore += score
        self.number_of_quizzes += 1

    def getTotalScore(self):
        return self.quizscore

    def getAverageScore(self):
        return self.quizscore/self.number_of_quizzes

test = Student('flapper', 9)
print(test.getName())
test.addQuiz(8)
print(test.getTotalScore())
print(test.getAverageScore())
    