import pandas as pd
from excel_utils import write_sheet_to_excel

class SaveToExcel:
    def __init__(self, input_file_path, output_sheet_name, students):
        self.input_file_path = input_file_path
        self.output_sheet_name = output_sheet_name
        self.students = students

    def save_to_excel(self):
        df = pd.read_excel(self.input_file_path)
        for student in self.students:
            row_index = df[df['ID'] == student.student_id].index
            df.loc[row_index, 'Classroom'] = student.group.classroom + 1
            df.loc[row_index, 'GroupID'] = student.group.group_id
            df.loc[row_index, 'GroupValues'] = str(student.group.get_group_values())
            df.loc[row_index, 'Group'] = str(student.group.group)
        # df.to_excel(self.input_file_path, sheet_name=self.output_sheet_name, index=False)

        write_sheet_to_excel(df, self.output_sheet_name, self.input_file_path)
           
def main():
    """
    This is the  main entry point of the program. 
    """
    input_file_path = 'new_students.xlsx'
    output_file_path = 'new_students_output.xlsx'
    students = StudentFileReader(file_path).get_students()


if __name__ == '__main__':
    main()
