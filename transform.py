import ast
import subprocess
import os
from transpile import PythonToCVisitor
import re, keyword

def python_to_c_transpile(python_code):
    tree = ast.parse(python_code)
    visitor = PythonToCVisitor()
    visitor.visit(tree)
    return visitor.c_code
def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

if __name__ == "__main__":
    result = { "errors": [], "warnings": [], "code" : 0}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source = f"{current_dir}/PlutoPilot.py"
    dest = f"{current_dir}/PlutoPilot.cpp"
    with open(source, "r") as f:
        python_code = f.read()

    try:
        # Run pylint using the subprocess module
        process = subprocess.run(f"python -m pylint --disable=R,C {source}", shell=True, capture_output=True)
        # Check the exit code to see if pylint ran successfully
        error = r"^(.*?):(\d+):\d+: ([E]\d{4}): (.*)$"
        warning = r"^(.*?):(\d+):\d+: ([W]\d{4}): (.*)$"
        output = process.stdout.decode("utf-8")

        for line in output.split("\n"):
            # Check if the line contains an error or warning code
            if re.match(error, line):
                path, line_no,  error_code, error_message = re.match(error, line).groups()
                result["errors"].append({
                    "path": path,
                    "line": int(line_no),
                    "code": error_code,
                    "message": error_message.strip()
                })
            elif re.match(warning, line):
                path, line_no, warning_code, warning_message = re.match(warning, line).groups()
                result["warnings"].append({
                    "path": path,
                    "line": int(line_no),
                    "code": warning_code,
                    "message": warning_message.strip()
                })

        if process.returncode == 0 or process.returncode == 4:
            result["code"] = 1

        print(print_colored(result["code"], "green"))
        for error in result["errors"]:
            error_output = f"File {error['path']}, at line {error['line']} \n{error['message']} \n"
            print(print_colored(error_output, "red"))
        for warning in result["warnings"]:
            warning_output = f"File {warning['path']}, at line {warning['line']} \n{warning['message']} \n"
            print(print_colored(warning_output, "yellow"))

    except Exception as e:
        print(f"An error occurred: {e}")

    if result["code"]:
        c_code = python_to_c_transpile(python_code)

        with open(dest, "w") as f:
            f.write(c_code)
        # print(c_code)
