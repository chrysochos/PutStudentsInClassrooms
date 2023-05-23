import pandas as pd
import math

class ValidityOfNewStudents():
    filename = 'new_students.xlsx'

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(filename, 'Students')

    valitity = 1

    # Check the validity of the ID column
    for i, id in enumerate(df['ID']):
        if not isinstance(id, int):
            print(f"Λάθος ID {id} στην στήλη {i+1}")
            valitity=0

    # Check the validity of the Gender column
    valid_values = ["M", "F"]
    for i, gender in enumerate(df['Gender']):
        if gender not in valid_values:
            print(f"Λάθος τιμή φύλλου στην στήλη  {i+1} ")
            valitity=0

    # Check the validity of the WithID column
    valid_ids = set(df['ID'].tolist())
    for with_id in df[df['WithID'].notna()]['WithID']:
        if with_id != 'WithID' and with_id not in valid_ids:
            print(f"Λάθος WithID τιμή {with_id} στην στήλη WithID")
            valitity=0

    # Check the validity of the SpecialNeeds column
    valid_values = [1,1.0, 0]
    for i, special_needs in enumerate(df['SpecialNeeds']):
        if  special_needs not in valid_values:
            if str(special_needs) =='nan':
                df.at[i, 'SpecialNeeds'] = 0
            else:
                print(f"Λάθος SpecialNeeds τιμή {special_needs} βρέθηκε στην στήλη {i+1}")
                valitity=0

    #check if there are floating values in MeanValues
    # Check the validity of the column containing floating-point numbers
    for i, val in enumerate(df['MeanValue']):
        if not isinstance(val, float):
            print(f"Λάθος MeanValue στην γραμμή {i+1} ")
        elif math.isnan(val):
            print(f"Λάθος MeanValue στην γραμμή {i+1} ")
        elif not math.isfinite(val):
            print(f"Λάθος MeanValue στην γραμμή {i+1} ")

    # replace the empty values of SpecialNeeds with zero
    df['SpecialNeeds'] = df['SpecialNeeds'].fillna(0)

    # replace the empty values of OldSchool with Olds
    for index, row in enumerate(df['OldSchool']):
        if str(row) == 'nan':
            print(f"Γέμισα αυτόματα άδειο κελί OldSchoolClass στην γραμμή {index+1}")
            df.at[index, 'OldSchoolClass'] = 'ΠαλιόΣχολείο'

    # replace the empty values of OldSchoolClass with Olds
    for index, row in enumerate(df['OldSchoolClass']):
        if str(row) == 'nan':
            print(f"Γέμισα αυτόματα άδειο κελί OldSchoolClass στην γραμμή {index+1}")
            df.at[index, 'OldSchoolClass'] = 'ΠαλιάΤάξη'

    if valitity == 0:
        print('ΠΡΟΒΛΗΜΑΤΙΚΕΣ ΤΙΜΕΣ ΣΤΟΝ ΠΙΝΑΚΑ new_students.xlsx ΚΟΙΤΑΞΕ ΤΑ ΠΙΟ ΠΑΝΩ ΣΧΟΛΙΑ.')
        exit()
def main():
    ValidityOfNewStudents()
if __name__ == '__main__':
    main()  
