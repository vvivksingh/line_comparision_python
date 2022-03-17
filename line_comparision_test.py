from line_comp import Line, line_len_dict
from line_comp import LineComparision


def test_calculate_length():
    line_dict = {"name": "line1", "x1": 3, "y1": 6, "x2": -2, "y2": -4}
    line = Line(line_dict)
    length = line.calculate_length()
    assert length == 11.180339887498949










