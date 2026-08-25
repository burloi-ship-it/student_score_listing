class Log:
    def __init__(self, student, score):
        self.student = student
        self.score = score
        
    def __str__(self):
        return f"{self.student} - {self.score}"