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
            return length
        except Exception:
            logging.exception("Calculation error!!!")


class LineComparision:
    def compare_length(self):
        line1_name = input("Enter name of 1st line you want to compare: ")
        line2_name = input("Enter name of 2nd line you want to compare: ")
        if line_len_dict[line1_name] > line_len_dict[line2_name]:
            print(f"{line1_name} is greater than {line2_name}")
        elif line_len_dict[line1_name] == line_len_dict[line2_name]:
            print(f"{line1_name} is equal to {line2_name}")
        else:
            print(f"{line1_name} is smaller than {line2_name}")

    def add_line(self, ):
        line_len_dict.update({name: l_length})

    def display(self):
        print(line_len_dict)


if __name__ == "__main__":
    line_len_dict = {}
    line_comparision = LineComparision()

    try:
        while True:

            print("""Your choices:-
                    1.Add line
                    2.Display
                    3.Check Equality
                    4.Exit
                    """)
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                name = input("Enter line name:- ")
                x1 = int(input("Enter the x1 value:- "))
                y1 = int(input("Enter the y1 value:- "))
                x2 = int(input("Enter the x2 value:- "))
                y2 = int(input("Enter the y2 value:- "))
                line_dict = {"name": name, "x1": x1, "y1": y1, "x2": x2, "y2": y2}
                line = Line(line_dict)
                l_length = line.calculate_length()
                line_comparision.add_line()
                print(f"{name} is added successfully")

            elif choice == 2:
                line_comparision.display()

            elif choice == 3:
                line_comparision.compare_length()

            else:
                break

    except Exception:
        logging.exception("Pass the integer value")
