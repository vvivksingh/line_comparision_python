import logging
import math


logging.basicConfig(filename="line_comp.log", filemode="w")


class Line:
    """
    initializing attributes and finding length
    """

    def __init__(self, line_dict):
        """
        Initializing the attribute of a line
        :param line_dict:
        """
        self.name = line_dict.get("name")
        self.x1 = line_dict.get("x1")
        self.y1 = line_dict.get("y1")
        self.x2 = line_dict.get("x2")
        self.y2 = line_dict.get("y2")

    def calculate_length(self):
        """
        calculation for finding the length
        :return:
        """
        try:
            length = math.sqrt((self.x2 - self.x1) * (self.x2 - self.x1) + (self.y2 - self.y1) * (self.y2 - self.y1))
            return f"length is {length}"
        except Exception:
            logging.exception("Calculation error!!!")


class LineComparision:

    def __init__(self):
        self.line_list = []
        self.line_length = []

    def add_line(self, line_l):
        """
        Adding the line in list
        :param line_l:as a object
        """
        try:
            self.line_list.append(line_l)
        except Exception:
            logging.exception("Takes integer value only")

    def display(self):
        """
        Display the input value
        """
        for line_l in self.line_list:
            print("Line name is:- ", line_l.name)
            print("X1 value is:- ", line_l.x1)
            print("Y1 value is:- ", line_l.y1)
            print("X2 value is:- ", line_l.x2)
            print("Y2 value is:- ", line_l.y2)

    def finding_length(self):
        """
        finding the length of line
        """
        for line_l in self.line_list:
            print(line_l.name, line_l.calculate_length())

    def check_equality(self):
        """
        checking the equality of line inputted by the user with comparing
        """
        for i in range(len(self.line_list)):
            for j in range(i + 1, len(self.line_list)):
                if (self.line_list[i].calculate_length()).__eq__(self.line_list[j].calculate_length()):
                    print(f"{self.line_list[i]}  is equal to {self.line_list[j]}")
                else:
                    print(f"{str(self.line_list[i])}  is not equal to {str(self.line_list[j])}")


if __name__ == "__main__":

    line_comaprision = LineComparision()
    try:
        while True:

            print("""Your choices:-
                    1.Add line
                    2.Display
                    3.Find length
                    4.Check Equality
                    """)
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                name = input("Enter line name:- ")
                x1 = int(input("Enter the x1 value:- "))
                y1 = int(input("Enter the y1 value:- "))
                x2 = int(input("Enter the x2 value:- "))
                y2 = int(input("Enter the y2 value:- "))
                line_dict = {"name": name, "x1": x1,"y1": y1 , "x2": x2, "y2": y2}
                line = Line(line_dict)

                line_comaprision.add_line(line)
            elif choice == 2:
                line_comaprision.display()
            elif choice == 3:
                line_comaprision.finding_length()
            elif choice == 4:
                line_comaprision.check_equality()
            else:
                print("Wrong choice!!!")
                break

    except Exception:
        logging.exception("Pass the integer value")