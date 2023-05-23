import os
import pandas as pd 
import math
from student import Student

from collections import defaultdict
# Import the StudentFileReader class from the student_file_reader module
from student_file_reader import StudentFileReader

class Main1:
    file_path = 'new_students.xlsx'  # Path to the Excel file
    student_generator = StudentFileReader(file_path)
    students = list(student_generator.generate_students())
    couples = {}

    for student in students:
        # Process each student object

        if student.with_id.is_integer():
            print(f"Student ID: {student.student_id}, with_id: {student.with_id}")
            couples[student.student_id] = [int(student.with_id)]
        else:
            couples[student.student_id]= []
    # print(couples)

    # Create a function to find the groups
    def find_groups(couples):
        # Create an empty graph
        graph = defaultdict(list)
        
        # Add edges to the graph
        for v1 in couples:
            for v2 in couples[v1]:
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        # Initialize an empty list of groups
        groups = []
        
        # Traverse the graph to find the groups
        visited = set()
        for v in couples:
            if v not in visited:
                island = set()
                stack = [v]
                while stack:
                    vertex = stack.pop()
                    if vertex not in visited:
                        visited.add(vertex)
                        island.add(vertex)
                        stack.extend(graph[vertex])
                groups.append(island)
        
        # Return the list of groups
        return groups

    groups = find_groups(couples)
    # print(groups)

    def find_student_by_id(students, student_id):

        for student in students:
            if student.student_id == student_id:
                return student
        print("ERROR: Student not found")
        return None

    # def something_else():
    #     groups_list = []
    #     for idx1, group1 in enumerate(groups):
    #         print("group has:", group1)
    #         length = len(group1)
    #         if length > 5:  # external setting
    #             print('group=', i, ' is too big')
    #             exit()
    #         gm = 0
    #         gf = 0
    #         gsn = 0
    #         ggrade = 0 
    #         for i, stud in enumerate(group1):
    #             student=find_student_by_id(students, stud)                
    #             if student.gender == 'M' or student.gender =='m':
    #                 gm += 1
    #             else:
    #                 gf += 1
    #             if student.special_needs == 1:
    #                 gsn += 1
    #             ggrade += student.mean_value
                
    #         ggrade = ggrade / length
    #         ggrade = ggrade / 10
    #         #print('group=', id, ' Male=',gm,' Female=',gf, ' SpecialNeeds=',gsn, ' Group Grade=',ggrade)
    #         #print(id, gm, gf, gsn, "{:.2f}".format(ggrade))

    #         groups_list.append([idx1,int(gm),int(gf),int(gsn),ggrade])

    pass