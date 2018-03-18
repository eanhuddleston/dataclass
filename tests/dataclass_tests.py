# run with: `python -m tests.dataclass_tests`

from dataclass import dataclass
import unittest


class DataclassTests(unittest.TestCase):
    def test_creates_data_class_with_args_in_string(self):
        PersonData = dataclass('PersonData', 'name age')
        self.assertEqual(PersonData.__name__, 'PersonData')

    def test_creates_data_class_with_args_in_list(self):
        PersonData = dataclass('PersonData', [
            'name',
            'age',
        ])
        self.assertEqual(PersonData.__name__, 'PersonData')

    def test_data_class_instantiates_data_object(self):
        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        self.assertEqual(data_obj.name, 'joe')
        self.assertEqual(data_obj.age, 10)

    def test_allowed_attrs_mutable(self):
        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        data_obj.name = 'bob'
        self.assertEqual(data_obj.name, 'bob')

    def test_you_cant_assign_new_attrs(self):
        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        with self.assertRaises(Exception):
            data_obj.random_thing = 'blah'

    def test_attrs_not_set_at_init_default_to_none(self):
        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe')
        data_obj.age = 100
        self.assertEqual(data_obj.age, 100)

    def test_not_inititialized_attrs_can_be_changed(self):
        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe')
        self.assertEqual(data_obj.age, None)

    def test_supports_object_equality_comparison(self):
        PersonData = dataclass('PersonData', 'name age')
        person1 = PersonData(name='joe', age=10)
        person2 = PersonData(name='joe', age=10)
        self.assertEqual(person1, person2)
        person2.name = 'bob'
        self.assertNotEqual(person1, person2)

    def test_data_objects_not_equal_if_different_classes(self):
        PersonData = dataclass('PersonData', 'name age')
        CityData = dataclass('CityData', 'name age')

        person = PersonData(name='joe', age=10)
        city = CityData(name='joe', age=10)

        self.assertNotEqual(person, city)

    def test_supports_not_equal_comparison(self):
        PersonData = dataclass('PersonData', 'name age')
        person1 = PersonData(name='joe', age=10)
        person2 = PersonData(name='bob', age=10)
        self.assertTrue(person1 != person2)

    def test_to_dict_works(self):
        expected = {'name': 'joe', 'age': 10}

        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        json = data_obj.to_json()
        self.assertEqual(json, expected)

    def test_str_method_works(self):
        expected = "<PersonData name: 'joe'; age: 10>"

        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        self.assertEqual(str(data_obj), expected)

    def test_repr_method_works(self):
        expected = "PersonData(name='joe', age=10)"

        PersonData = dataclass('PersonData', 'name age')
        data_obj = PersonData(name='joe', age=10)
        self.assertEqual(repr(data_obj), expected)

    def test_creates_multiple_data_classes(self):
        PersonData = dataclass('PersonData', 'name age')
        CityData = dataclass('CityData', 'name population')
        self.assertEqual(PersonData.__name__, 'PersonData')
        self.assertEqual(CityData.__name__, 'CityData')

        person = PersonData(name='joe', age=10)
        self.assertEqual(person.name, 'joe')
        self.assertEqual(person.age, 10)

        city = CityData(name='St. Andrews', population=20)
        self.assertEqual(city.name, 'St. Andrews')
        self.assertEqual(city.population, 20)

        self.assertNotEqual(person, city)


if __name__ == '__main__':
    unittest.main()
