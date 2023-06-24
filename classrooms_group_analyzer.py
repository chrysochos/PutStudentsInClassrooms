import random
import numpy as np
from student_file_reader import StudentFileReader
from group_analyzer import GroupAnalyzer
from save_to_excel import SaveToExcel
from clustering import Clustering

class ClassroomsGroupAnalyzer:
    def __init__(self, file_path, groups_list,students,classrooms,max_old_classrooms, max_old_schools):
        """_summary_line
        Args:
            file_path (str): path to the file
            groups_list (list): list of groups
            students (list): list of students
            
        """ 
        self.students = students
        self.file_path = file_path
        self.max_old_classrooms = max_old_classrooms
        self.max_old_schools = max_old_schools
        # self.student_generator = StudentFileReader(self.file_path)
        # self.students = list(self.student_generator.generate_students())
        self.groups_list = groups_list
        self.males = 0
        self.females = 0
        self.special_needs = 0
        self.sum_of_grades = 0
        self.classrooms = classrooms
        self.classrooms_list = []
        self.classrooms_content = []
        self.previous_solution_cost = 1000000000
        self.coef = 0.85

    def analyze_groups(self,groups_list):
        """
        _summary_line
        Args:
            groups_list (list): list of groups
        Returns:
            None      
        """        
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
        print("Sum of grades:", round(sum_of_grades,2))
        print("Total grade:", round(sum_of_grades/(males+females),2))
        print()

    def create_classrooms(self):
        self.classrooms_list.clear()
        for classroom in range(self.classrooms):
            self.classrooms_list.append([classroom, 0, 0, 0, 0,[0]*(self.max_old_schools+1),[0]*(self.max_old_classrooms+1)])
        return self.classrooms_list

    def place_group_in_classroom(self, group, classroom):
        self.classrooms_list[classroom][1] += group.gm
        self.classrooms_list[classroom][2] += group.gf
        self.classrooms_list[classroom][3] += group.gsn
        self.classrooms_list[classroom][4] += group.ggrade
        # I want a dictionary for each classroom to keep variablle number of keys of OldSchools to keep counters of such occurences
        # self.classrooms_list[classroom][5] = []
        # I want a dictionary for each classroom to keep variablle number of keys of OldSchoolsClassrooms to keep counters of such occurences
        # self.classrooms_list[classroom][6] = []
        for student0 in group.group:
            # find student with student.id in self.students
            for student in self.students:
                if student.student_id == student0:

                    self.classrooms_list[classroom][5][student.old_school] += 1

                    self.classrooms_list[classroom][6][student.old_school_classroom] += 1

                    break



        self.classrooms_content.append([self.classrooms_list[classroom][0], group])
        return True

    def placement_of_groups_in_classrooms(self):

        for i in range(len(self.groups_list)):
            try:
                if self.groups_list[i].preput == True:
                    if self.place_group_in_classroom(self.groups_list[i], int(self.groups_list[i].preput_classroom)-1):
                        pass
                    else:
                        print("The group", i, "was not placed in any classroom")
                    continue
            except:
                pass
            needs = []
            for j in range(len(self.classrooms_list)):
                add_males = self.classrooms_list[j][1] + self.groups_list[i].gm
                add_females = self.classrooms_list[j][2] + self.groups_list[i].gf
                add_specialneeds = self.classrooms_list[j][3] + self.groups_list[i].gsn
                add_ggrades = self.classrooms_list[j][4] + self.groups_list[i].ggrade
                coef = self.coef
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

    def flatten_list(self,nested_list):
        flattened = []
        for item in nested_list:
            if isinstance(item, list):
                flattened.extend(self.flatten_list(item))
            else:
                flattened.append(item)
        return flattened
    

    def optimize_classroom_placement(self, iterations):
        for j in range(iterations):
            self.classrooms_content.clear()
            self.create_classrooms()

            

            self.placement_of_groups_in_classrooms()

            my_list = []
            # I must flatten but keep the list of each classrooms
           
            for classroom in self.classrooms_list:
                homogeneous_list = self.flatten_list(classroom)
                # homogeneous_list = [value for value in self.flatten_list(classroom)[1:] if value != 0]
                my_list.append(homogeneous_list[1:])
                pass
            np_array = np.array(my_list)
            # we add the first 2 columns with males and females and we put the sum in the first column
            sum_column = np_array[:, 0] + np_array[:, 1]
            np_array = np.insert(np_array, 0, sum_column, axis=1)
            # for the cost we see the ratio of the grades to the number of students
            np_array[:,4] = np_array[:,4]/np_array[:,0]
            # There is no any need to see only the first columns
            # np_array = np.array(my_list)[:, :8]
            mean = np.mean(np_array, axis=0)
            # We give more weight to the bigger values like number of students, males, females, grades, old schools and old classrooms.
            coefficient_of_variation = np.std(np_array, axis=0) * mean 
            solution_cost = np.sum(coefficient_of_variation)

            if solution_cost < self.previous_solution_cost:
                self.previous_solution_cost = solution_cost
                self.min_iteration = j
                self.best_classrooms_content = self.classrooms_content.copy()
                self.best_classrooms_list = self.classrooms_list.copy()
                self.best_np_array = np_array.copy()
            # print(j, solution_cost)
            # if solution_cost < 115:
            #     break

    def find_groups_by_classroom(self,iterations):
        print("Minimum Solution Cost", self.previous_solution_cost, "was found at iteration", self.min_iteration, "out of", iterations)
        # print()
        # print("Groups by classroom")
        # groups_by_classroom = {}
        for item in self.best_classrooms_content:
            classroom = item[0]
            group = item[1]
            group.assign_group_to_classroom(classroom)
            # print("Classroom", classroom, "Group", group.group_id)
        # print(groups_by_classroom)
        return None
    
    def find_students_by_group_by_classroom(self):
        for student in self.students:
            pass
            print("Student no. ",student.student_id, " in classroom " ,student.group.classroom, " in group ", student.group.group_id, student.group.get_group_values(), student.group.group) 
        return None
    

