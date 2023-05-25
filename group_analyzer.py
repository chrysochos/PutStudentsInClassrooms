from collections import defaultdict
from student_file_reader import StudentFileReader
from group import Group

class GroupAnalyzer:
    def __init__(self, students, file_path):
        self.file_path = file_path
        self.students = students

        self.couples = {}

    def process_students_to_couples(self):
        for student in self.students:
            if student.with_id.is_integer():
                # print(f"Student ID: {student.student_id}, with_id: {student.with_id}")
                self.couples[student.student_id] = [int(student.with_id)]
            else:
                self.couples[student.student_id] = []

    def find_groups(self):
        graph = defaultdict(list)

        for v1 in self.couples:
            for v2 in self.couples[v1]:
                graph[v1].append(v2)
                graph[v2].append(v1)
        i = 0
        groups = []
        visited = set()
        for v in self.couples:
            if v not in visited:
                island = set()
                stack = [v]
                while stack:
                    vertex = stack.pop()
                    if vertex not in visited:
                        visited.add(vertex)
                        island.add(vertex)
                        stack.extend(graph[vertex])
                # create a group object
                group = Group(self.students)
                group.add_group(i, island,students=self.students)
                for student1 in island:
                    for student in self.students:
                        if student.student_id == student1:
                            student.assign_group(group)
                groups.append(group)
                i += 1
        return groups

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        print("ERROR: Student not found")
        return None



def main():
    # Usage example
    file_path = 'new_students.xlsx'
    student_generator = StudentFileReader(file_path)
    students = list(student_generator.generate_students())
    group_analyzer = GroupAnalyzer(students,file_path)
    group_analyzer.process_students_to_couples()
    groups_list = group_analyzer.find_groups()
    for group in groups_list:
        group.print_group() 

if __name__ == '__main__':
    main()
