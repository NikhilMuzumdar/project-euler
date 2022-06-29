def sudoku_string_to_sudoku_list(sudoku_string):
    """Takes a sudoku text string (usually 81 long) and returns a list of list (board)"""
    split_strings = []
    for index in range(0, len(sudoku_string), 9):
        split_strings.append(sudoku_string[index: index + 9])

    sudoku_list = []
    for element in split_strings:
        temp_list = []
        for d in element:
            temp_list.append(int(d))
        sudoku_list.append(temp_list)

    return sudoku_list

def read_data_as_string_dict(file_name="coordinates.txt"):
    """Reads the data from text file and returns a dict with "Grid XX" as keys"""
    sudoku_dict = {}
    with open(file_name, mode="r") as file:
        for line in file.readlines():
            data = line.rstrip()
            if "Grid" in data:
                key = data
            else:
                if key in sudoku_dict.keys():
                    sudoku_dict[key] += data
                else:
                    sudoku_dict[key] = data

    return sudoku_dict

def solve_sudoku(sudoku_list):
    """Takes a list of list and returns a solved list of list"""
    from sudoku import Sudoku
    puzzle = Sudoku(3, 3, board=sudoku_list)
    solution = puzzle.solve()
    solution_list = solution.board
    return solution_list


def main():
    """Return the sum of first 3 element in the first row for all solved sudoku(s)"""
    result = 0
    # Read the data into dictionary as a string with Grid No as keys
    sudoku_string_dict = read_data_as_string_dict()

    # Convert the string to a board (list of list) and store in another dict
    sudoku_list_dict = {}
    for key in sudoku_string_dict:
        sudoku_list_dict[key] = sudoku_string_to_sudoku_list(sudoku_string_dict[key])

    # Solve the boards
    sudoku_list_dict_solved = {}
    for key in sudoku_list_dict:
        sudoku_list_dict_solved[key] = solve_sudoku(sudoku_list_dict[key])

    for element in sudoku_list_dict_solved.values():
        str_digit = ""
        for digit in element[0][:3]:
            str_digit += str(digit)
        result += int(str_digit)

    print(f"Sum of the first 3 digits in all 50 solution boards is {result}\n"
          f"This is solved with the help of py-sodoku library")

if __name__ == '__main__':
    main()
