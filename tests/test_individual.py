import unittest
from Familytree.individual import Person
from Familytree import variables


class Testperson(unittest.TestCase):

    def setUp(self):
        self.person = Person(1, "Jane", "Female")

    def test_initialization(self):
        # check instance
        self.assertEqual(isinstance(self.person, Person), True)

        # check properties
        self.assertEqual(self.person.id, 1)
        self.assertEqual(self.person.name, "Jane")
        self.assertEqual(self.person.gender, "Female")
        self.assertEqual(self.person.mother, None)
        self.assertEqual(self.person.father, None)
        self.assertEqual(self.person.spouse, None)
        self.assertEqual(self.person.children, [])

    def test_assign_mother(self):
        mother_error_case = "error_value"
        mother_error_male_case = Person(2, "male_person", "Male")
        mother_success_case = Person(3, "Mother", "Female")

        # error case
        self.assertRaises(ValueError, self.person.assign_mother, mother_error_case)
        self.assertRaises(ValueError, self.person.assign_mother, mother_error_male_case)

        # success case
        self.person.assign_mother(mother_success_case)
        self.assertEqual(self.person.mother.name, "Mother")
        self.assertTrue(self.person.mother.gender, "Female")

    def test_assign_father(self):
        father_error_case = "error_value"
        father_error_female_case = Person(2, "female_father", "Female")
        father_success_case = Person(3, "Father", "Male")

        # error cases
        self.assertRaises(ValueError, self.person.assign_father, father_error_case)
        self.assertRaises(ValueError, self.person.assign_father, father_error_female_case)

        # success case
        self.person.assign_father(father_success_case)
        self.assertEqual(self.person.father.name, "Father")
        self.assertTrue(self.person.father.gender, "Male")

    def test_assign_spouse(self):
        spouse_error_case = "error_value"
        spouse_error_same_gender = Person(2, "same_gender_spouse", "Female")
        spouse_success_case = Person(3, "Husband", "Male")

        # error cases
        self.assertRaises(ValueError, self.person.assign_spouse, spouse_error_case)
        self.assertRaises(ValueError, self.person.assign_spouse, spouse_error_same_gender)

        # success case
        self.person.assign_spouse(spouse_success_case)
        self.assertEqual(self.person.spouse.name, "Husband")
        self.assertEqual(self.person.spouse.gender, "Male")

    def test_add_children(self):
        child_error_case = "error_Case"
        child_success_case = Person(4, "Daughter", "Female")

        # error case
        self.assertRaises(ValueError, self.person.add_children, child_error_case)

        # success case
        self.person.add_children(child_success_case)
        self.assertEqual(len(self.person.children), 1)
        self.assertEqual(self.person.children[0].name, "Daughter")
        self.assertEqual(self.person.children[0].gender, "Female")


if __name__ == '__main__':
    unittest.main()
