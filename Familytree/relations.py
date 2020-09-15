from Familytree import variables


class Relations:

    def __init__(self):
        pass

    def get_mother(self, member):
        if not member.mother:
            return None
        return [member.mother]

    def get_father(self, member):
        if not member.father:
            return None
        return [member.father]

    # get mother of father for the requested member, used for getting the relations attached to her
    def get_paternal_grandmother(self, member):
        if not member.father:
            return None
        if not member.father.mother:
            return None
        return member.father.mother

    # get mother of mother for the requested member, used for getting the relations attached to her
    def get_maternal_grandmother(self, member):
        if not member.mother:
            return None
        if not member.mother.mother:
            return None
        return member.mother.mother

    # get mother of spouse for the requested member, used for getting the relations attached to her
    def get_spouse_mother(self, member):
        if not member.spouse:
            return None
        if not member.spouse.mother:
            return None
        return member.spouse.mother

    # using fathers mother getting the female siblings
    def get_paternal_aunt(self, member):
        grandmother = self.get_paternal_grandmother(member)
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.female],
                grandmother.children
            )
        )

    # Using fathers mother getting  the male siblings
    def get_paternal_uncle(self, member):
        grandmother = self.get_paternal_grandmother(member)
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.male] and x.name != member.father.name,
                grandmother.children
            )
        )

    # Getting mothers sisters using her mother
    def get_maternal_aunt(self, member):
        grandmother = self.get_maternal_grandmother(member)
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.female] and x.name != member.mother.name,
                grandmother.children
            )
        )

    # Getting mothers brothers using her mother
    def get_maternal_uncle(self, member):
        grandmother = self.get_maternal_grandmother(member)
        if not grandmother:
            return []
        if not grandmother.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.male],
                grandmother.children
            )
        )

    # Getting spouses of siblings using siblings
    def get_sibling_spouses(self, member):
        siblings = self.get_siblings(member)
        if not siblings:
            return []
        sibling_spouses = [
            sibling.spouse for sibling in siblings if sibling.spouse
        ]
        return sibling_spouses

    def get_spouse_siblings(self, member):
        if not member.spouse:
            return []
        return self.get_siblings(member.spouse)

    def get_brother_in_law(self, member):
        results = self.get_sibling_spouses(member) + self.get_spouse_siblings(member)
        if not results:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.male],
                results
            )
        )

    def get_sister_in_law(self, member):
        results = self.get_sibling_spouses(member) + self.get_spouse_siblings(member)
        if not results:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.female],
                results
            )
        )

    def get_son(self, member):
        if not member.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.male],
                member.children
            )
        )

    def get_daughter(self, member):
        if not member.children:
            return []
        return list(
            filter(
                lambda x: x.gender in variables.Gender[variables.female],
                member.children
            )
        )

    def get_siblings(self, member):
        if not member.mother:
            return []
        if not member.mother.children:
            return []
        return list(
            filter(
                lambda x: x.name != member.name,
                member.mother.children
            )
        )

    # calling the appropriate method for the required relation
    # getting back the results to the get_relationship method in family creation module
    def get_relation(self, member, relationship_type):
        switch = {
            'Mother': self.get_mother(member),
            'Father': self.get_father(member),
            'Son': self.get_son(member),
            'Daughter': self.get_daughter(member),
            'Siblings': self.get_siblings(member),
            'Paternal-Uncle': self.get_paternal_uncle(member),
            'Paternal-Aunt': self.get_paternal_aunt(member),
            'Maternal-Uncle': self.get_maternal_uncle(member),
            'Maternal-Aunt': self.get_maternal_aunt(member),
            'Brother-In-Law': self.get_brother_in_law(member),
            'Sister-In-Law': self.get_sister_in_law(member)
        }

        relationship = switch.get(
            relationship_type, None)

        if relationship == [] or relationship is None:
            return None
        else:
            return relationship
