from collections import defaultdict
import pandas as pd
import math

## Create a dictionary of students and their partners
# couples = {
#     1: [2, 3],
#     2: [1, 3],
#     3: [1, 2],
#     4: [5],
#     5: [4],
# }



# Create a function to get the couples
def get_couples(df): 
    # Convert the DataFrame to a dictionary
    couples1 = dict(zip(df['ID'], df['WithID']))
    couples2 = {k: [] if math.isnan(v) else [v] for k, v in couples1.items()}
    couples = {k: [int(x) for x in v] if v else [] for k, v in couples2.items()}
    return couples

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


def get_groups(df):
    # Get the couples
    couples=get_couples(df)

    # Find the groups
    groups = find_groups(couples)

    # Enumerate the items with 'Group1'
    enumerated_groups = [(f'Group_{index}', str(item)[1:-1]) for index, item in enumerate(groups)]

    # Create a pandas dataframe from the enumerated items
    group_df = pd.DataFrame(enumerated_groups, columns=['Index', 'Value'])

    return groups, group_df


# find group characteristics
def find_group_characteristics(students, groups):
    StGrs = []
    # ΞΕΚΙΝΑΜΕ ΑΠΟ ΤΟ ΓΚΡΟΥΠ ΜΗΔΕΝ 0
    for i, group in enumerate(groups):
        gm = 0
        gf = 0
        gsn = 0
        ggrade = 0
        length = len(group)
        if length > 5:
            print('group=', i, ' is too big')
            exit()
           
        for id in group:
            for row in students.values:
                if row[0] == id:                  
                    if row[4]=='M' or row[4]=='m':
                        gm += 1
                    else:
                        gf += 1
                    if row[14]==1:
                        gsn += 1
                    ggrade += row[13]
                    #row[21]=group
                    break
        ggrade = ggrade / length
        ggrade = ggrade / 10
        #print('group=', id, ' Male=',gm,' Female=',gf, ' SpecialNeeds=',gsn, ' Group Grade=',ggrade)
        #print(id, gm, gf, gsn, "{:.2f}".format(ggrade))

        StGrs.append([gm,gf,gsn,ggrade])

    return StGrs

# Write the extra columns to the excel file
def write_extra_columns_to_excel(df, group_df, output_file):
    # open the output file for writing
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter', mode='w')

    # For each student in df, add the group number that it belongs to 'GroupN' column, the size of 'GroupN' in column 'GroupSize'. Put in 'GroupMembers' all the ids of the Students in this GroupN group. Put in 'MeanGroupValue' their average NeanValue
    # we need to iterate over the rows of the dataframe df in order to get the 'id' of each student and all the other columns
    for index, row in df.iterrows():
        current_id = str(row['ID']).strip()
        # Find the first group which has the student in it
        for  index1, value1 in group_df.iterrows():
            students_in_group = value1.Value.split(', ')
            if current_id in students_in_group:
                break

        # Get the group from the group_df dataframe
        group = group_df.loc[index1]
        
        # Add the group number to the 'GroupN' column
        df.loc[index, 'GroupN'] = group['Index']

        # Add the group size to the 'GroupSize' column
        group_members = group['Value'].split(', ')
        group_size = len(group_members)
        df.loc[index, 'GroupSize'] = group_size

        # Add the group members to the 'GroupMembers' column
        df.loc[index, 'GroupMembers'] = group['Value']
    
        # group_mean_value is the sum of the MeanValue of each group member divided by the group size
        group_mean_value1 = 0
        # For each group member, get the MeanValue from the dataframe and sum them up
        for group_member in group_members:
            group_mean_value = float(df[df['ID'] == int(group_member)]['MeanValue'].iloc[0])
            group_mean_value1 = group_mean_value1 + group_mean_value
        # Divide the sum by the group size to get the group mean value
        group_mean_value = group_mean_value1 / group_size

        # if 'MeanGroupValue' column does not exist, create it
        if 'MeanGroupValue' not in df.columns:
            df['MeanGroupValue'] = ''
        df.loc[index, 'MeanGroupValue'] = group_mean_value


    # Write the dataframe to the excel file with sheet name 'Groups' to the first sheet to the output file
    df.to_excel(writer, sheet_name='Groups', index=False)

    writer.close()



# find the groups of students list stgrs = shcool. Write the extra columns to the excel file
def find_stgrs(filepath):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(filepath, sheet_name='Students')

    # Get the groups
    groups, group_df = get_groups(df)

    StGrs = find_group_characteristics(df, groups)
    
    # Write the extra columns to the excel file
    write_extra_columns_to_excel(df, group_df, output_file)
    return StGrs

# Give the input file name of excel file with path
filepath = "new_students.xlsx"

# Give the output file name
output_file = 'groups.xlsx'

StGrs= find_stgrs(filepath)

output_file1 = 'StGrs.xlsx'
# write the StGrs groups to the excel file
def write_groups_to_excel(groups, output_file):
    # open the output file for writing
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter', mode='w')

    # convert the list of groups to a dataframe
    groups_df = pd.DataFrame(groups) 
    # write the dataframe to the excel file
    groups_df.to_excel(writer, sheet_name='Groups', index=False)

    writer.close()

write_groups_to_excel(StGrs, output_file1)

