# PUT THE STUDENTS IN CLASSROOMS
We start with empty classrooms. We put students in classrooms based on their space. Whenever we put a student we add to the corresponding dimensions of several characteristics, like grades, gender, previous school, and class etc. We may have requests to put some students in the same classroom as some other students. So, we start from these groups first. Our intention is to put the students evenly distributed based on their characteristics in all the classrooms.

We try to put the students to the emptiest classroom, but we give a randomness and we try many times. We calculate the results (cost) of each run and then we select the optimum run.

## EXECUTABLE PROGRAMS

### classrooms_groups_analyzer.py
The main program is classrooms_groups_analyzer.py, which has the following parameters:

	iterations (runs) = 2000 # Trials to find the optimal solution.
	file_path = 'new_students.xlsx' # The working file
	starting_sheet_name = 'Starting Students' # The sheet with the actual data
	sheet_name = 'Students' # The program's understanding of the students
	output_sheet_name = 'Results' # The results of class placements
	classrooms = 4 # Number of classrooms
	coef = 0.85 # One minus Randomness in the algorithm's run decision.
In the system there is clustering for old shcools and old classrooms. This may reduce the real clusters and you may need to adjust the threshold, or remove the clustering.

The system can accept students that are pre-placed in classrooms, before the optimization runs.

### student_file_creator.py
The file new_students.xlsx is provided in the directory and should be used for samples as well as to input your own data.
In normal operation, you don't need to run the student_file_creator.py program, which is only for testing.
WARNING: If you accidentally run student_file_creator.py, your new_students.xlsx file will be moved to the backups directory, and the date will be added. The parameters of this excel file are:

	filename = 'new_students.xlsx' # File created for testing
	sheet_name = 'Starting Students' # Data is placed on this sheet
	students_number = 99 # The number of students randomly created
	with_id_proportion = 0.25 # The percentage of students who will ask to be with someone else
	male_proportion = 0.4 # The ratio of boys to girls
	special_needs_proportion = 0.2 # The percentage of special needs students.
	
 Additionally, mock data elements are given at the beginning of the object definition and can be in the form of:

	greek_first_names = ['Alexandros', 'Dimitris', 'Giorgos', 'Konstantinos', 'Andreas', 'Nikolaos', 'Panagiotis', 'Stavros', 'Vasilis', 'Michalis']
	greek_surnames = ['Papadopoulos', 'Karamanlis', 'Giannopoulos', 'Papandreou', 'Koumoutsakos', 'Tsipras', 'Mitsotakis', 'Karatzaféris', 'Liapis', 'Adonis Georgiadis']
	old_schools = ['S1', 'S2', 'S3', 'S4'] # Names of old schools
	old_school_classes = ['OSC1', 'OSC2', 'OSC3'] # Names of old classes
	grades = [5, 4, 3, 2, 1] # Only total grades are used in the program. 

In Preput, we put 1 where we want the student to be placed in a given classroom, and in PreputClassroom, we put the classroom number + 1. 

### validity_of_new_students.py
Checks for errors in new_students.xlsx.
You need to correct the errors to proceed.


# Copyright (c) 2023 Ioannis Chrysochos
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
