import csv

from common import box_mapping
from data_types import Box, Column, Row, Cell

class Matrix(object):
    
    def __init__(self,size,source_file):
        self.size = size
        self.boxes = []
        self.rows = []
        self.columns = []
        self.cells = []
        for i in range(1, size + 1):
            self.boxes.append(Box(i))
            self.rows.append(Row(i))
            self.columns.append(Column(i))
        for i in range(1, (size ** 2) + 1):
            self.cells.append(Cell(i))
        data = read_file(source_file)
        for item in data:
            self.columns[int(item[0])].insert(int(item[2]))
            self.rows[int(item[1])].insert(int(item[2]))
            self.boxes[box_mapping(int(item[0]),int(item[1]))].insert(int(item[2]))
            self.cells[cell_mapping(int(item[0]),int(item[1]))].insert(int(item[2]))
        for cell in self.cells:
            cell.set_location(self.size)
    
    def solve(self):
        print("solving...")
        
def read_file(filename):
    response = []
    with open(filename, newline='') as csvfile:
        values = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in values:
            response.append((row[0],row[1],row[2]))
    return response


def cell_mapping(column, row):
    return column * 9 + row
