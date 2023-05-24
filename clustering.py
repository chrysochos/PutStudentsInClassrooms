import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import AgglomerativeClustering
from fuzzywuzzy import fuzz
# from itertools import combinations
from excel_utils import write_sheet_to_excel

class Clustering:
    def __init__(self, input_file_path, starting_sheet_name, output_sheet_name):
        self.input_file_path = input_file_path
        self.output_sheet_name = output_sheet_name
        self.starting_sheet_name = starting_sheet_name

        # read in the data
        df = pd.read_excel(self.input_file_path, sheet_name=self.starting_sheet_name)

        # concatenate Old School and Old School Class Conc columns
        df['OldSchoolClassFull'] = df['OldSchool'] + ' ' + df['OldSchoolClass']

        # label encode the Old School Class Conc and Old School columns
        le_class = LabelEncoder()
        df['ClassCode'] = le_class.fit_transform(df['OldSchoolClassFull'])

        le_school = LabelEncoder()
        df['SchoolCode'] = le_school.fit_transform(df['OldSchool'])

        # fit Agglomerative Clustering model to the encoded data
        class_cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=20, linkage='ward')
        class_cluster.fit(df[['ClassCode']])

        school_cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=20, linkage='ward')
        school_cluster.fit(df[['SchoolCode']])

        # function to get fuzzy cluster labels
        def get_cluster_labels_fuzzy(data, threshold):
            labels = []
            for i in range(len(data)):
                match_found = False
                for label in labels:
                    if fuzz.token_sort_ratio(data[i], label[0]) > threshold:
                        label.append(i)
                        match_found = True
                        break
                if not match_found:
                    labels.append([data[i], i])
            cluster_labels = [-1] * len(data)
            for i, label in enumerate(labels):
                for data_index in label[1:]:
                    cluster_labels[data_index] = i
            return cluster_labels

        # assign fuzzy class and school labels
        class_labels_fuzzy = get_cluster_labels_fuzzy(df['OldSchoolClassFull'], 90)
        school_labels_fuzzy = get_cluster_labels_fuzzy(df['OldSchool'], 90)

        # add fuzzy labels to dataframe
        df['ClassClusterFuzzy'] = class_labels_fuzzy
        df['SchoolClusterFuzzy'] = school_labels_fuzzy



        # save output to excel
        # Write the new sheet to the Excel file
        # with pd.ExcelWriter(self.input_file_path, engine='openpyxl', mode='a') as writer:
        #     df.to_excel(writer, sheet_name=self.output_sheet_name, index=False)
        write_sheet_to_excel(df, sheet_name= self.output_sheet_name, input_file_path= self.input_file_path)
