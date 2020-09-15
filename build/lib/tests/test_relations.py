import unittest
from Familytree.individual import Person
from Familytree.relations import Relations
from Familytree import variables
from unittest.mock import patch, Mock
from tests import mock_member_creation


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.member = Person(1, "Hubby", "Male")

    def test_get_paternal_grandmother(self):
        member = Person(7, "alpha", "Male")
        father = Person(8, "beta", "Male")
        grandmother = Person(9, "charlie", "Female")

        # error cases
        self.assertEqual(Relations().get_paternal_grandmother(member), None)

        member.father = father
        self.assertEqual(Relations().get_paternal_grandmother(member), None)

        member.father.mother = grandmother
        self.assertEqual(Relations().get_paternal_grandmother(member), grandmother)

    def test_get_maternal_grandmother(self):
        member = Person(7, "alpha", "Male")
        mother = Person(8, "beta", "Female")
        grandmother = Person(9, "charlie", "Female")

        # error cases
        self.assertEqual(Relations().get_paternal_grandmother(member), None)

        member.mother = mother
        self.assertEqual(Relations().get_paternal_grandmother(member), None)

        member.mother.mother = grandmother
        self.assertEqual(Relations().get_maternal_grandmother(member), grandmother)

    def test_get_spouse_mother(self):
        member = Person(7, "alpha", "Male")
        spouse = Person(8, "alpha_spouse", "Female")
        spouse_mother = Person(9, "alpha_spousemother", "Female")

        # error cases
        self.assertEqual(Relations().get_spouse_mother(member), None)

        member.spouse = spouse
        self.assertEqual(Relations().get_spouse_mother(member), None)

        member.spouse.mother = spouse_mother
        self.assertEqual(Relations().get_spouse_mother(member), spouse_mother)

    @patch('Familytree.relations.Relations.get_paternal_grandmother', side_effect=[
        None,
        mock_member_creation(),
        mock_member_creation(children=[Person(3, "Father", "Male")]),
        mock_member_creation(children=[
            Person(3, "Father", "Male"),
            Person(4, "Uncle", "Male")
        ]),
        mock_member_creation(children=[
            Person(3, "Father", "Male"),
            Person(4, "Uncle", "Male"),
            Person(5, "Aunt", "Female")
        ])
    ])
    def test_get_paternal_aunt(self, mock_get_paternal_grandmother):
        # check if get_paternal_grandmother has been replaced by a mock
        self.assertEqual(
            isinstance(Relations.get_paternal_grandmother, Mock),
            True
        )
        self.assertEqual(Relations().get_paternal_aunt(self.member), [])
        self.assertEqual(Relations().get_paternal_aunt(self.member), [])
        self.assertEqual(Relations().get_paternal_aunt(self.member), [])
        self.assertEqual(Relations().get_paternal_aunt(self.member), [])

        paternal_aunts = Relations().get_paternal_aunt(self.member)
        self.assertEqual(len(paternal_aunts), 1)
        self.assertEqual(paternal_aunts[0].name, "Aunt")
        self.assertTrue(paternal_aunts[0].gender in variables.Gender[variables.female])

        # to check that the mock_get_paternal_grandmother was called instead
        # of self.member.get_paternal_grandmother
        mock_get_paternal_grandmother.assert_called_with(self.member)

    @patch('Familytree.relations.Relations.get_paternal_grandmother', side_effect=[
        None,
        mock_member_creation(),
        mock_member_creation(children=[Person(3, "Father", "Male")]),
        mock_member_creation(children=[
            Person(3, "Aunt", "Female"),
            Person(4, "Father", "Male")
        ]),
        mock_member_creation(children=[
            Person(3, "Father", "Male"),
            Person(4, "Uncle", "Male"),
            Person(5, "Aunt", "Female")
        ])
    ])
    def test_get_paternal_uncle(self, mock_get_paternal_grandmother):
        self.member.father = Person(3, "Father", "Male")
        # check if get_paternal_grandmother has been replaced by a mock
        self.assertEqual(isinstance(
            Relations().get_paternal_grandmother, Mock),
            True
        )

        self.assertEqual(Relations().get_paternal_uncle(self.member), [])
        self.assertEqual(Relations().get_paternal_uncle(self.member), [])
        self.assertEqual(Relations().get_paternal_uncle(self.member), [])
        self.assertEqual(Relations().get_paternal_uncle(self.member), [])

        paternal_uncle = Relations().get_paternal_uncle(self.member)
        self.assertEqual(len(paternal_uncle), 1)
        self.assertEqual(paternal_uncle[0].name, "Uncle")
        self.assertTrue(paternal_uncle[0].gender in variables.Gender[variables.male])

        # to check that the mock_get_paternal_grandmother was called instead
        # of self.member.get_paternal_grandmother
        mock_get_paternal_grandmother.assert_called_with(self.member)

    @patch('Familytree.relations.Relations.get_maternal_grandmother', side_effect=[
        None,
        mock_member_creation(),
        mock_member_creation(children=[Person(3, "Mother", "Female")]),
        mock_member_creation(children=[
            Person(3, "Mother", "Female"),
            Person(4, "Uncle", "Male")
        ]),
        mock_member_creation(children=[
            Person(3, "Mother", "Female"),
            Person(4, "Uncle", "Male"),
            Person(5, "Aunt", "Female")
            ])
    ])
    def test_get_maternal_aunt(self, mock_get_maternal_grandmother):
        self.member.mother = Person(3, "Mother", "Female")
        # check if get_paternal_grandmother has been replaced by a mock
        self.assertEqual(isinstance(
            Relations.get_maternal_grandmother, Mock),
            True
        )

        self.assertEqual(Relations().get_maternal_aunt(self.member), [])
        self.assertEqual(Relations().get_maternal_aunt(self.member), [])
        self.assertEqual(Relations().get_maternal_aunt(self.member), [])
        self.assertEqual(Relations().get_maternal_aunt(self.member), [])

        maternal_aunts = Relations().get_maternal_aunt(self.member)
        self.assertEqual(len(maternal_aunts), 1)
        self.assertEqual(maternal_aunts[0].name, "Aunt")
        self.assertTrue(maternal_aunts[0].gender in variables.Gender[variables.female])

        # to check that the mock_get_paternal_grandmother was called instead of
        # self.member.get_paternal_grandmother
        mock_get_maternal_grandmother.assert_called_with(self.member)

    @patch('Familytree.relations.Relations.get_maternal_grandmother', side_effect=[
        None,
        mock_member_creation(),
        mock_member_creation(children=[Person(3, "Mother", "Female")]),
        mock_member_creation(children=[
            Person(3, "Aunt", "Female"),
            Person(4, "Mother", "Female")
        ]),
        mock_member_creation(children=[
            Person(3, "Mother", "Female"),
            Person(4, "Uncle", "Male"),
            Person(5, "Aunt", "Female")
        ])
    ])
    def test_get_maternal_uncle(self, mock_get_maternal_grandmother):
        # check if get_paternal_grandmother has been replaced by a mock
        self.assertEqual(
            isinstance(Relations.get_maternal_grandmother, Mock),
            True
        )

        self.assertEqual(Relations().get_maternal_uncle(self.member), [])
        self.assertEqual(Relations().get_maternal_uncle(self.member), [])
        self.assertEqual(Relations().get_maternal_uncle(self.member), [])
        self.assertEqual(Relations().get_maternal_uncle(self.member), [])

        maternal_uncle = Relations().get_maternal_uncle(self.member)
        self.assertEqual(len(maternal_uncle), 1)
        self.assertEqual(maternal_uncle[0].name, "Uncle")
        self.assertTrue(maternal_uncle[0].gender in variables.Gender[variables.male])

        # to check that the mock_get_paternal_grandmother was called
        # instead of self.member.get_paternal_grandmother
        mock_get_maternal_grandmother.assert_called_with(self.member)

    @patch('Familytree.relations.Relations.get_siblings', return_value=[
        mock_member_creation(
            name="Alpha", gender='Male', spouse=mock_member_creation(
                name="Beta", gender='Female', spouse=mock_member_creation(
                    name="Alpha")
            )
        ),
        mock_member_creation(
            name="Charlie", gender='Female', spouse=mock_member_creation(
                name="Delta", gender='Male', spouse=mock_member_creation(
                    name="Charlie")
            )
        ),
        mock_member_creation(
            name="Charlie", gender='Female'
        )
    ])
    def test_get_sibling_spouses(self, mock_get_siblings):
        self.assertEqual(len(Relations().get_sibling_spouses(self.member)), 2)

    def test_get_spouse_siblings(self):
        self.assertEqual(len(Relations().get_spouse_siblings(self.member)), 0)
        self.member.spouse = mock_member_creation(name="Wife")
        # spouse_siblings = Relations().get_siblings(self.member.spouse)
        spouse_siblings = [
            mock_member_creation(name="Alpha"),
            mock_member_creation(name="Beta")
        ]
        self.assertEqual(len(spouse_siblings), 2)

    @patch('Familytree.relations.Relations.get_spouse_siblings', return_value=[
        mock_member_creation(name="Alpha", gender='Male'),
        mock_member_creation(name="Beta", gender='Female')
    ])
    @patch('Familytree.relations.Relations.get_sibling_spouses', return_value=[
        mock_member_creation(name="Charlie", gender='Male'),
        mock_member_creation(name="Delta", gender='Female')
    ])
    def test_get_brother_in_law(self, mock_get_sibling_spouses,
                                mock_get_spouse_siblings):
        self.assertEqual(len(Relations().get_brother_in_law(self.member)), 2)

    @patch('Familytree.relations.Relations.get_spouse_siblings', return_value=[
        mock_member_creation(name="Alpha", gender='Male'),
        mock_member_creation(name="Beta", gender='Female')
    ])
    @patch('Familytree.relations.Relations.get_sibling_spouses', return_value=[
        mock_member_creation(name="Charlie", gender='Male'),
        mock_member_creation(name="Delta", gender='Female')
    ])
    def test_get_sister_in_law(self, mock_get_sibling_spouses,
                               mock_get_spouse_siblings):
        self.assertEqual(len(Relations().get_sister_in_law(self.member)), 2)

    def test_get_son(self):
        member = Person(5, "Dummy", "Male")
        son = Person(7, "Son", "Male")
        daughter = Person(7, "Daughter", "Female")

        self.assertEqual(Relations().get_son(member), [])
        member.children.append(daughter)
        self.assertEqual(Relations().get_son(member), [])
        member.children.append(son)
        sons = Relations().get_son(member)
        self.assertEqual(len(sons), 1)
        self.assertEqual(sons[0].name, "Son")
        self.assertTrue(sons[0].gender in variables.Gender[variables.male])

    def test_get_daughter(self):
        member = Person(5, "Dummy", "Male")
        son = Person(7, "Son", "Male")
        daughter = Person(7, "Daughter", "Female")

        self.assertEqual(Relations().get_daughter(member), [])
        member.children.append(son)
        self.assertEqual(Relations().get_daughter(member), [])
        member.children.append(daughter)
        daughters = Relations().get_daughter(member)
        self.assertEqual(len(daughters), 1)
        self.assertEqual(daughters[0].name, "Daughter")
        self.assertTrue(daughters[0].gender in variables.Gender[variables.female])

    def test_get_siblings(self):
        member = Person(5, "Dummy", "Male")
        mother = Person(9, "Mother", "Female")
        son = Person(7, "Son", "Male")
        daughter = Person(7, "Daughter", "Female")

        self.assertEqual(Relations().get_siblings(member), [])
        member.mother = mother
        self.assertEqual(Relations().get_siblings(member), [])
        mother.children.extend([member, son, daughter])
        member.mother = mother
        siblings = Relations().get_siblings(member)
        self.assertEqual(len(siblings), 2)

    @patch('Familytree.relations.Relations.get_siblings')
    @patch('Familytree.relations.Relations.get_daughter')
    @patch('Familytree.relations.Relations.get_son')
    @patch('Familytree.relations.Relations.get_sister_in_law')
    @patch('Familytree.relations.Relations.get_brother_in_law')
    @patch('Familytree.relations.Relations.get_maternal_uncle')
    @patch('Familytree.relations.Relations.get_maternal_aunt')
    @patch('Familytree.relations.Relations.get_paternal_uncle')
    @patch('Familytree.relations.Relations.get_paternal_aunt')
    def test_get_relationship(self, mock_get_paternal_aunt,
                              mock_get_paternal_uncle,
                              mock_get_maternal_aunt, mock_get_maternal_uncle,
                              mock_get_brother_in_law, mock_get_sister_in_law,
                              mock_get_son, mock_get_daughter,
                              mock_get_siblings):
        self.assertEqual(Relations().get_relation(self.member, 'invalid_relation'), None)

        Relations().get_relation(self.member, 'Paternal-Aunt')
        mock_get_paternal_aunt.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Paternal-Uncle')
        mock_get_paternal_uncle.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Maternal-Aunt')
        mock_get_maternal_aunt.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Maternal-Uncle')
        mock_get_maternal_uncle.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Brother-In-Law')
        mock_get_brother_in_law.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Sister-In-Law')
        mock_get_sister_in_law.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Son')
        mock_get_son.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Daughter')
        mock_get_daughter.assert_called_with(self.member)

        Relations().get_relation(self.member, 'Siblings')
        mock_get_siblings.assert_called_with(self.member)


if __name__ == '__main__':
    unittest.main()
