#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):

    def test_is_base(self):
        self.assertIsInstance(Rectangle(10, 10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Rectangle(10, 10), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        s1 = Rectangle(8, 9)
        s2 = Rectangle(9, 8)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Rectangle(5, 6, 7)
        s2 = Rectangle(2, 3, 4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        s1 = Rectangle(5, 6, 7, 8)
        s2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(10, 2, 2, 7, 1).id, 1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_is_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 1, 1).__width)

    def test_is_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 1, 1).__height)

    def test_is_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 1, 1).__x)

    def test_is_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 1, 0, 1, 1).__y)

    def test_width_getter(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 1).width, 1)

    def test_width_setter(self):
        s = Rectangle(1, 2, 3, 4, 1)
        s.width = 5
        self.assertEqual(s.width, 5)

    def test_height_getter(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 1).height, 2)

    def test_height_getter(self):
        s = Rectangle(1, 2, 3, 4, 1)
        s.height = 5
        self.assertEqual(s.height, 5)

    def test_x_getter(self):
        self.assertEqual(Rectangle(5, 6).x, 0)

    def test_y_getter(self):
        self.assertEqual(Rectangle(5, 6).y, 0)


class TestRectangle_width_arg(unittest.TestCase):
    """Unittests for testing width of the Rectangle class."""
    # Test width types
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("NotAnInt", 3)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.0, 5)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 7)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 7)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"width": 1, "x": 2, "y": 3}, 1)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2, 3, 4)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 4, 0, 5)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 10)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 11)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 12)

    # test width value
    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 13)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 2)


class TestRectangle_height_arg(unittest.TestCase):
    """Unittests for testing height of the Rectangle class."""
    # Test height types
    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None, 2, 2, 0)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "NotAnInt", 3, 2, 1)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 2.0, 5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(2), 7)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(28, [1, 2, 3], 7, 2)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"height": 1, "x": 2, "y": 3}, 1)

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3), 2, 3, 4)

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1, 2, 3}, 4, 0, 5)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(11, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(100, float('nan'), 12)

    # test height value
    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(13, -5, 13)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 2, 3)


class TestRectangle_x_arg(unittest.TestCase):
    """Unittests for testing x coordinate of the Rectangle class."""
    # Test x types
    def test_None_x(self):	
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 2, 0)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 3, "NotAnInt", 2, 1)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 3, 2.0, 5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(2), 7)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(28, 50, [1, 2, 3], 7, 2)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, {"x": 1, "x": 2, "y": 3}, 1)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2, 3), 3, 4)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 1, {1, 2, 3}, 0, 5)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, True)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(11, 11, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 100, float('nan'), 12)

    # test x value
    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(13, 15, -5, 13)


class TestRectangle_y_arg(unittest.TestCase):
    """Unittests for testing y of the Rectangle class."""
    # Test y types
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 1, 1, None, 0)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 5, 0, "NotAnInt", 1)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(15, 15, 5, 2.0, 5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 90, 1, complex(2), 7)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 2, [1, 2, 3], 2)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 4, 2, {"y": 1, "x": 2, "y": 3}, 1)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (1, 2, 3), 4)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 5, {1, 2, 3}, 5)

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, True)

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2 ,3, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 0, float('nan'), 12)

    # test y value
    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 0, -5, 13)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Rectangle attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, "x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, 0, "y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", "x", 0)

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "height", 0, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "x", "y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_one_arg(self):
        s = Rectangle(7, 7, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.area(0)

    def test_area(self):
        self.assertEqual(Rectangle(999999, 999999, 0, 0, 10).area(), 999998000001)

    def test_area_changed_attributes(self):
        s = Rectangle(7, 1, 1, 0)
        s.height = 5
        s.width = 3
        self.assertEqual(15, s.area())

if __name__ == "__main__":
    unittest.main()
