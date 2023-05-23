from main1 import Main1
from student import Student
from student_file_reader import StudentFileReader
import numpy as np


class Group():
    def __init__(self):
        self.group_id = None
        self.group =[]
        self.classroom = None

    def add_group(self, group_id,group, students):
        self.group_id = group_id
        self.group = group
        self.gm =0
        self.gf =0
        self.gsn =0
        self.ggrade =0
        for stud in group:
            student = Main1.find_student_by_id(students, stud)
            self.gm += 1 if student.gender in ('M', 'm') else 0
            self.gf += 1 if student.gender in ('F', 'f') else 0
            value = np.where(np.isnan(student.special_needs), 0, student.special_needs)
            self.gsn += int(value)  
            self.ggrade += student.mean_value
            student.assign_group(self)
        self.ggrade = self.ggrade / len(group)
        self.ggrade = self.ggrade / 10
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
    
    