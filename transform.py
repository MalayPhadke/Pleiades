import ast
import subprocess
import os
from transpile import PythonToCVisitor
import re

def python_to_c_transpile(python_code):
    tree = ast.parse(python_code)
    visitor = PythonToCVisitor()
    visitor.visit(tree)
    return visitor.c_code

if __name__ == "__main__":
    status = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source =f"{current_dir}/PlutoPilot.py"
    dest = f"{current_dir}/PlutoPilot.cpp"
    with open(source, "r") as f:
        python_code = f.read()

    try:
        # Run pylint using the subprocess module4
        process = subprocess.run(f"python -m pylint --disable=R,C {current_dir}\PlutoPilot.py", shell=True, capture_output=True)
        # Check the exit code to see if pylint ran successfully
        error = r"^(.*?):(\d+):\d+: ([E]\d{4}): (.*)$"
        warning = r"^(.*?):(\d+):\d+: ([W]\d{4}): (.*)$"
        errors = []
        warnings = []
        output = process.stdout.decode("utf-8")
        
        for line in output.split("\n"):
            # Check if the line contains an error or warning code
            if re.match(error, line):
                errors.append(line)
            elif re.match(warning, line):
                warnings.append(line)

        if process.returncode == 0 or process.returncode == 4:
            status = 1
            print(1)
            print("\n".join(warning for warning in warnings))
        else:
            print("Errors encountered")
            print("\n".join(error1 for error1 in errors))

    except Exception as e:
        print(f"An error occurred: {e}")

    if status:
        c_code = python_to_c_transpile(python_code)

        with open(dest, "w") as f:
            f.write(c_code)
        # print(c_code)
