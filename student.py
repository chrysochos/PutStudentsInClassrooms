

class Student():
    def __init__(self, student_id, characteristics):
        self.student_id = student_id
        self.first_name = characteristics['first_name']
        self.middle_name = characteristics['middle_name']
        self.family_name = characteristics['family_name']
        self.gender = characteristics['gender']
        self.with_id = characteristics['with_id']
        self.old_school = characteristics['old_school']
        self.old_school_class = characteristics['old_school_class']
        self.g1 = characteristics['g1']
        self.g2 = characteristics['g2']
        self.g3 = characteristics['g3']
        self.g4 = characteristics['g4']
        self.g5 = characteristics['g5']
        self.mean_value = characteristics['mean_value']
        self.special_needs = characteristics['special_needs']
        self.notes = characteristics['notes']
        self.old_school_classroom = characteristics['old_school_classroom']
        self.old_school = characteristics['old_school']
        self.preput = characteristics['preput']
        self.preput_classroom = characteristics['preput_classroom']
    
    def print_score(self):
        print('%s:%s' % (self.name, self.score))    
        return None


    def assign_group(self, group):
        self.group = group
        self.group_id = group.group_id