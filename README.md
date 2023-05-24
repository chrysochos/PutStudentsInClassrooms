ΕΚΤΕΛΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ
## classrooms_groups_analyzer.py 
Το κυρίως πρόγραμμα είναι το classrooms_groups_analyzer.py το οποίο έχει τις πιο κάτω παραμέτρους:

    iterations = 2000  # Δοκιμές που κάνει για να βρει την βέλτιστη.
    file_path = 'new_students.xlsx' # Το αρχείο εργασίας
    starting_sheet_name = 'Starting Students' # Το φύλλο με τα πραγματικά δεδομένα
    sheet_name = 'Students' # Η αντίληψη του προγράμματος για τους μαθητές
	output_sheet_name = 'Results' # Τα αποτελέσματα της τοποθέτησης σε τάξεις
    classrooms = 4 # Αριθμός τάξεων
    coef = 0.85 # Τυχαιότητα στην απόφαση του αλγόριθμου.

## student_file_creator.py
Το αρχείο new_students.xlsx δίνεται μέσα στο directory και αυτό πρέπει να χρησιμοποιείται για δείγμα αλλά και για να βάλετε μέσα τα δικά σας δεδομένα. 
Στην κανονική λειτουργία δεν χρειάζεστε να τρέχετε το πρόγραμμα δημιουργία τυχαίων μαθητών student_file_creator.py το οποίο είναι μόνο για δοκιμές.
ΠΡΟΣΟΧΗ: Αν κατά λάθος το τρέξετε το student_file_creator.py το δικός σας αρχείο new_students.xlsx θα μεταφερθεί στο directory backups και θα προστεθεί η ημερομηνία.

	filename = 'new_students.xlsx'  # Αρχείο που δημιουργείται για δοκιμές
	sheet_name = 'Starting Students' # Τα δεδομένα τοποθετούνται στο φύλλο αυτό
	students_number = 99  # Ο αριθμός των μαθητών που δημιουργούνται τυχαία
	with_id_proportion = 0.25  # Το ποσοστό των μαθητών που θα ζητήσουν να πάνε με κάποιο άλλο
	male_proportion = 0.4  # Η αναλογία αγοριών και κοριτσιών
	special_needs_proportion = 0.2 # Το ποσοστό των ειδικών αναγκών.

## validity_of_new_students.py
Εξετάζει αν υπάρχουν λάθη στο new_students.xlsx.
Πρέπει να διορθώσετε τα λάθη για να προχωρήσετε.


# Copyright (c) 2023 Ioannis Chrysochos
# This is done by Ioannis Chrysochos
# All rights reserved.
