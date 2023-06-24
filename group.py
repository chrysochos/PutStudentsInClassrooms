import numpy as np
class Group():
    def __init__(self, students):
        self.group_id = None
        self.group =[]
        self.classroom = None


    def find_student_by_id(self,students, student_id):

        for student in students:
            if student.student_id == student_id:
                return student
        print("ERROR: Student not found")
        return None
        
    def add_group(self, group_id,group, students):
        self.group_id = group_id
        self.group = group
        self.gm =0
        self.gf =0
        self.gsn =0
        self.ggrade =0
        self.group_old_schools = []
        self.group_old_school_classrooms = []
        for stud in group:
            student = self.find_student_by_id(students, stud)
            self.gm += 1 if student.gender in ('M', 'm') else 0
            self.gf += 1 if student.gender in ('F', 'f') else 0
            value = np.where(np.isnan(student.special_needs), 0, student.special_needs)
            self.gsn += int(value)  
            self.ggrade += student.mean_value
            student.assign_group(self)
            self.group_old_school_classrooms.append(student.old_school_classroom)
            self.group_old_schools.append(student.old_school)
        return None
 
    def get_group_values(self):
        """_summary_line
        Returns: the values of the group         
        """        
        return [self.gm, self.gf, self.gsn, round(self.ggrade,2)]

    def get_group(self):
        return self.group
       
    def print_group(self):
        print(self.group_id, self.group)
        return None

    def assign_group_to_classroom(self, classroom):
        self.classroom = classroom
        return None
    
    def get_classroom_of_group(self):
        return self.classroom
    
    