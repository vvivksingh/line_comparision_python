import logging
import math


logging.basicConfig(filename="line_comp.log", filemode="w")


class Line:
    """
    initialising the coordinates of line and finding the length
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the attribute
        :param x1:coordinates of x-axis for the 1st point
        :param x2:coordinates of x-axis for the 2nd point
        :param y1:coordinates of y-axis for the 1st point
        :param y2:coordinates of y-axis for the 2nd point
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_length(self):
        """
        finding the length
        :return:
        """
        try:
            length = math.sqrt((self.x2 - self.x1)^2 + (self.y2 - self.y1)^2)
            print("Length of the line is : ", length)
        except Exception:
            logging.exception("something went wrong")


if __name__ == "__main__":

    """
    Creating object for Line class and calling calculation
    """
    try:
        line = Line(2, 1, 6, 4)
        line.calculate_length()
    except Exception:
        logging.exception("please enter integer value")