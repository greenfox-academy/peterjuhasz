
# sudoku = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

# sudoku = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,5,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,3,7,2,8,4],
#           [2,0,0,4,1,9,0,3,5],
#           [0,0,0,0,8,0,0,7,9]]

sudoku = [[6, 7, 2, 1, 9, 5, 3, 4, 0],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 0, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 0, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]]


# sudoku_mod = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,5,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,7,2,8,4],
#           [0,0,0,4,1,9,0,3,5],
#           [0,0,0,0,8,0,0,7,9]]

compare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

check_list = []
def correct_check_list():
    pass

def zero_rowindexes(row):
    zeros_indexes_in_row = []
    for i in range(len(sudoku[row])):
        if sudoku[row][i] == 0:
            zeros_indexes_in_row.append(i)
    return zeros_indexes_in_row

# print(zero_rowindexes(0))

#-----------collect numbers fom row------------------
def collect_numbers_row(row):
    collected_numbers_in_row = []
    for i in range(len(sudoku[row])):
        if sudoku[row][i] != 0:
            collected_numbers_in_row.append(sudoku[row][i])
    return collected_numbers_in_row

# print(collect_numbers_row(0))

# -----------collect numbers from Column---------------
def collect_numbers_column(column):
    collected_numbers_in_column = []
    for i in range(len(sudoku[column])):
        if sudoku[i][column] != 0:
            collected_numbers_in_column.append(sudoku[i][column])
    return collected_numbers_in_column

# print(collect_numbers_column(0))

def collect_numbers_square(row,column):
#  select sarting row position
    if row < 3:
        s_row = 0
    elif row < 6:
        s_row = 3
    else:
        s_row = 6

#  select sarting column position
    if column < 3:
        s_column = 0
    elif column < 6:
        s_column = 3
    else:
        s_column = 6

    square_column = 0
    collected_numbers_in_square = []
    while square_column < 3 :
        for r in range(len(sudoku[:3])):
            if sudoku[s_row][s_column+r] != 0:
                collected_numbers_in_square.append(sudoku[s_row][s_column+r])
        s_row += 1
        square_column += 1
    return collected_numbers_in_square

# print(collect_numbers_square(7,9))

# -----------------------------------------------------------
# 1. sor első nulla eleméhez tartozó számok számok
###################################################
#-------------------LAYER 2.-----------------------
###################################################
def collect_numbers_for_zero(row, column):

    a = collect_numbers_column(column)
    # print (a)

    b = collect_numbers_row(row)
    # print (b)

    c = collect_numbers_square(row, column)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_numbers=(set(compare_list) - set(all_number_for_zero))
    # print(missing_numbers)

    return len(set(all_number_for_zero)) #remove duplicates


#------------------ missing numbers --------------------
def missing_numbers(row, column):

    a = collect_numbers_column(column)
    # print (a)

    b = collect_numbers_row(row)
    # print (b)

    c = collect_numbers_square(row, column)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_number=(set(compare_list) - set(all_number_for_zero))
    print(missing_numbers)

    return missing_number #remove duplicates
# print (collect_numbers_for_zero(0, 0))

def matrix_print():
    print(sudoku_mod[1])
    print(sudoku_mod[2])
    print(sudoku_mod[3])
    print(sudoku_mod[4])
    print(sudoku_mod[5])
    print(sudoku_mod[6])
    print(sudoku_mod[7])
    print(sudoku_mod[8])

###################################################
#-------------------LAYER 3.-----------------------
###################################################

row = 0
# column = zero_rowindexes(0)[0]
def wtf_length(row=0):
    zero_value = []
    # row_zero_value = []
    for r in range(len(zero_rowindexes(row))):
        zero_value.append(collect_numbers_for_zero(row, zero_rowindexes(row)[r]))
    row += 1
    return(len(zero_vale))


while row < 9:
    zero_value = []
    # row_zero_value = []
    for r in range(len(zero_rowindexes(row))):
        zero_value.append(collect_numbers_for_zero(row, zero_rowindexes(row)[r]))
    row += 1
    print (zero_value)

# print(collect_numbers_for_zero(0,2))

# row = 0
# column = zero_rowindexes(0)[0]
#
# run=0
# def solution():
#     while row < 9:
#         # zero_value = []
#         # row_zero_value = []
#         change = 0
#         for r in range(len(zero_rowindexes(row))):
#             if collect_numbers_for_zero(row, zero_rowindexes(row)[r]) == 8:
#                 print("mukodik")
#                 # a = zero_rowindexes(row)[r]
#                 # b = missing_numbers(row, a)
#                 # print(b)
#                 print( int(missing_numbers(row, zero_rowindexes(row)[r])) )
#                 change = int(input("ha cserélni szeretnél írd be a számot:"))
#                 sudoku_mod[row][zero_rowindexes(row)[r]] = change
#                 # matrix_print()
#                 change = 0
#         row += 1
#
#     return sudoku_mod
# #
# print(solution())

    # print (zero_value)
#


# print(collect_numbers_for_zero(0,2))

# print(sudoku[7])
# sudoku[7][7]=missing_numbers(7, 7)
# print(sudoku[7])

# matrix_print()










####