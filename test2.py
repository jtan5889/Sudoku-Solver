"""
Made by: Jason Tan Tze Hong

This is a simple program that attempts to solve easy to intermediate sudoku puzzles.
Does not work on harder puzzles due to lack of implementation of more complex sudoku rules
This is by no means the best of most efficient way of doing so, and is done by myself.

Terminology:
row: the puzzle in the format of rows (top to bottom) in lists
col: the puzzle in the format of columns (left to right) in lists
box: the puzzle in the format of boxes or the 3x3 grid (left to right, then top to bottom) in lists

puzzle row/col/box refers to the list that contains the possible numbers for the cell in
their respective formats. This is written as p_row,p_col,p_box in the code below


*************
How it works:

-For cells without a number (empty cells) its corresponding location in the puzzle row/col/box
will contain a list containing the possible numbers. eg. [1,2,6] means the cell can be either
1, 2 or 6

-Using existing numbers in the puzzle, attempt to remove possibilities in p_row/col/box

-When a cell's possibility list is reduced to a size of 1, then it must be that number,
then fill in the number, reflect the changes and repeat again until the puzzle is completely solved
"""

#This is where you input the puzzle you wish to solve

r1=[1,2,0,6,0,0,4,0,9] 
r2=[0,0,0,0,0,4,1,0,2]
r3=[0,0,6,0,1,0,5,0,0]
r4=[6,0,8,1,0,0,0,0,0]
r5=[0,5,0,3,4,2,0,0,0]
r6=[4,0,2,0,0,8,0,0,0]
r7=[8,0,7,0,0,0,3,0,5]
r8=[3,0,4,0,0,0,0,2,6]
r9=[0,0,0,4,0,0,0,0,0]

#Initializing the data structure for the program 
pr1 = [0,0,0,0,0,0,0,0,0]
pr2 = [0,0,0,0,0,0,0,0,0] 
pr3 = [0,0,0,0,0,0,0,0,0] 
pr4 = [0,0,0,0,0,0,0,0,0] 
pr5 = [0,0,0,0,0,0,0,0,0] 
pr6 = [0,0,0,0,0,0,0,0,0] 
pr7 = [0,0,0,0,0,0,0,0,0] 
pr8 = [0,0,0,0,0,0,0,0,0] 
pr9 = [0,0,0,0,0,0,0,0,0]

c1,c2,c3,c4,c5,c6,c7,c8,c9 = [],[],[],[],[],[],[],[],[]
b1,b2,b3,b4,b5,b6,b7,b8,b9 = [],[],[],[],[],[],[],[],[]
pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8,pc9 = [],[],[],[],[],[],[],[],[]
pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9 = [],[],[],[],[],[],[],[],[]

box = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
column = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
row = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
puzzle_row = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9]
puzzle_col=[pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8,pc9]
puzzle_box = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9]




def row_to_col(input_row,input_col):                #Converts the puzzle from row to column format
    for b in input_col:
        for a in input_row:
            b.append(a[input_col.index(b)])
    return input_col

def row_to_box(input_row,input_box):                #Converts the puzzle from row to box format
    new_box = []
    for d in range(0,9,3):
        for e in range(d,d+3):
            input_box[d] = input_box[d] + input_row[e][0:3]
            input_box[d+1] = input_box[d+1] + input_row[e][3:6]
            input_box[d+2] = input_box[d+2] + input_row[e][6:9]
    return input_box

def row_to_p_row(input_row,input_p_row):            #Converts the puzzle from row to puzzle_row format
    for x in input_row:
        counter = 0
        for v in x:
            if v == 0:
                input_p_row[row.index(x)][counter] = [1,2,3,4,5,6,7,8,9]
            counter += 1
    return input_p_row

def snum_p_row(input_row,input_col,input_box,input_p_row):   #PREPROCESSING STEP
    for x in input_row:   
        for b in x:
            if b != 0:
                for c in input_p_row[input_row.index(x)]:
                    if c != 0:
                        if b in c:
                            c.remove(b)
    for x in input_col:
        for b in x:
            if b != 0:
                for c in input_p_row:
                    if c[input_col.index(x)] != 0:
                        if b in c[input_col.index(x)]:
                            c[input_col.index(x)].remove(b)

    index_r = 0
    index_c = 0
    for x in input_box:
        index_r = input_box.index(x) // 3
        index_c = input_box.index(x) % 3
        for b in x:
            if b != 0:
                for c in range((index_r * 3),((index_r * 3) + 3)):
                    for d in range((index_c * 3),((index_c * 3)+ 3)):
                        if input_p_row[c][d] != 0:
                            if b in input_p_row[c][d]:
                                input_p_row[c][d].remove(b)
    return input_p_row

def list_to_set(input_list):                #Removes duplicates from list(set)
    temp = []
    temp_list = []
    for x in input_list:
        temp = []
        for a in x:
            if a == 0:
                continue
            else:
                temp += a
        temp_list.append(temp)
        
    return temp_list

