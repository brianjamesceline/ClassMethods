class Student:
    # This is known as a class variable or class member
    gender = 'Female'

    def __init__(self, scores = []):
        self.scores = scores

    # The below is an instance method as it has the property of 'self'
    def avg(self):
        return round(sum(self.scores) / len(self.scores))
        
    @staticmethod
    # static methods only have access to what is passed in the brackets and NOT instance variables or class variables
    def notice():
        return "Exams next week!"
    

    @classmethod
    # Class method cannot access instance variabes but has its own property 'class' or 'cls' only. It can access class variabes above
    def what_is_gender(cls):
      return f"I am {cls.gender}"



print(Student.what_is_gender())

# class variables can access directly
print(Student.gender)
