class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def student_has_name(self):
        return self.student.name
    
    def student_has_cohort(self):
        return self.student.cohort
    
    def student_can_update_name(self):
        self.student.name = "Mike"
        return self.student.name
    
    def student_can_change_cohort(self):
        self.student.cohort = "G21"
        return self.student.cohort
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return "I love " + language
