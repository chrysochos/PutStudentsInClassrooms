import random
import numpy as np
import pandas as pd
from collections import defaultdict
from student_file_reader import StudentFileReader
from student import Student
from group_analyzer import GroupAnalyzer


class ClassroomsGroupAnalyzer:
    def __init__(self, file_path, groups_list,students):
        self.students = students
        self.file_path = file_path
        # self.student_generator = StudentFileReader(self.file_path)
        # self.students = list(self.student_generator.generate_students())
        self.groups_list = groups_list
        self.males = 0
        self.females = 0
        self.special_needs = 0
        self.sum_of_grades = 0
        self.classrooms = 4
        self.classrooms_list = []
        self.classrooms_content = []
        self.previous_solution_cost = 1000000000

    def analyze_groups(self,groups_list):
        # groups = len(groups_list)
        males = 0
        females = 0
        special_needs = 0
        sum_of_grades = 0
        for group in groups_list:
            males += int(group.gm)
            females += int(group.gf)
            special_needs += int(group.gsn)
            sum_of_grades += group.ggrade
        print()
        print("Number of males:", males)
        print("Number of females:", females)
        print("Number of special_needs:", special_needs)
        print("Sum of grades:", sum_of_grades)
        print()

    def create_classrooms(self):
        self.classrooms_list.clear()
        for i in range(self.classrooms):
            self.classrooms_list.append([i, 0, 0, 0, 0])
        return self.classrooms_list

    def place_group_in_classroom(self, group, classroom):
        self.classrooms_list[classroom][1] += group.gm
        self.classrooms_list[classroom][2] += group.gf
        self.classrooms_list[classroom][3] += group.gsn
        self.classrooms_list[classroom][4] += group.ggrade
        self.classrooms_content.append([self.classrooms_list[classroom][0], group])
        return True

    def placement_of_groups_in_classrooms(self):
        for i in range(len(self.groups_list)):
            needs = []
            for j in range(len(self.classrooms_list)):
                add_males = self.classrooms_list[j][1] + self.groups_list[i].gm
                add_females = self.classrooms_list[j][2] + self.groups_list[i].gf
                add_specialneeds = self.classrooms_list[j][3] + self.groups_list[i].gsn
                add_ggrades = self.classrooms_list[j][4] + self.groups_list[i].ggrade
                coef = 0.85
                coef1 = random.uniform(coef, 1)
                coef2 = random.uniform(coef, 1)
                coef3 = random.uniform(coef, 1)
                coef4 = random.uniform(coef, 1)
                needs.append([j, coef1 * add_males + coef2 * add_females + coef3 * add_specialneeds + coef4 * add_ggrades])

            max_val = min(needs, key=lambda x: x[1])
            choose_class = max_val[0]

            if self.place_group_in_classroom(self.groups_list[i], self.classrooms_list[choose_class][0]):
                pass
            else:
                print("The group", i, "was not placed in any classroom")

    def optimize_classroom_placement(self, iterations, file_path,sheet_name):
        for j in range(iterations):
            self.classrooms_content.clear()
            self.create_classrooms()

            self.placement_of_groups_in_classrooms()

            np_array = np.array(self.classrooms_list)
            variances = np.var(np_array, axis=0)
            # solution_cost = variances[1] / (self.males +0.000000001) + variances[2] / (self.females +0.000000001) + variances[3] / (self.special_needs +0.000000001) + variances[4] / (self.sum_of_grades +0.000000001)
            solution_cost = variances[1] + variances[2] + variances[3] + variances[4]

            if solution_cost < self.previous_solution_cost:
                self.previous_solution_cost = solution_cost
                self.min_iteration = j
                self.best_classrooms_content = self.classrooms_content.copy()
                self.best_classrooms_list = self.classrooms_list.copy()

    def find_groups_by_classroom(self,iterations):
        print("Minimum Solution Cost", self.previous_solution_cost, "was found at iteration", self.min_iteration, "out of", iterations)
        # print()
        # print("Groups by classroom")
        # groups_by_classroom = {}
        for item in self.best_classrooms_content:
            classroom = item[0]
            group = item[1]
            group.assign_group_to_classroom(classroom)
            print("Classroom", classroom, "Group", group.group_id)
        # print(groups_by_classroom)
        return None
    
    def find_students_by_group_by_classroom(self):
        for student in self.students:
            print(student.student_id, student.group.group_id, student.group.classroom, student.group.group) 
        return None
    


        # df = pd.read_excel(file_path, sheet_name=sheet_name)

        # list_of_groups_to_classrooms = []
        # output_dict = {}
        # sorted_keys = sorted(groups_by_classroom.keys())
        # for key in sorted_keys:
        #     print(key, groups_by_classroom[key])
        #     for element in groups_by_classroom[key]:
        #         if element not in output_dict:
        #             output_dict[element] = []
        #         output_dict[element].append(key)

        # for key in sorted(output_dict.keys()):
        #     list_of_groups_to_classrooms.append(output_dict[key])
        #     for index, row in df.iterrows():
        #         if str(row['GroupN']).strip() == 'Group_' + str(key):
        #             df.at[index, 'Classroom'] = output_dict[key]

        # df.to_excel('final.xlsx', index=False)

        # print()
        # print("Best classrooms list")
        # for element in best_classrooms_list:
        #     print(element)
        # print()
        # print("Minimum Solution Cost", self.previous_solution_cost, "was found at iteration", min_iteration, "out of", iterations, "iterations")
        # print()

def main():
    # Usage example
    iterations = 2000
    file_path = 'new_students.xlsx'
    sheet_name = 'Students'
    classrooms = 4
    student_generator = StudentFileReader(file_path)
    students = list(student_generator.generate_students())
    group_analyzer = GroupAnalyzer(students,file_path)
    group_analyzer.process_students_to_couples()
    groups_list = group_analyzer.find_groups()
    for group in groups_list:
        group.print_group() 


    classrooms_group_analyzer = ClassroomsGroupAnalyzer(file_path, groups_list,students)
    classrooms_group_analyzer.analyze_groups(groups_list)
    classrooms_group_analyzer.create_classrooms()
    # classrooms_group_analyzer.placement_of_groups_in_classrooms()
    classrooms_group_analyzer.optimize_classroom_placement(iterations=iterations, file_path=file_path, sheet_name=sheet_name)
    # classrooms_group_analyzer.print_classrooms(iterations=iterations, file_path=file_path, sheet_name=sheet_name)
    classrooms_group_analyzer.find_groups_by_classroom(iterations=iterations)
    # print(groups_by_classroom)
    students_by_group_by_classroom = classrooms_group_analyzer.find_students_by_group_by_classroom()
    # print(students_by_group_by_classroom)
    # print(classrooms_group_analyzer.best_classrooms_list)
    # print(classrooms_group_analyzer.best_classrooms_content)
    classr = {}
    for classroom in range(classrooms):
        classr[classroom] = []
        classr_m = 0
        classr_f = 0
        classr_s = 0
        classr_g = 0
        for group in groups_list:
            if group.classroom == classroom:
                classr[classroom].append(group.group_id)
                classr_m +=group.gm
                classr_f +=group.gf
                classr_s +=group.gsn
                classr_g +=group.ggrade
        # print(classroom, classr[classroom])
        print(classroom, classr_m, classr_f, classr_s, classr_g)


    # print(classrooms_group_analyzer.classrooms_list)
    # print(classrooms_group_analyzer.classrooms_content)
    # print(classrooms_group_analyzer.previous_solution_cost)
    # print(classrooms_group_analyzer.min_iteration)
    pass
  
   


# call main
if __name__ == "__main__":
    main()
