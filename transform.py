import ast
from transpile import PythonToCVisitor

def python_to_c_transpile(python_code):
    tree = ast.parse(python_code)
    visitor = PythonToCVisitor()
    visitor.visit(tree)
    return visitor.c_code

if __name__ == "__main__":
    with open("PlutoPilot.py", "r") as f:
        python_code = f.read()

    c_code = python_to_c_transpile(python_code)
    print(c_code)
