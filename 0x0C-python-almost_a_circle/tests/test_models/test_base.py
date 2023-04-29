import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    def test_no_arg1(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(1, b2.id - b1.id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(-1, b1.id - b2.id)

    def test_no_arg2(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(2, b3.id - b1.id)

    def test_one_arg(self):
        b = Base(98)
        self.assertEqual(98, b.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_nb_instance_after_unique_id(self):
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(2)
        b.id = 10
        self.assertEqual(10, b.id)

    def test_nb_instance_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instance)

    def test_char_id(self):
        self.assertEqual('A', Base('A').id)

    def test_str_id(self):
        self.assertEqual("betty", Base("betty").id)

    def test_float_id(self):
        self.assertEqual(3.5, Base(3.5).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)

    def test_complex_id(self):
        self.assertEqual(complex(2), Base(complex(2)).id)

    def test_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(2, 8, 1, 1, 98)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 98)

class TestBase_save_to_file(unittest.TestCase):

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(7, 5, 1, 6, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 52)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(7, 5, 1, 6, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 104)

    def test_save_to_file_one_square(self):
        s = Square(7, 5, 1, 6)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_two_squares(self):
        s1 = Square(7, 5, 1, 6)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 76)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(7, 5, 1, 6)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(7, 5, 1, 6)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": "hello", "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_type_square(self):
        list_input = [{"id": "hello", "size": 16}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 1, "width": 5, "height": 7, "x": 2, "y": 2}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 5, "height": 5, "x": 2, "y": 4},
            {"id": 98, "width": 7, "height": 4, "x": 1, "y": 5},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"size": 4, "id": 98, "y": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"size": 16, "id": 10, "x": 2},
            {"size": 5, "id": 1, "x": 1}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 98)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_initial(self):
        r1 = Rectangle(2, 1, 2, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 2/2 - 2/1", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(2, 1, 2, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 2/2 - 2/1", str(r2))

    def test_create_rectangle_is_not(self):
        r1 = Rectangle(2, 1, 2, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_not_equals(self):
        r1 = Rectangle(2, 1, 2, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_initial(self):
        s1 = Square(2, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 1/2 - 2", str(s1))

    def test_create_square_new(self):
        s1 = Square(2, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 1/2 - 2", str(s2))

    def test_create_square_is_not(self):
        s1 = Square(2, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_not_equals(self):
        s1 = Square(2, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(objs) == Rectangle for objs in output))

    def test_load_from_file_first_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(objs) == Square for objs in output))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 98)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,1,2,3,4", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,1,2,3,4\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("4,1,2,3", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("4,1,2,3\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(1, 2, 3, 4)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("4,1,2,3", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(5, 3, 8, 1)
        Square.save_to_file_csv([s])
        s = Square(1, 2, 3, 4)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("4,1,2,3", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 98)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_objs = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_objs[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_objs = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_objs[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file_csv([r1, r2])
        list_objs = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(o) == Rectangle for o in list_objs))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file_csv([s1, s2])
        list_squares_objs = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_objs[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file_csv([s1, s2])
        list_squares_objs = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_objs[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)
        Square.save_to_file_csv([s1, s2])
        list_objs = Square.load_from_file_csv()
        self.assertTrue(all(type(o) == Square for o in list_objs))

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 98)

if __name__ == "__main__":
    unittest.main()
