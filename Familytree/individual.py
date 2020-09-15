from Familytree import variables


class Person:
    # A person class with the details corresponding to his family initialized with only his name, gender
    # can be added only through mother apart from the initialization of family tree.
    def __init__(self, num, name, gender):
        self.id = num
        self.name = name
        self.gender = gender
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    # assigning mother details
    def assign_mother(self, mother):
        if not isinstance(mother, Person):
            raise ValueError('Invalid value for mother')
        if mother.gender not in variables.Gender[variables.female]:
            raise ValueError(
                'Invalid gender value for mother.'
                'Mother should be a Female'
            )
        self.mother = mother

    # assigning father details.
    def assign_father(self, father):
        if not isinstance(father, Person):
            raise ValueError('Invalid value for father')
        if father.gender not in variables.Gender[variables.male]:
            raise ValueError(
                'Invalid gender value for father.'
                'Father should be a Male'
            )
        self.father = father

    # assigning spouse incase if there is any.
    def assign_spouse(self, spouse):
        if not isinstance(spouse, Person):
            raise ValueError('Invalid value for spouse')
        if self.gender == spouse.gender:
            raise ValueError(
                'Invalid gender value for spouse.'
                'Spouse and member cannot have the same gender.'
            )
        self.spouse = spouse

    # adding children for parents when ever a new child is added.
    def add_children(self, child):
        if not isinstance(child, Person):
            raise ValueError('Invalid value for child')
        self.children.append(child)
