
from matrix import Matrix

def main():
    matrix = Matrix(9, '/Users/nadav.sorek/factory/python/suduku_solver/main/simple.csv')
    matrix.solve()
    print(matrix.cells[56].values)
    print(matrix.cells[71].is_solved())
    print(matrix.cells[61].is_solved())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        