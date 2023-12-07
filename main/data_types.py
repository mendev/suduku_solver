from common import box_mapping 

class Container(object):
    
    def __init__(self, id):
        self.values = [ None ] * 9
        self.id = id

    def in_values(self, number):
        return number in self.values
    
    def insert(self, number):
        self.values.append(number)
        self.values = self.values[-9:]


class Box(Container):
    
    def __init__(self, id):
        super().__init__(id)

    
class Column(Container):
    
    def __init__(self, id):
        super().__init__(id)


class Row(Container):
    
    def __init__(self, id):
        super().__init__(id)
 
        
class Cell(Container):

    def __init__(self, id):
        super().__init__(id)
        self.options = []


    def insert(self, number):
        self.values = [number]
        self.options = [number]

    def set_location(self, size):
        column = int(self.id / (size - 1))
        row = int(self.id % size) - 1
        box = box_mapping(column, row)
        self.location = (column, row, box)
     
    def is_solved(self):
        """
        is this cell solved
        """
        return len(self.options) == 1
       