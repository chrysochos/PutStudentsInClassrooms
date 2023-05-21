


import random
import numpy as np
import pandas as pd


# we have groups of students with the same characteristics as one classroom.
# each group has 3 counters: the number of students, special needs and the sum of the grade of each student. 
# The special needs in an integer number which is equal or less than the number of students in the group.
# the number os special needs is a random number between 0 and the number of students in the group and only 20% of the groups have special needs.
# the sum of the grade of each student is a random number between 0 and 10.
# the number of groups is a given number.
# the number of students in each group is a random number between 0 and 3.


filepath = "StGrs.xlsx"
df1 = pd.read_excel(filepath, sheet_name='Groups')
new_header = ['males','females','specialneeds','ggrade']
df1.columns = new_header

males = 0
females = 0
special_needs=0
sum_of_grades=0


groups_list = []

for idx1, kk in df1.iterrows():
    groups_list.append([idx1,int(kk[0]),int(kk[1]),int(kk[2]),kk[3]])

groups = len(groups_list)

for i in range(groups):
    males += int(groups_list[i][1])
    females += int(groups_list[i][2])
    special_needs += int(groups_list[i][3])
    sum_of_grades += groups_list[i][4]
print()
print()
print("Number of males:",males)
print("Number of females:",females)
print("Number of special_needs:",special_needs)
print("Sum of grades:",sum_of_grades)
print()




# we must have four classrooms
classrooms = 4
classrooms_list = []
def create_classrooms(classrooms):
    #each classroom has its number and list of 3 counters: the number of students, special needs and the sum of the grade of each student.
    classrooms_list.clear()
    for i in range(classrooms):
        classrooms_list.append([i,0,0,0,0])
        #print (classrooms_list[i])
    return classrooms_list

classrooms_list = create_classrooms(classrooms)


# create a function to place a group in a classroom. It must add the counters of the group to the counters of the classroom.
# It must return True if the group was placed in the classroom and False if the group was not placed in the classroom.
def place_group_in_classroom(group,classroom):  
    #print(" Please place group",group,"in classroom",classroom)
    #if classrooms_list[classroom][1] + group[0] > 23:
    #     return False
    # if classrooms_list[classroom][2] + group[1] > classrooms_list[classroom][0]:
    #     return False
    classrooms_list[classroom][1] += group[1]
    classrooms_list[classroom][2] += group[2]
    classrooms_list[classroom][3] += group[3]
    classrooms_list[classroom][4] += group[4]


    # add the group and the classroom number to the classrooms_content list
    classrooms_content.append([classrooms_list[classroom][0],group])
   
    return True    

#define a classroms_content list to store the content of the classrooms with the groups and the number of classrom


# placement of the groups in the classrooms
def placement_of_groups_in_classrooms(groups_list,classrooms_list):

    # for each group in the groups_list
    for i in range(len(groups_list)):

        # we must decide where to place the group
        # we must place the group in the classroom with the less number of students, special needs and sum of grades
        needs = []
        for j in range(len(classrooms_list)):
            dif_males = classrooms_list[j][1] - groups_list[i][1]
            dif_females = classrooms_list[j][2] - groups_list[i][2]
            dif_specialneeds = classrooms_list[j][3] - groups_list[i][3]
            dif_ggrades = classrooms_list[j][4] - groups_list[i][4]
   
            coef = 0.85
            coef1 = random.uniform(coef, 1)
            coef2 = random.uniform(coef, 1)
            coef3 = random.uniform(coef, 1)
            coef4 = random.uniform(coef, 1)
            needs.append([j, coef1*dif_males +coef2*dif_females + coef3*dif_specialneeds + coef4*dif_ggrades ]) #* random.uniform(0.9, 1)])

        max_val = min(needs, key=lambda x: x[1])
        choose_class = max_val[0]
        #print(classrooms_list)
        #print('choose_class=',choose_class )

 
        if place_group_in_classroom(groups_list[i],classrooms_list[choose_class][0]):
                # stop the loop
                pass
        else:
            # if the group was not placed in any classroom
            print ("The group",i,"was not placed in any classroom")

classrooms_content = []

previous_solution_cost = 1000000000
# for a range of 10 do the following
iterations = 2000
for j in range(iterations):
    classrooms_content.clear()

    create_classrooms(classrooms)
    

    placement_of_groups_in_classrooms(groups_list,classrooms_list)

    # # print the content of the classrooms
    # for i in range(classrooms):
    #     print ("Classroom",i,classrooms_list[i])
    # print ()

    # print the content of the classrooms
    np_array = np.array(classrooms_list)
    variances = np.var(np_array, axis=0)
    # print(variances)
    # I want to normalize the variances in order to add them. How can I do it?
    # print("variance of students:",variances[1]/students)
    # print("variance of special needs:",variances[2]/special_needs)
    # print("variance of grades:",variances[3]/sum_of_grades)
    # I want to normalize the variances in order to add them. How can I do it? 
    solution_cost = variances[1]/males + variances[2]/special_needs + variances[3]/sum_of_grades
    #print("Solution Cost:",solution_cost)

    # check if value_i is smaller than current minimum value


    if solution_cost < previous_solution_cost:
        previous_solution_cost = solution_cost
        min_iteration = j
        best_classrooms_content = classrooms_content.copy()
        best_classrooms_list = classrooms_list.copy()
        pass
    # previous_solution_cost = solution_cost

print("Minimum Solution Cost", previous_solution_cost, "was found at iteration", min_iteration, "out of", iterations, "iterations")
print()
# print("Best classrooms content",best_classrooms_content)
# print()

print("Groups by classroom")
groups_by_classroom = {}
for item in best_classrooms_content:
    classroom, group_info = item
    group_number = group_info[0]
    if classroom not in groups_by_classroom:
        groups_by_classroom[classroom] = []
    groups_by_classroom[classroom].append(group_number)



# Read the Groups from the excel file from the sheet Groups
filepath = "groups.xlsx"
df = pd.read_excel(filepath, sheet_name='Groups')


# Find the groups for each classroom and the classrooms for each group
list_of_groups_to_classrooms = []
output_dict = {}
# find the groups for each classroom and the classrooms for each group
#print(groups_by_classroom)
sorted_keys = sorted(groups_by_classroom.keys())
for key in sorted_keys:
    print(key, groups_by_classroom[key])
    for element in groups_by_classroom[key]:

        # If the number is not already a key in the output dictionary, add it with an empty list
        if element not in output_dict:
            output_dict[element] = []
        # Append the original key to the list for this number
        output_dict[element].append(key)

for key in sorted(output_dict.keys()):
    # print(f"{key}: {output_dict[key]}")
    list_of_groups_to_classrooms.append(output_dict[key])
    # we need to iterate the students which are give by the index of df.
    for index, row in df.iterrows():
        # check the GroupN of the student to have 'Group_' plust the same value with the key
        if str(row['GroupN']).strip() == 'Group_' + str(key):
            # Put in the column Classroom the output_dict[key]
            df.at[index, 'Classroom'] = output_dict[key]
            # print('Βάλε μαθητή ' ,index+1,' από το Group ',key, ' στην τάξη ', output_dict[key][0])
            pass

# save the dataframe to excel
df.to_excel('final.xlsx', index=False)

# save the dataframe to excel
df.to_excel('final.xlsx', index=False)

# print the content of the classrooms
print()
print("Best classrooms list")
for element in best_classrooms_list:
    print(element)
pass

print()
print("Minimum Solution Cost", previous_solution_cost, "was found at iteration", min_iteration, "out of", iterations, "iterations")
print()



pass




