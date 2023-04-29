#!/usr/bin/python3


import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(8, 9)
        s2 = Square(9, 8)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(5, 6, 7)
        s2 = Square(2, 3, 4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(Square(10, 2, 2, 7).id, 7)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_is_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5, 1, 0, 1).__size)

    def test_size_getter(self):
        self.assertEqual(Square(5, 2, 3, 9).size, 5)

    def test_size_setter(self):
        s = Square(1, 2, 3, 4)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_width_getter(self):
        s = Square(1, 2, 3, 4)
        s.size = 5
        self.assertEqual(s.width, 5)

    def test_height_getter(self):
        s = Square(1, 2, 3, 4)
        s.size = 5
        self.assertEqual(s.height, 5)

    def test_x_getter(self):
        self.assertEqual(Square(5).x, 0)

    def test_y_getter(self):
        self.assertEqual(Square(5).y, 0)


class TestSquare_size_arg(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""
    # test size types
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("NotAnInt")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.0)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(2))

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"size": 1, "x": 2, "y": 3})

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # test size value
    def test_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1, 2)


class TestSquare_x_arg(unittest.TestCase):
    """Unittests for testing x initialization of the Square class."""
    # test x types
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "NotAnInt")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, 2.0)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, complex(2))

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, [1, 2, 3])

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"x": 1, "x": 2, "y": 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, (1, 2, 3))

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(15, {1, 2, 3})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, True)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(12, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))

    # test x value
    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2)


class TestSquare_y_arg(unittest.TestCase):
    """Unittests for testing y initialization of the Square class."""
    # test y types
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 4, "NotAnInt")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 7, 2.0)

    def test_compley_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, complex(2))

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 2, [1, 2, 3])

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 7, {"y": 1, "y": 2, "y": 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 1, (1, 2, 3))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(15, 2, {1, 2, 3})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 5, True)

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(12, 0, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, float('nan'))

    # test y value
    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 3, -5)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", 1, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "x", "y")

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size", "x", 1)


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_one_arg(self):
        s = Square(7, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.area(0)

    def test_area(self):
        self.assertEqual(Square(999999, 0, 0, 10).area(), 999998000001)

    def test_area_changed_attributes(self):
        s = Square(7, 1, 1, 0)
        s.size = 5
        self.assertEqual(25, s.area())

if __name__ == "__main__":
    unittest.main()
