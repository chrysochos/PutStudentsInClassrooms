import pandas as pd
from student import Student

class StudentFileReader():
    def __init__(self, file_path):
        self.file_path = file_path

    def generate_students(self):
        # Read the Excel file
        df = pd.read_excel(self.file_path)

        # Iterate over the rows and generate student objects
        for _, row in df.iterrows():
            student_id = row['ID']
            characteristics = {
                'first_name': row['FirstName'],
                'middle_name': row['MiddleName'],
                'family_name': row['FamilyName'],
                'gender' : row['Gender'],
                'with_id': row['WithID'],
                'old_school': row['OldSchool'],
                'old_school_class': row['OldSchoolClass'],
                'g1': row['G1'],
                'g2': row['G2'],
                'g3': row['G3'],
                'g4': row['G4'],
                'g5': row['G5'],
                'mean_value': row['MeanValue'],
                'special_needs': row['SpecialNeeds'],
                'notes': row['Notes']
            }
            yield Student(student_id, characteristics)

def main():
    file_path = 'new_students.xlsx'  # Path to the Excel file
    student_generator = StudentFileReader(file_path)
    students = list(student_generator.generate_students())
    return students

if __name__ == '__main__':
    students = main()

    # Print the number of students
    print(f"Number of students: {len(students)}")
    for student in students:
        # Process each student object
        print(f"Student ID: {student.student_id}, Characteristics: {student.first_name}")