def main():
    """
    This is the  main entry point of the program. 
    Here we must initialize and create the main objects
    and give the results of the program to screen and excel file.
    """    
    # Usage example
    iterations = 300000
    file_path = 'new_students.xlsx'
    output_sheet_name = 'Results'
    starting_sheet_name = 'Starting Students'
    sheet_name = 'Students'
    classrooms = 7
    coef = 0.85
    clustering = Clustering(file_path, starting_sheet_name,sheet_name)
    max_old_classrooms, max_old_schools = clustering.run()
    student_generator = StudentFileReader(file_path, sheet_name=sheet_name)
    students = list(student_generator.generate_students())
    group_analyzer = GroupAnalyzer(students,file_path)
    group_analyzer.process_students_to_couples()
    groups_list = group_analyzer.find_groups()

    # for group in groups_list:
    #     group.print_group() 
    classrooms_group_analyzer = ClassroomsGroupAnalyzer(file_path, groups_list,students,classrooms, max_old_classrooms, max_old_schools)
    classrooms_group_analyzer.coef = coef
    classrooms_group_analyzer.analyze_groups(groups_list)
    # the preput groups are going directly into preput classrooms
    classrooms_group_analyzer.optimize_classroom_placement(iterations=iterations)
    classrooms_group_analyzer.find_groups_by_classroom(iterations=iterations)
 
    save_to_excel = SaveToExcel(file_path, output_sheet_name, students)
    save_to_excel.save_to_excel()
    print("Τάξη","Αγόρ.","Κορ","Sp.","Βαθμός")
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
        a =classroom+1
        bb = round(classr_g/(classr_m+classr_f),2)
        print(f"{a:4}", f"{classr_m:4}", f"{classr_f:4}", f"{classr_s:4}", f"{bb:4}")  

    print("The results are saved in the file", file_path ,"in the sheet", output_sheet_name)
    pass
  
    # Assuming classrooms_group_analyzer.best_np_array is the array
    rows, cols = classrooms_group_analyzer.best_np_array.shape

    # Print the array in rows
    print("The best solution is the following: ")
    print("Μαθ.","Αγ.","Κορ.","Sp","Βαθ.", end=" ")
    for i in range(0,max_old_schools+1):
        print(f"Σ{i+1}".rjust(3), end=" ")
    for i in range(max_old_classrooms+1):
        print(f"T{i+1}".rjust(3), end=" ")
    print()
    for row in range(rows): 
        for col in range(cols):
            print(str(int(classrooms_group_analyzer.best_np_array[row][col])).rjust(3), end=" ")
        print()
    pass



# call main
if __name__ == "__main__":
    main()
