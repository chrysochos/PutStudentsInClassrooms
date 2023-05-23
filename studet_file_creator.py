# Copyright (c) 2023 Ioannis Chrysochos
# This is done by Ioannis Chrysochos
# All rights reserved.

import random
import openpyxl

# generate a list of students
def generate_students(filename='new_students.xlsx', students_number=99, male_proportion=0.5, special_needs_proportion=0.2, with_id_proportion=0.3):

    # Create a new excel workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Set the column headers
    ws.append(['ID', 'FirstName', 'MiddleName', 'FamilyName', 'Gender', 'WithID', 'OldSchool', 'OldSchoolClass', 'G1', 'G2', 'G3', 'G4', 'G5', 'MeanValue', 'SpecialNeeds', 'Notes'])

    # Set up the mock data
    greek_first_names = ['Αλέξανδρος', 'Δημήτρης', 'Γιώργος', 'Κωνσταντίνος', 'Ανδρέας', 'Νικόλαος', 'Παναγιώτης', 'Σταύρος', 'Βασίλης', 'Μιχάλης']
    greek_surnames = ['Παπαδόπουλος', 'Καραμανλής', 'Γιαννόπουλος', 'Παπανδρέου', 'Κουμουτσάκος', 'Τσίπρας', 'Μητσοτάκης', 'Καρατζαφέρης', 'Λιάπης', 'Αδωνις Γεωργιάδης']
    old_schools = ['S1', 'S2', 'S3', 'S4']
    old_school_classes = ['OSC1', 'OSC2', 'OSC3']
    grades = [5, 4, 3, 2, 1]

    # define a list of created students
    students_list = []

    # Create 99 rows of data
    for i in range(1, students_number + 1):
        # Generate mock data for each column
        first_name = random.choice(greek_first_names)
        middle_name = random.choice(greek_first_names)
        family_name = random.choice(greek_surnames)
        #gender = random.choice(['F', 'M', 'F', 'F', 'F', 'M', 'M', 'M', 'M', 'M'])
        rr =random.random()
        if rr < male_proportion:
            gender = 'M'
        else:
             gender = 'F'
        with_id = random.randint(1, 99) if random.random() < with_id_proportion else ''
        old_school = random.choice(old_schools)
        old_school_class = random.choice(old_school_classes)
        g1 = random.choice(grades)
        g2 = random.choice(grades)
        g3 = random.choice(grades)
        g4 = random.choice(grades)
        g5 = random.choice(grades)
        mean_value = (g1 + g2 + g3 + g4 + g5) / 5
        special_needs = 1 if random.random() < special_needs_proportion else ''
        
        # Add the row of data to the worksheet
        ws.append([i, first_name, middle_name, family_name, gender, with_id, old_school, old_school_class, g1, g2, g3, g4, g5, mean_value, special_needs, ''])
    
        # Add the student to the list of students
        students_list.append(i)
                    
    #print(wb.sheetnames)
    wb['Sheet'].title = 'Students'
    # Save the workbook as an excel file
    wb.save(filename)
    return students_list 

filename = 'new_students.xlsx'
students_number = 99
with_id_proportion = 0.25
male_proportion = 0.4
special_needs_proportion = 0.2
students_list = generate_students(filename, students_number, male_proportion, special_needs_proportion, with_id_proportion)
#print(students_list)