def unique_ele_p_box(temp_list,row,col,box,p_row,p_col,p_box):  #Finds a cell with only 1 item in p_box
    t_list = temp_list
    ab = []
    c = []
    for a in t_list:
        c.clear()
        list_dup = a.copy()
        ab = list(set(list_dup))
        for b in ab:
            count = 0
            for x in a:
                if x == b:
                    count += 1
            if count == 1:
                c.append(b)
        if len(c) != 0:
            for b in p_box[t_list.index(a)]:      
                if b != 0:
                    for d in c:
                        if d in b:           #Sets cell in p_box to 0, and replaces the cell in Row, Column, Box to the number 
                            index1 = ((t_list.index(a)//3)*3) + (p_box[t_list.index(a)].index(b) // 3)
                            index2 = ((t_list.index(a) % 3)*3) + (p_box[t_list.index(a)].index(b) % 3)
                            p_row[index1][index2] = 0
                            p_col[index2][index1] = 0
                            row[index1][index2] = d
                            col[index2][index1] = d
                            box[t_list.index(a)][p_box[t_list.index(a)].index(b)] = d
                            p_box[t_list.index(a)][p_box[t_list.index(a)].index(b)] = 0
                            for n in p_row[index1]:
                                if n != 0:
                                    if d in n:
                                        n.remove(d)
                            for o in p_col[index2]:
                                if o != 0:
                                    if d in o:
                                        o.remove(d)
                            for p in p_box[t_list.index(a)]:
                                if p != 0:
                                    if d in p:
                                        p.remove(d)
    return row,col,box,p_row,p_col,p_box

def unique_ele_p_row(temp_list,row,col,box,p_row,p_col,p_box):  #Finds a cell with only 1 item in p_row
    t_list = temp_list
    ab = []
    c = []

    for a in t_list:
        c.clear()
        list_dup = a.copy()
        ab = list(set(list_dup))
        for b in ab:
            count = 0
            for x in a:
                if x == b:
                    count += 1
            if count == 1:
                c.append(b)
        if len(c) != 0:
            for b in p_row[t_list.index(a)]:      
                if b != 0:
                    for d in c:
                        if d in b:           #Sets cell in p_row to 0, and replaces the cell in Row, Column, Box to the number 
                            index1 = t_list.index(a)
                            index2 = p_row[t_list.index(a)].index(b)
                            p_row[index1][index2] = 0
                            p_col[index2][index1] = 0
                            row[index1][index2] = d
                            col[index2][index1] = d
                            box[((index1 //3)*3)+(index2//3)][((index1%3)*3)+(index2%3)] = d
                            p_box[((index1 //3)*3)+(index2//3)][((index1%3)*3)+(index2%3)] = 0
                            for n in p_row[index1]:
                                if n != 0:
                                    if d in n:
                                        n.remove(d)
                            for o in p_col[index2]:
                                if o != 0:
                                    if d in o:
                                        o.remove(d)
                            for p in p_box[((index1 //3)*3)+(index2//3)]:
                                if p != 0:
                                    if d in p:
                                        p.remove(d)
    return row,col,box,p_row,p_col,p_box

def unique_ele_p_col(temp_list,row,col,box,p_row,p_col,p_box): #Finds a cell with only 1 item in p_col
    t_list = temp_list
    ab = []
    c = []

    for a in t_list:
        c.clear()
        list_dup = a.copy()
        ab = list(set(list_dup))
        for b in ab:
            count = 0
            for x in a:
                if x == b:
                    count += 1
            if count == 1:
                c.append(b)
        if len(c) != 0:
            for b in p_col[t_list.index(a)]:      
                if b != 0:
                    for d in c:
                        if d in b:           #Sets cell in p_col to 0, and replaces the cell in Row, Column, Box to the number 
                            index1 = t_list.index(a)
                            index2 = p_col[t_list.index(a)].index(b)
                            p_row[index2][index1] = 0
                            p_col[index1][index2] = 0
                            row[index2][index1] = d
                            col[index1][index2] = d
                            box[((index2 //3)*3)+(index1//3)][((index2%3)*3)+(index1%3)] = d
                            p_box[((index2 //3)*3)+(index1//3)][((index2%3)*3)+(index1%3)] = 0
                            for n in p_row[index2]:
                                if n != 0:
                                    if d in n:
                                        n.remove(d)
                            for o in p_col[index1]:
                                if o != 0:
                                    if d in o:
                                        o.remove(d)
                            for p in p_box[((index2 //3)*3)+(index1//3)]:
                                if p != 0:
                                    if d in p:
                                        p.remove(d)
    return row,col,box,p_row,p_col,p_box

def program_flow(row):
    col = row_to_col(row,column)
    box_1 = row_to_box(row,box)
    row_to_p_row(row,puzzle_row)
    p_row = snum_p_row(row,column,box,puzzle_row)
    p_col = row_to_col(p_row,puzzle_col)
    p_box = row_to_box(p_row,puzzle_box)
    boolean = 0
    while boolean == 0:
        temp_row = list_to_set(p_row)
        temp_box = list_to_set(p_box)
        temp_col = list_to_set(p_col)
        
        row1,col1,box1,p_row1,p_col1,p_box1 = unique_ele_p_box(temp_box,row,col,box_1,p_row,p_col,p_box)
        row2,col2,box2,p_row2,p_col2,p_box2 = unique_ele_p_row(temp_row,row1,col1,box1,p_row1,p_col1,p_box1)
        row3,col3,box3,p_row3,p_col3,p_box3 = unique_ele_p_col(temp_col,row2,col2,box2,p_row2,p_col2,p_box2)
        row,col,box_1,p_row,p_col,p_box = row3,col3,box3,p_row3,p_col3,p_box3
        boolean = 1

        for a in p_row:
            for b in a:
                if b != 0:
                    boolean = 0
        """
        for a in row:
            print(a)
        print()
        """
    return row3
def main():
    completed_puzzle = program_flow(row)
    for a in completed_puzzle:
        print(a)
main()    
