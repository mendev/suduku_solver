import argparse
import sys
from matrix import Matrix

def main():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('source_file')
    parser.add_argument('-s', '--size', type=int)
    parser.add_argument('--no_solve', action='store_true')
    parser.add_argument('-c', '--cell', type=int)
    args = parser.parse_args()
    
    matrix = Matrix(args.size, args.source_file)
    # matrix = Matrix(9, '/Users/nadav.sorek/factory/python/suduku_solver/main/simple.csv')
    if args.no_solve:
        print(f"Cell {args.cell} values {matrix.cells[args.cell].values}")
        print(f"Cell {args.cell} is solved - {matrix.cells[args.cell].is_solved()}")
        print(f"Cell {args.cell} location is {matrix.cells[args.cell].location}")
    else:
        matrix.solve()
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        