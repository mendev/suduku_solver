import subprocess
import pytest

@pytest.fixture
def run_application():
    def _run_application(run_arguments):
        # Setup code (if needed) before running the application
        command_line = ['/Users/nadav.sorek/factory/python/suduku_solver/.venv/bin/python', '/Users/nadav.sorek/factory/python/suduku_solver/main/app.py']
        command_line = command_line + run_arguments
        # Run the application
        process = subprocess.Popen(command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr
    return _run_application
 
def test_cell_54_simple_input(run_application):
    returncode, stdout, stderr = run_application(['/Users/nadav.sorek/factory/python/suduku_solver/main/simple.csv', '-s', '9', '--no_solve', '-c', '54'])

    # Perform checks on the return code, stdout, and stderr
    assert returncode == 0
    assert b'Cell 54 values [6]' in stdout, "Expected cell 54 value not found in stdout"
    assert b'Cell 54 location is (6, 0, 6)' in stdout, "Cell 54 location is wrong"
    assert b'Cell 54 is solved - True' in stdout, "Expected cell 54 sloved wrong in stdout"

def test_cell_36_simple_input(run_application):
    returncode, stdout, stderr = run_application(['/Users/nadav.sorek/factory/python/suduku_solver/main/simple.csv', '-s', '9', '--no_solve', '-c', '36'])

    # Perform checks on the return code, stdout, and stderr
    assert returncode == 0
    assert b'Cell 36 values [None, None, None, None, None, None, None, None, None]' in stdout, "Expected cell 36 value not found in stdout"
    assert b'Cell 36 location is (4, 0, 3)' in stdout, "Cell 36 location is wrong"
    assert b'Cell 36 is solved - False' in stdout, "Expected cell 36 sloved wrong in stdout"
