import ast
import subprocess
from transpile import PythonToCVisitor

def python_to_c_transpile(python_code):
    tree = ast.parse(python_code)
    visitor = PythonToCVisitor()
    visitor.visit(tree)
    return visitor.c_code

if __name__ == "__main__":
    status = 0
    try:
        with open("PlutoPilot.py", "r") as f:
            python_code = f.read()
            compile(python_code, "PlutoPilot.py", 'exec')
        print(f"PlutoPilot.py has no syntax errors.")
        status = 1
    except SyntaxError as e:
        print(f"Syntax error in PlutoPilot.py at line {e.lineno}: {e.msg}")
        print(e)

    try:
        # Replace 'your_file.py' with the name of your Python file you want to analyze
        filename = 'PlutoPilot.py'

        # Run pylint using the subprocess module4
        process = subprocess.run("python -m pylint PlutoPilot.py", shell=True, capture_output=True)

        # Check the exit code to see if pylint ran successfully
        # print(process)
           

    except Exception as e:
        # Handle exceptions, if any
        print(f"An error occurred: {e}")

    if status:
        c_code = python_to_c_transpile(python_code)

        with open("PlutoPilot.cpp", "w") as f:
            f.write(c_code)
        print(c_code)
